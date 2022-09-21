from django.shortcuts import render
from django.http import JsonResponse
from testing.models import *
# Create your views here.
#this is updated version views
def getbook(request):
    city = City.objects.all()
    subcategories=Subcategory.objects.all()
    newsubcategory=[]
    for subcategory in subcategories:
        package=Package.objects.filter(subcategory=subcategory)
        package_list=[]
        for p in package:
            print('---------------------------')
            print('package start')
            price_data=Price.objects.filter(package=p)
            price_list=[]
            for price in price_data:
                print('price start')
                price_dict={
                    'area':price.area,
                    'price':price.price,
                    'city':price.city.name
                }
                price_list.append(price_dict)
                print('price finish')
            
            print(price_list)
            package_dict={
                'id':p.id,
                'prices':price_list
            }
            package_list.append(package_dict)
            print('package finish')
            print('---------------------------')
        print(package_list)
        subcategory_dict={
            'name':subcategory.name,
            'package':package_list
        }
        newsubcategory.append(subcategory_dict)
        print('subcategory finish')
    print(newsubcategory)
    a={
        'sub_list':newsubcategory
    }

    return JsonResponse(a,safe=False)


#     {
# "subcategories":[{"name":"s1","slug":"s2","packages":[{"name":"p1","prices":[{"price":40,"city":"cuttack"},{"price":140,"city":"bhubaneswar"}]},{"name":"p2","prices":[{"price":40,"city":"cuttack"},{"price":140,"city":"bhubaneswar"},4,5,6]}]},{"name":"s1","slug":"s2","packages":[{"name":"p1","prices":[{"price":40,"city":"cuttack"},{"price":140,"city":"bhubaneswar"}]},{"name":"p2","prices":[{"price":40,"city":"cuttack"},{"price":140,"city":"bhubaneswar"},4,5,6]}]}]
# }

