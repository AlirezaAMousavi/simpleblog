from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categorys = models.ManyToManyField(Category, related_name='articles')
    title = models.CharField(max_length=20)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    num_comments = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True)
    article_image = models.ImageField(upload_to='images/articles')

    class Meta:
        ordering = ['-pub_date']

    def save(
            self,
            *args,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f'{self.title}-{self.content[:30]}'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.parent and self.parent.article != self.article:
            raise ValidationError(f'Replies must be to comments on the same article.'
                                  f'You should choose <{self.parent.article.title}>')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.author}: {self.content[:30]}'


class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateField(blank=True, default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Contact Us'
