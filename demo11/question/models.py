from django.db import models

# Create your models he


class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def _str_(self):
        return self.course_name



     

