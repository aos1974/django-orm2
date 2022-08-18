from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Tag, ArticleTag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    pass

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_clicked = False
        for form in self.forms:
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            if is_main_clicked and form.cleaned_data.get('is_main'):
                raise ValidationError('ОШИБКА: Только одна Тема может быть основной!')
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            is_main_clicked = is_main_clicked or form.cleaned_data.get('is_main')            
        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInLine(admin.TabularInline):
    model = ArticleTag
    extra = 1
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine,]

