from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Course(models.Model):
    STATUS_CHOICES = (
        ('پیش نویس', 'پیش نویس'),
        ('منتشر شده', 'منتشر شده'),
    )    ]
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextFiled()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='پیش نویس')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title