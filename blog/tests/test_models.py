from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Author, Blog, Comment
from django.utils import timezone


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create user (will also create an author instance at user.author)
        user = User.objects.create_user(username='testuser1', password='12345') 
        user.save()
        
    def test_get_absolute_url(self):
        author=Author.objects.get(id=1)       
        self.assertEquals(author.get_absolute_url(),'/blog/blogger/1')
           
    def test_user_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('user').verbose_name
        self.assertEquals(field_label,'user')
        
    def test_bio_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('bio').verbose_name
        self.assertEquals(field_label,'bio')

    def test_bio_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('bio').max_length
        self.assertEquals(max_length,500)
        
    def test_object_name(self):
        author=Author.objects.get(id=1)
        expected_object_name = author.user.username
        self.assertEquals(expected_object_name,str(author))


class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create user (will also create an author instance at user.author)
        user = User.objects.create_user(username='testuser1', password='12345') 
        user.save()
        user.author.bio='This is a bio'
        blog = Blog.objects.create(title='Test Blog 1',author=user.author,text='Test Blog 1 Text')
        
    def test_get_absolute_url(self):
        blog=Blog.objects.get(id=1)       
        self.assertEquals(blog.get_absolute_url(),'/blog/1')
           
    def test_title_label(self):
        blog=Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')
        
    def test_title_max_length(self):
        blog=Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEquals(max_length,200)
        
    def test_text_label(self):
        blog=Blog.objects.get(id=1)
        field_label = blog._meta.get_field('text').verbose_name
        self.assertEquals(field_label,'text')
        
    def test_text_max_length(self):
        blog=Blog.objects.get(id=1)
        max_length = blog._meta.get_field('text').max_length
        self.assertEquals(max_length,None)

    def test_date_label(self):
        blog=Blog.objects.get(id=1)
        field_label = blog._meta.get_field('created_date').verbose_name
        self.assertEquals(field_label,'created date')
        
    def test_date(self):
        blog=Blog.objects.get(id=1)
        the_date = blog.created_date.date()
        self.assertEquals(the_date,timezone.now().today().date())

    def test_object_name(self):
        blog=Blog.objects.get(id=1)
        expected_object_name = blog.title
        self.assertEquals(expected_object_name,str(blog))


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create users (will also create author instances at user.author)
        user1 = User.objects.create_user(username='testuser1', password='12345') 
        user1.save()
        user2 = User.objects.create_user(username='testuser2', password='12345') 
        user2.save()
        user1.author.bio='This is a bio'
        blog = Blog.objects.create(title='Test Blog 1',author=user1.author,text='Test Blog 1 Text')
        comment=Comment.objects.create(text='Test Blog 1 Comment 1 Text', author=user2.author,blog=blog)

        
    def test_text_label(self):
        comment=Comment.objects.get(id=1)
        field_label = comment._meta.get_field('text').verbose_name
        self.assertEquals(field_label,'text')
        
    def test_text_max_length(self):
        comment=Comment.objects.get(id=1)
        max_length = comment._meta.get_field('text').max_length
        self.assertEquals(max_length,None)
           
    def test_author_label(self):
        comment=Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEquals(field_label,'author')
        
    def test_date_label(self):
        comment=Comment.objects.get(id=1)
        field_label = comment._meta.get_field('created_date').verbose_name
        self.assertEquals(field_label,'created date')
        
    def test_blog_label(self):
        comment=Comment.objects.get(id=1)
        field_label = comment._meta.get_field('blog').verbose_name
        self.assertEquals(field_label,'blog')

    def test_object_name(self):
        comment=Comment.objects.get(id=1)
        expected_object_name = ''
        len_title=75
        if len(comment.text)>len_title:
            expected_object_name=comment.text[:len_title] + '...'
        else:
            expected_object_name=comment.text
            
        self.assertEquals(expected_object_name,str(comment))