from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name must be start with r')
    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # read_only_fields=['name','roll']
        # extra_kwargs={'name':{'read_only':True}}

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'sabrina' and ct.lower() != 'chittagong':
    #         raise serializers.ValidationError('City must be Chittagong')
    #     return data
