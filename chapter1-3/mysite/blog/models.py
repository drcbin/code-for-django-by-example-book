from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self, ): # 过滤出仅发布过的文章
        return super(PublishedManager, self).get_queryset().filter(status='published')



class Post(models.Model): 
    STATUS_CHOICES = (
                ('draft', 'Draft'), # 草稿
                ('published', 'Published'), # 发布
            )

    objects = models.Manager()
    published = PublishedManager()

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES,
                              default='draft')



    class Meta:
        ordering = ('-publish', )



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug])
