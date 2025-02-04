from rest_framework import generics
from .models import Student
from .serializers import StudentAPISerializer


class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentAPISerializer
