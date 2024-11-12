
from rest_framework import serializers
from .models import Student
   
# class StudentSerializer(serializers.Serializer):
#     id= serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
    # city = serializers.CharField(max_length=100)
    # roll = serializers.IntegerField()

#     def create(self, validated_data):
#             return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.city = validated_data.get('city', instance.city)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'