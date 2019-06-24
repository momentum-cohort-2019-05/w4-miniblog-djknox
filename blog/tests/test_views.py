from django.test import TestCase

# Create your tests here.
from blog.models import Blog, Author
from django.urls import reverse
from django.contrib.auth.models import User #Blog author or commenter

class BlogListView(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # create a test user (this will also create an author instance at user.author)
        user = User.objects.create_user(username='testuser', password='12345') 
        user.save()
        
        number_of_blogs = 13
        for blog_num in range(number_of_blogs):
           Blog.objects.create(title=f'Test Blog {blog_num}s',author=user.author,text=f'Test Blog {blog_num}s Description')
    
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/blog/blogs/') 
        self.assertEqual(resp.status_code, 200)  
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blogs'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blogs'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/blog_list.html')

    def test_pagination_is_five(self):
        resp = self.client.get(reverse('blogs'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertEqual( len(resp.context['blog_list']), 5)