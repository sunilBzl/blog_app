from django.db import models
from django.conf  import settings


# Create your models here.

CATEGORY_CHOICES = [
        ('T', 'Technology'),
        ('N', 'News'),
        ('M', 'Movies'),
        ('L', 'LifeStyle'),
        ('TB', 'Travel'),
        ('MS', 'Music'),
        ('S', 'Sports')
]


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()
    intro = models.TextField()
    blog_type = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
    )
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
