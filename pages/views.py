from django.shortcuts import render
# gelen requestlere cevap vermek icin
# from django.http import HttpResponse , duzenleme, buraya geri donus icin render kullanirim ve html dosyasi donmesini isterim
from django.http import HttpResponseRedirect
# from pages.models import Booking
# ilk view fonksiyonu


def index(request):
    # buraya otomatik bir sekilde gider ve templates dosyasindan file'i cagirir
    return render(request, 'index.html')


# def gallery(request):
#     return render(request, 'partials/gallery.html')

def contact(request):
    return render(request, 'partials/contact.html')

# def appointment(request):
#     return render(request, 'partials/appointment.html')

def services(request):
    return render(request, 'partials/services.html')

# def booking(request):
#     booking = Booking.objects.all()

#     if request.method == "POST":
#         your_name = request.POST['your-name']
#         your_surname = request['your-surname']
#         your_email = request.POST['your-email']
#         your_phone = request.POST['your-phone']
#         your_pet = request.POST['your-pet']
#         your_operasion = request.POST('your-operasion')
#         your_time = request.POST['your-time']
#         your_gender = request.POST['your-gender']
#         # obj = Booking(neme=name, surname=surname, email=email, message=message, phone_num=phone_num)
        

#         return render(request, 'partials/appointment.html', {
#             'your_name':your_name,
#             'your_surname':your_surname,
#             'your_email':your_email,
#             'your_phone':your_phone,
#             'your_pet':your_pet,
#             'your_operasion':your_operasion,
#             'your_time':your_time,
#             'your_gender':your_gender
#         })

#     else:
#         return render(request, 'partials/booking.html', {})