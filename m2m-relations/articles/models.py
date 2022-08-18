from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=25, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
    
    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    articles = models.ManyToManyField(Tag, through='ArticleTag')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at',]

    def __str__(self):
        return self.title

class ArticleTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тема', related_name='scopes')
    is_main = models.BooleanField(default='False', verbose_name='Основной')
    
    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'

    def __str__(self):
        return f'{self.article}_{self.tag}'