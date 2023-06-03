from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)
    room_id = models.AutoField(primary_key=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    room = models.OneToOneField(Room, on_delete=models.CASCADE, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
