from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from .models import Comment
from .forms import CommentForm
import markdown

# note: redirect 既可以接收一个 URL 作为参数，
# 也可以接收一个模型的实例作为参数（例如这里的 post）
# 如果接收一个模型的实例，那么这个实例必须实现了 get_absolute_url 方法，
# 这样 redirect 会根据 get_absolute_url 方法返回的 URL 值进行重定向。


def post_comment(request, post_pk):
    '''
    在河里
    :param request:
    :param post_pk:
    :return:
    '''
    post = get_object_or_404(Post, pk=post_pk)
    post.body = markdown.markdown(post.body,
                                  extensions=['markdown.extensions.extra',
                                              'markdown.extensions.codehilite',
                                              'markdown.extensions.toc'])

    if request.method == 'POST':
        form = CommentForm(request.POST) #注意这个地方是获取由post请求传过来的表单数据
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            form = CommentForm()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)


