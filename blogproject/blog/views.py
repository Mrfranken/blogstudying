from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
from comments.forms import CommentForm
import markdown
from django.views.generic import ListView, DetailView

#重要： 将视图函数改写为类视图

# def index(request):
#     # return HttpResponse("欢迎访问我的博客首页!")
#
#     post_list = Post.objects.all() #.order_by('-created_time')
#     context = {
#         'title': '我的博客首页',
#         'welcome': '欢迎访问我的博客首页',
#         'post_list': post_list
#     }
#     return render(request, 'blog/index.html', context=context)


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = "post_list"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'title': '我的博客首页',
            'welcome': '欢迎访问我的博客首页',
        })
        return context


def about(request):
    return render(request, 'blog/about.html')


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
    post.increase_views()
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month)
    return render(request, 'blog/index.html', context={"post_list": post_list})


def category(request, category_id):
    cate = get_object_or_404(Category, pk=category_id)
    post_list = Post.objects.filter(category=cate)
    num_of_post_list = post_list.count()
    return render(request, 'blog/index.html', context={"post_list": post_list,
                                                       "count": num_of_post_list})

