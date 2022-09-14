from rest_framework import serializers
from testing.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','student','name']