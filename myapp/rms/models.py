from django.db import models

# Create your models here.
class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_fullname = models.CharField(max_lenth=230)
    s_address = models.CharField(max_length=123)
    class Meta:
        dba_table = 'student'

class Program(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name =models.CharField(max_length=50)
    p_capacity = models.CharField(max_length=40)
    s_id = models.OneToOneField(Student, on_delete = models.CASCADE)
    class Meta:
        dba_table = 'program'
            
