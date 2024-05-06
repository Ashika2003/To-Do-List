from django.db import models
from django.contrib.auth.models import User
status_choices=[('Completed','Completed'),('Pending','Pending')]
priority_choices=[('High','High'),('Medium','Medium'),('Low','Low')]
# Create your models here.
class TodoModel(models.Model):
    title=models.CharField(max_length=50)
    status=models.CharField(max_length=9 ,choices=status_choices)
    due_date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    priority=models.CharField(max_length=6 ,choices=priority_choices)


