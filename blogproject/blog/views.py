from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
import markdown


def index(request):
    # return HttpResponse("欢迎访问我的博客首页!")

    post_list = Post.objects.all().order_by('-created_time')
    context = {
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页',
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context=context)


def detail(request, pk):
    '''
    get_object_or_404 方法，其作用就是当传入的 pk 对应的 Post 在数据库存在时，
    就返回对应的 post，如果不存在，就给用户返回一个 404 错误，
    表明用户请求的文章不存在。
    :param request:
    :param pk:
    :return:
    '''
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=['markdown.extensions.extra',
                                              'markdown.extensions.codehilite',
                                              'markdown.extensions.toc'])
    return render(request, 'blog/detail.html', context={'post': post})
