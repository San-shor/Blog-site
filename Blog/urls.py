from django.urls import path
from Blog import views
app_name='Blog'
urlpatterns=[
path('',views.Blog_List.as_view(),name='blog_list'),
path('write/',views.Create_blog.as_view(),name='blog_create'),

]
