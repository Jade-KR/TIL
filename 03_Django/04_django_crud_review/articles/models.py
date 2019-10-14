from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'제목: {self.title}, 내용: {self.content}'
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments') 
    # 어떤 게시물을 참조할 수 있도록 만들어줌, 게시글을 삭제하면 모든 댓글이 삭제되도록 하는 옵션, comment_set.all 이 아닌 name에 정의한 이름으로 불러올 수 있음
    content = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk', ]


    def __str__(self):
        # return f'댓글: {self.content}'
        return f'<Article({self.article_id}): Comment({self.pk} - {self.content})>'