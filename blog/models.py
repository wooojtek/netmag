from django.db import models
from django.core.urlresolvers import reverse
import django_filters


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='posts')
 
    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title
 
    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    #posts = models.ManyToManyField(Post, related_name='categories')

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return u'%s' % self.category_name


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['categories']

    # def __init__(self, *args, **kwargs):
    #     super(PostFilter, self).__init__(*args, **kwargs)
    #     self.filters['categories'].extra.update(
    #         {'empty_label': 'All Categories'})