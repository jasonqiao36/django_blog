from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import reverse
from django.utils.html import format_html

from .adminforms import PostAdminForm
from .models import Category, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    list_display = (
        "title",
        "category",
        "status_show",
        "pv",
        "uv",
        "created_time",
        "operator",
    )
    list_filter = ("category", "status", "created_time")
    search_fields = ("title", "category__name", "desc")
    date_hierarchy = "created_time"
    exclude = ("html", "pv", "uv")
    autocomplete_fields = ("category", "tag")

    # 编辑界面
    save_on_top = True

    # form_layout = Fieldset(
    #     "基础信息",
    #     "title",
    #     "slug",
    #     "desc",
    #     Row("category", "status", "is_markdown"),
    #     "content",
    #     "tag",
    # )

    def operator(self, obj):
        return format_html(
            "<a href={}>编辑</a>", reverse("admin:blog_post_change", args=(obj.id,))
        )

    operator.short_description = "操作"


class PostInline(admin.options.InlineModelAdmin):
    fields = ("title", "status")
    extra = 1
    model = Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_time", "is_nav", "operator")
    list_filter = ("status", "is_nav")
    search_fields = ("name",)

    # inlines = (PostInline,)

    def operator(self, obj):
        return format_html(
            "<a href={}>编辑</a>", reverse("admin:blog_category_change", args=(obj.id,))
        )

    operator.short_description = "操作"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_time", "operator")
    list_filter = ("status",)
    search_fields = ("name",)

    def operator(self, obj):
        return format_html(
            "<a href={}>编辑</a>", reverse("admin:blog_tag_change", args=(obj.id,))
        )

    operator.short_description = "操作"
