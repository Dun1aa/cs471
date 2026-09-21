from django.shortcuts import render
from django.http import HttpResponse  # نحتاجه لدالة index2

# Create your views here.

def index(request):  # أول view، يستقبل name من الرابط ويعرضه في القالب
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1=0):  #  view ثاني يستقبل رقم من مسار الرابط
    return HttpResponse("value1 = " + str(val1))

def viewbook(request, bookId):  #  view يعرض تفاصيل كتاب حسب الـ ID
    # افترض إن هذي الكتب جاية من قاعدة بيانات
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book': targetBook}  # book هو اسم المتغير اللي يقرأه القالب
    return render(request, 'bookmodule/show.html', context)