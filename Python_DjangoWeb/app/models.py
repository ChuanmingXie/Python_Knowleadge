"""
Definition of models.
"""

from django.db import models

# Create your models here.
class conentList(models.Model):
    """ 创建章节标题实体 """
    chapterNum=models.CharField(max_length=200)
    chapterTitle=models.CharField(max_length=200)
    chapterAuthor=models.CharField(max_length=200)
    create_house=models.CharField(max_length=200)
    edited_data=models.DateTimeField('date edited')