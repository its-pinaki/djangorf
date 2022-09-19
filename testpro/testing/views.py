from django.shortcuts import render
from testing.models import Book
from django.http import JsonResponse
from testing.models import Student,Book
# Create your views here.
#this is updated version views
def getbook(request):
    data={}
    data['books']={}
    # convert queryset to list
    book = list(Book.objects.values())
    
    # accessing all queryset data
    book1 = Book.objects.all()
    for bo1 in book1:
        pass
        # print(bo1.name)
        # print(bo1.student.name)


    # print(book1)
    for i in book1:
        data['books']['books'+str(i.id)]={}
        data['books']['books'+str(i.id)]['bookname']=i.name
        # accessing foreign key field with its parent model attributes
        data['books']['books'+str(i.id)]['student']=i.student.name
    print(data)
    # accessing filtered queryset data with value
    b = Book.objects.filter(id=6).values()
    for bo in b:
        print(bo['name'])
        # print(bo.student.name)


    book.append(data)
    # returning jsonresponse with 'safe=false'
    return JsonResponse(book,safe=False)

