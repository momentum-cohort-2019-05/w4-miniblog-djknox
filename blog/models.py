from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.template.defaultfilters import truncatechars


class Author(models.Model):
    """Model representing an author."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Author object."""
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Author.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.author.save()


class Blog(models.Model):
    """Model representing a blog post."""
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField(help_text='Write your blog post here.', null=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog."""
        return reverse('blog-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-created_date',]


class Comment(models.Model):
    """Model representing a comment."""
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    text = models.TextField(help_text='Write your comment here.', null=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        """String for representing the Model object."""
        return truncatechars(self.text, 75)

    class Meta:
        ordering = ['created_date',]

