from django.shortcuts import render
from django.http import HttpResponse  # نحتاجه لدالة index2 من لاب 3
from .models import Book
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

def search(request):  # أضفت معالجة النموذج لما يصير إرسال (POST)
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True

            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')

def __getBooksList():  # دالة خاصة ترجع قائمة كتب ثابتة حقت لاب 6
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def add_book(request):
    mybook = Book(
        title="Python and Django",
        author="Duna",
        price=150.0,
        edition=2
    )
    mybook.save()

    return render(request, "bookmodule/index.html")


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains="and")
    return render(
        request,
        "bookmodule/bookList.html",
        {"books": mybooks}
    )

def complex_query(request):#لاب 7 تاسك 4
    mybooks = (
        Book.objects
        .filter(author__isnull=False)
        .filter(title__icontains="and")
        .filter(edition__gte=2)
        .exclude(price__lte=100)[:10]
    )

    if len(mybooks) >= 1:
        return render(
            request,
            "bookmodule/bookList.html",
            {"books": mybooks}
        )
    else:
        return render(request, "bookmodule/index.html")