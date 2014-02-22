from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=55)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.subject