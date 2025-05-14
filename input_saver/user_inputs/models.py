from django.db import models


class UserInput(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50] + "..." if len(self.content) > 50 else self.content
