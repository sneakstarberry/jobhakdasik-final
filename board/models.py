from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.contrib.auth.models import User

Category_select = (
    ('상식', '상식'),
    ('철학', '철학'),
    ('정치', '정치'),
)

class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='img/')
    body = RichTextUploadingField(blank=True, null=True)
    category = models.CharField(max_length=20, choices = Category_select, default = '상식')
    created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)
    like = models.ManyToManyField(User, related_name='like_post', blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite_post', blank=True)


    def summary(self):
        return self.body[:10]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('board.Blog', related_name='comments',on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    comment_like=models.ManyToManyField(User, related_name='like_comment', blank=True)
    comment_dislike=models.ManyToManyField(User, related_name='dislike_comment', blank=True)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text