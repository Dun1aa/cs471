from django.shortcuts import render
from django.http import HttpResponse  # نحتاجه لدالة index2 من لاب 3

# Create your views here.

def index(request):
    return render(request, "bookmodule/index.html")  # شلت name وصارت تعرض صفحة index مباشرة

def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))  # خليتها زي ما هي من لاب 3

def list_books(request):  #  أضفتها عشان تعرض صفحة قائمة الكتب
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):  #  شلت بيانات الكتب اللي كتبتها في لاب 3، وصارت تعرض one_book.html
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):  #  أضفتها عشان تعرض صفحة About
    return render(request, 'bookmodule/aboutus.html')