from django.shortcuts import render
# gelen requestlere cevap vermek icin
# from django.http import HttpResponse , duzenleme, buraya geri donus icin render kullanirim ve html dosyasi donmesini isterim
from .models import Book
# ilk view fonksiyonu


def index(request):
    # buraya otomatik bir sekilde gider ve templates dosyasindan file'i cagirir
    return render(request, 'index.html')


# def gallery(request):
#     return render(request, 'partials/gallery.html')

def contact(request):
    return render(request, 'partials/contact.html')

def services(request):
    return render(request, 'partials/services.html')

def booking(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'partials/booking.html',context)

