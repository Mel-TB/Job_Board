from django.db import models

# Create your models here.
# model => python class
# model represents table in the db
# attributes => fields in table


class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} | {self.company} | Active: {self.is_active}'

# CRUD Operations
# Create
# Read
# Update
# Delete

# model manager => object
# JobPosting.objects.all()
# JobPosting.objects.get(id=1)
# JobPosting.objects.filter(title='job title')
