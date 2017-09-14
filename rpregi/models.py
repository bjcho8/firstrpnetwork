from django.db import models
from django.utils import timezone

class Rplist(models.Model):
    researcher = models.ForeignKey('auth.User')
    ptid = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    summary = models.TextField()
    fundusRt = models.ImageField()
    fundusLt = models.ImageField()
    VisualfieldRt = models.ImageField()
    VisualfieldLt = models.ImageField()

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.ptid

