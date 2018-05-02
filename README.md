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
