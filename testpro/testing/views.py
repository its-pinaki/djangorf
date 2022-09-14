from django.shortcuts import render
from testing.models import Book
from django.http import JsonResponse
from testing.models import Student,Book
# Create your views here.

def getbook(request):
    data={}
    # convert queryset to list
    book = list(Book.objects.values())
    book1 = Book.objects.all()
    for i in book1:
        data['id_'+ str(i.id)]=i.id
    for k,v in data.items():
        b = Book.objects.filter(id=data[k])
        for bo in b:
            data[k]=bo.name
    print(data)
    # returning jsonresponse with 'safe=false'
    return JsonResponse(book,safe=False)

