from django.shortcuts import render,get_object_or_404
from .models import Blog,BlogType
from django.core.paginator import Paginator
# Create your views here.

def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list,3)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['blog_types'] = BlogType.objects.all()
    context['page_of_blogs'] = page_of_blogs
    context['blog_dates'] = Blog.objects.dates("created_time",'month',order="DESC")
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request,blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog,pk=blog_pk)
    return render(request, 'blog/blog_detail.html', context)


def get_blog_bytype(request,blog_type_key):
    context =  {}
    blog_type = get_object_or_404(BlogType,pk = blog_type_key)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render(request, 'blog/blog_with_type.html', context)

def get_blog_date(request,year,month):
    context = {}
    context['blogs'] = Blog.objects.filter(created_time__year=year,created_time__month=month)
    context['blogs_with_date'] = '%s年%s月'%(year,month)
    context['blog_dates'] = Blog.objects.dates('created_time','month',order='DESC')
    return render(request, 'blog/blog_with_date.html', context)