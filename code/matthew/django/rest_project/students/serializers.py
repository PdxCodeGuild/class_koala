from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Student
		fields = ['id', 'first_name', 'last_name', 'cohort', 'favorite_topic', 'favorite_teacher', 'capstone']
		read_only_fields = ['id']