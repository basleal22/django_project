from django.db import models

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=120)#changed from textfield to charfield, max length = required
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(default='write something here',null=True,blank=False)#blank means that the field is rendered,
    #while null means whether a field is required or not
    featured = models.BooleanField(default=True)