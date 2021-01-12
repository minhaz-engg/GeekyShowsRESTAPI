from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Student


def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("Name should be start with r")


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value

    # objects level validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'sanaullah' and city.lower() != 'chittagong':
            raise ValidationError("City must be chittagong")
        return data
