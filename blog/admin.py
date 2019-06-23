from django.contrib import admin
from blog.models import Blog, Author, Comment

# Register your models here.
admin.site.register(Author)
admin.site.register(Comment)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Blog, BlogAdmin)