from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comp(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    complainant_name=models.CharField(max_length=40,verbose_name="Name")
    complaint_type=models.CharField(max_length=50,verbose_name="Type")
    complaint_desc=models.TextField(verbose_name="Description")
    c_date=models.DateField(verbose_name="Date(YYYY-MM-DD)")
    status=models.CharField(max_length=20,choices = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Resolved', 'Resolved')],default='Pending')



    