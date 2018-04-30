from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    # return HttpResponse("欢迎访问我的博客首页!")

    post_list = Post.objects.all().order_by('-created_time')
    context = {
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页',
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context=context)
