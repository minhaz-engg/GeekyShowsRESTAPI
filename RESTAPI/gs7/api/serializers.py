from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # read_only_fields=['name','roll']
        extra_kwargs={'name':{'read_only':True}}