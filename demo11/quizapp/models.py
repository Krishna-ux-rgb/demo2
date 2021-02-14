from django.db import models

# Create your models here.

class Question(models.Model):
    ques_id = models.IntegerField(unique=True)
    title = models.CharField(max_length = 255)
    desc = models.TextField()
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200)

    def __str__(self):
        return self.title
        