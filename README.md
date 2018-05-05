# blogstudying
教程来自https://www.zmrenwu.com/post/2/


# 5.2
今天主要做了index.html和detail.html的侧边栏，
因为侧边栏中最新文章、归档和分类的显示，而这两个
页面的side都是继承自base.html,所以为了不重复获取
侧边栏的内容采取“自定义模板标签”的方式，在应用目录下
新建templatetags的包，然后使用@register.simple_tag
装饰我们需要的函数（@register.simple_tag还不理解，后期
需要理解）；
然后来base.html中使用{% load blog_tags%}去load这个
py文件，最后需要使用时e.g.
{% get_recent_posts as recent_post_list %}
这条语句用来将blog_tags.py中的函数获取然后给它定义一个
别名，其他用法与模板标签一致.

# 5.3
今天主要做了侧边栏的分类与归档的功能，主要实现方式是
e.g.假设现在点击了某一个分类，这个分类会向发起一个
url请求，并在请求中携带参数，view接收这个请求后根据
参数使用filter去查询数据库，返回结果后丢到index.html
进行显示

# 5.5
今天主要是实现评论的功能，首先评论分为
1. 先建立评论的模型类Comment，将Comment与Post做外键关联;
2. 创建form表单类，在类中将模型类Comment与此类关联;
3. 在模板中{{form.name}}将自动渲染成表单;
4. 在处理表单post请求的视图函数中验证表单数据的合法性，如果表单
为空也应该注意点击提交后然后
将传过来的对应的post文章id与此时的表单数据关联，然后存入数据库，
再重定向或更新页面;
5. 所以要注意一个问题，不管现在一篇文章有没有评论，在首次进入到
文章详情函数的时候，都应该初始化表单类并传入到模板，都应该使用此时
的post去获得相应的评论并传到到模板（因为Comment类和Post类关联了
所以能获取到）;
6. 显示评论内容

