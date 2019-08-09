from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)#최초 생성하면 끝
    updated_at = models.DateTimeField(auto_now=True)#계속 수정됨

    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'