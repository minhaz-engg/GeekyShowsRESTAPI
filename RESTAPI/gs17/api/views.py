from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print("********list********")
        print(f"Basename: {self.basename}")
        print(f"Action: {self.action}")
        print(f"Detail: {self.detail}")
        print(f"Suffix: {self.suffix}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print("********retrieve********")
        print(f"Basename: {self.basename}")
        print(f"Action: {self.action}")
        print(f"Detail: {self.detail}")
        print(f"Suffix: {self.suffix}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        print("********create********")
        print(f"Basename: {self.basename}")
        print(f"Action: {self.action}")
        print(f"Detail: {self.detail}")
        print(f"Suffix: {self.suffix}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        print("********update********")
        print(f"Basename: {self.basename}")
        print(f"Action: {self.action}")
        print(f"Detail: {self.detail}")
        print(f"Suffix: {self.suffix}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Complete Data Updated!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        print("********partial update********")
        print(f"Basename: {self.basename}")
        print(f"Action: {self.action}")
        print(f"Detail: {self.detail}")
        print(f"Suffix: {self.suffix}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Partial Data Updated!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        print("********destory********")
        print(f"Basename: {self.basename}")
        print(f"Action: {self.action}")
        print(f"Detail: {self.detail}")
        print(f"Suffix: {self.suffix}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg": "Data Deleted"})
