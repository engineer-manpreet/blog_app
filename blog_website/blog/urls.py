from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='blogpost_list'),
    path('<int:id>/', views.blogpost_detail, name='blogpost_detail'),
    ]