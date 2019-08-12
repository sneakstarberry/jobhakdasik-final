from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class Debate(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(blank=True)
    body =  RichTextUploadingField(blank=True, null=True)
    
    agree = models.ManyToManyField(User, related_name='agree_post', blank=True)
    disagree = models.ManyToManyField(User, related_name='disagree_post', blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
        

class Debate_Comment(models.Model):
    debate_post = models.ForeignKey('debate.Debate', related_name='debate_comments', on_delete=models.CASCADE)
    debate_author = models.CharField(max_length=200)
    debate_text = models.TextField()
    debate_created_date = models.DateTimeField(default=timezone.now)
    debate_approved_comment = models.BooleanField(default=False)
 
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text