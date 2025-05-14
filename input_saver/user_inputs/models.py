from django.db import models
import json


class UserInput(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50] + "..." if len(self.content) > 50 else self.content


class QA(models.Model):
    name = models.CharField(max_length=20)
    question = models.CharField(max_length=200)  # Django 3.1+ 原生支持 JSONField
    answer = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
