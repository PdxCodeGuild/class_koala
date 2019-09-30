from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['url', 'fist_name', 'last_name', 'cohort', 'favorite_topic', 'favorite_teacher', 'capstone']
