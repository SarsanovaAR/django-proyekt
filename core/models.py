from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    fr_content = models.CharField(max_length=250)
    post_img =models.ImageField(upload_to='rasimlar/')
    post_date = models.DateField()
    

    def __str__(self):
        return self.title