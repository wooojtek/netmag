from django.db import models
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True,
                         always_update=True, editable=True)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', related_name='posts')

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True,
                         always_update=True, editable=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blog.views.category', args=[self.slug])