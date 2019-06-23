from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('<int:pk>/create', views.CommentCreate.as_view(), name='comment-create'),
    path('bloggers/', views.AuthorListView.as_view(), name='authors'),
    path('blogger/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]