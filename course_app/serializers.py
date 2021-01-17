from rest_framework import serializers
from . import models

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = ('id', 'name')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'first_name', 'second_name',
                  'email', 'faculty_id', 'university_id',
                  'department_id', 'stud_or_stuff', 'events')