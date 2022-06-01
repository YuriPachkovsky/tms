from django.db import models
from ckeditor.fields import RichTextField


class BaseContent(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

class TextPost(BaseContent):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    image_content = models.ImageField(upload_to='images', null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def base_content(self):
        return self.content[:50]


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name
