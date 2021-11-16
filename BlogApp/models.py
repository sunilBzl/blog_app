from django.db import models


# Create your models here.

class Post(models.Model):
    title       = models.CharField(max_length=255, unique=True)
    slug        = models.SlugField()
    pub_date    = models.DateField(auto_now_add=True)
    category    = models.ForeignKey("Category", on_delete=models.CASCADE)
    author      = models.ForeignKey('auth.user',
                on_delete=models.CASCADE
                )
    body        = models.TextField()
    img         = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['-id']


    def __str__(self):
        return self.title
    

class Category(models.Model):
    title   = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
