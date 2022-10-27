from django.db import models

class Stream(models.Model):
    stream_name = models.CharField(max_length=100) 

    def __str__(self):
        return self.stream_name

    @classmethod
    def get_allStreams(cls):
        streams = cls.objects.all().order_by('id')
        return streams

class Student(models.Model):
    first_name = models.CharField(max_length=100)    
    second_name = models.CharField(max_length=100)    
    adm_no = models.CharField(max_length=100)    
    age = models.PositiveIntegerField()
    mystream = models.ForeignKey(Stream, null=True, on_delete= models.SET_NULL)            


    def __str__(self):
        return self.first_name

    @classmethod
    def get_allStudents(cls):
        students = cls.objects.all().order_by('id')
        return students