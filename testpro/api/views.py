from testing.models import Student,Book
from .serializers import StudentSerializer,BookSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

#not required pk
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

class BookListCreate(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer

#pk required
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

class BookRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer