from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index_View.as_view(), name='index'),
    path('mbalvi/contactus/',views.Contact_Us_View.as_view(),name='contact'),
    path('mbalvi/blogs/',views.Blog_View.as_view(),name='blog'),
    path('mbalvi/blog_detail/<slug:slug>', views.Blog_detail, name='blog_detail'),
    
    
]
