from django.urls import path
from . import views


urlpatterns = [
    path('',views.blog_list,name='blog_list'),
    path('<int:blog_pk>',views.blog_detail,name='blog_detail'),
    path('type/<int:blog_type_key>',views.get_blog_bytype,name='blog_with_type'),
    path('type/<int:year>/<int:month>',views.get_blog_date,name='blog_with_date')
]