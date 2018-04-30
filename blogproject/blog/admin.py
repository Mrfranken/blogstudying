from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.


class PostInline(admin.StackedInline):
    model = Post
    extra = 2


class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostInline]


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    search_fields = ['title', 'category']
    actions_on_top = True


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)





