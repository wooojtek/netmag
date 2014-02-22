from django.db import models


class Contact(models.Model):
    email = models.EmailField(verbose_name='Your email address', help_text='i.e. email@example.com')
    subject = models.CharField(max_length=55)
    content = models.TextField(verbose_name='Message')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.subject