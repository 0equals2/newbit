from django.db import models
from django.conf import settings
# Create your models here.


class News(models.Model):
    title = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    date_tmp = models.IntegerField(blank=True, null=True)
    tokenized_doc = models.TextField(blank=True, null=True)
    tokenized_title = models.TextField(blank=True, null=True)
    cat_selected = models.TextField(blank=True, null=True)
    topic = models.IntegerField(blank=True, null=True)
    represent = models.IntegerField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'

# class TotalDb(models.Model):
#     title = models.TextField(blank=True, null=True)
#     date = models.TextField(blank=True, null=True)
#     category = models.TextField(blank=True, null=True)
#     content = models.TextField(blank=True, null=True)
#     company = models.TextField(blank=True, null=True)
#     date_tmp = models.BigIntegerField(blank=True, null=True)
#     tokenized_doc = models.TextField(blank=True, null=True)
#     tokenized_title = models.TextField(blank=True, null=True)
#     cat_selected = models.TextField(blank=True, null=True)
#     topic = models.BigIntegerField(blank=True, null=True)
#     represent = models.BigIntegerField(blank=True, null=True)
#     query = models.TextField(blank=True, null=True)