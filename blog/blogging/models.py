from django.db import models
from markdownx.models import MarkdownxField
from django.utils import timezone 
from markdownx.utils import markdownify

class Post(models.Model):
    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '記事'

    def __str__(self):
        return self.title

    title = models.CharField(
        verbose_name = 'タイトル',
        max_length = 100
    )
    abstract = models.CharField(
        verbose_name = '摘要',
        max_length = 100
    )
    text = MarkdownxField(
        '本文',
        help_text='Markdown形式で書いてください。'
    )
    
    updated_at = models.DateTimeField(
        verbose_name = '更新日',
        auto_now = True
    )

    published_at = models.DateTimeField(
        verbose_name = '投稿日',
        null = True,
        blank = True
    )

    def publish(self):
        self.published_at = timezone.auto_now
        self.save()
    
    def to_markdown(self):
        return markdownify(self.text)

