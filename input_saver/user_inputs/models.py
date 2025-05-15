from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

import json

class Questions(models.Model):
    title=models.CharField(max_length=20,unique=True)
    question=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class QA(models.Model):
    question=models.ForeignKey(
        Questions, 
        on_delete=models.CASCADE,  # 当Class1实例删除时，关联的Class2实例也会删除
        related_name='query',  # 反向查询名称（可选）
        null=True
    )
    query = models.CharField(max_length=200)  # Django 3.1+ 原生支持 JSONField
    answer = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question.title

class Rating(models.Model):
    question=models.ForeignKey(
        Questions, 
        on_delete=models.CASCADE,  # 当Class1实例删除时，关联的Class2实例也会删除
        related_name='rating',  # 反向查询名称（可选）
        null=True
    )
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating value from 1 to 5"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.item.name} rated {self.score}/5"