from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse #注意这里不同版本reverse所在包可能不同


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # verbose_name用来指定显示的标题，原生的会显示为 "TITLE"
    title = models.CharField(max_length=70, verbose_name='标题')
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-created_time']  # 指定通过查询得到的结果都按时间倒序排列，省去再在views中排序的代码



