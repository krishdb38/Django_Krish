from django.db import models
from django.conf import settings
from  django.utils.text import slugify

# Create your models here.
class Questions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    group = models.ForeignKey("QuestionGroups", on_delete=models.CASCADE, null=True, blank=True )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Questions, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
class Answers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    
    def __str__(self):
        return self.id
    
class QuestionGroups(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        