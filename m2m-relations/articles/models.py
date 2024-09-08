from django.db import models
from django.core.exceptions import ValidationError


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True,
                              verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    # tagline = models.ManyToManyField(Article, through='Scope',related_name='tags_line')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэг'
        # ordering = ['-name']

    def __str__(self):
        return self.name


class Scope(models.Model):
    scope = models.ForeignKey(
        Article,  on_delete=models.CASCADE, related_name="scopes")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
                            related_name="tags", verbose_name='Раздел')
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'
        ordering = ['-is_main', 'tag']

    # def save(self, *args, **kwargs):
    #     if self.is_main:
    #         if Scope.objects.filter(scope=self.scope, is_main=True).exists():
    #             self.is_main = False
    #     super().save(*args, **kwargs)
