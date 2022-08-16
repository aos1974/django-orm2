from django.contrib import admin

from .models import Article, Tag, ArticleTag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    pass

class ScopeInLine(admin.TabularInline):
    model = ArticleTag
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine,]

