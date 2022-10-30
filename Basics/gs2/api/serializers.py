from rest_framework import serializers
from .models import Student


# def validate_name(self, value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError("Name should start with r")
#

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)

        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # Validating roll number
    # function gets called automatically when is_valid() function is called
    def validate_roll(self, value):
        print("I am validating roll number")
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value

    # Object Level Validation
    def validate(self, data):
        print("I am validating name and city")

        name = data.get('name')
        city = data.get('city')
        print(name)
        print(city)
        if name.lower() == 'chinmay' and city.lower() != 'mumbai':
            raise serializers.ValidationError("City must be mumbai")
        return data
