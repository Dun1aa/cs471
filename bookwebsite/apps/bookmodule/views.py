from django.shortcuts import render
from django.http import HttpResponse  # نحتاجه لدالة index2 من لاب 3

# Create your views here.

def index(request):
    return render(request, "bookmodule/index.html")

def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def html5_links(request):  # دالة جديدة لصفحة الروابط حق لاب 5
    return render(request, 'bookmodule/html5_links.html')

def html5_text_formatting(request):  # تاسك 2 دالة جديدة لصفحة تنسيق النص حق لاب 5
    return render(request, 'bookmodule/html5_text_formatting.html')

def html5_listing(request):  # تاسك3 دالة جديدة لصفحة القوائم حق لاب 5
    return render(request, 'bookmodule/html5_listing.html')

def html5_tables(request):  # تاسك4 دالة جديدة لصفحة الجداول حق لاب 5
    return render(request, 'bookmodule/html5_tables.html')