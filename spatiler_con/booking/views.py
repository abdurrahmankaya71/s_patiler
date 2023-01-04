from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages

def index(request):
    return render(request, "index.html",{})

def booking(request):

    weekdays = validWeekday(22)

    
    validateWeekdays = isWeekdayValid(weekdays)
    

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        animal = request.POST.get('animal')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        time = request.POST.get('time')

        if service == None:
            messages.success(request, "Lütfen Hizmet Türü Seçiniz")
            return redirect('booking')

        
        request.session['day'] = day
        request.session['service'] = service
        request.session['name'] = name
        request.session['surname'] = surname
        request.session['animal'] = animal
        request.session['email'] = email
        request.session['gender'] = gender
        request.session['phone'] = phone
        request.session['time'] = time
        

        return redirect('bookingSubmit')


    return render(request, 'booking.html', {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'items' : Appointment.objects.all(),
        })

def bookingSubmit(request):
    user = request.user
    times = [
        "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 13:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "17:00 - 18:00"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    #Get stored data from django session:
    day = request.session.get('day')
    service = request.session.get('service')
    name = request.session.get('name')
    surname = request.session.get('surname')
    animal = request.session.get('animal')
    gender = request.session.get('gender')
    phone = request.session.get('phone')
    email = request.session.get('email')
    time = request.session.get('time')
    
    
    
    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1:
                            AppointmentForm = Appointment.objects.get_or_create(
                                # user = user,
                                service = service,
                                day = day,
                                time = time,
                                animal = animal,
                                name = name,
                                surname = surname,
                                gender = gender,
                                email = email,
                                phone = phone,
                                
                            )
                            messages.success(request, "Randevunuz Başarılı Bir Şekilde Alındı")
                            return redirect('index')
                        else:
                            messages.success(request, "Seçilen Zaman Daha Önce Ayrıldı!")
                    else:
                        messages.success(request, "Seçilen Gün Dolu!")
                else:
                    messages.success(request, "Seçilen Tarih Yanlış")
            else:
                    messages.success(request, "Seçilen Tarih Doğru Zaman Dilimi İçinde Değil!")
        else:
            messages.success(request, "Lütfen Bir Hizmet Seçin!")


    return render(request, 'bookingSubmit.html', {
        'times':hour,
    })

def userPanel(request):
    user = request.user
    appointments = Appointment.objects.order_by('day', 'time')
    return render(request, 'userPanel.html', {
        'user':user,
        'appointments':appointments,
    })

def userUpdate(request, id):
    appointment = Appointment.objects.get(pk=id)
    userdatepicked = appointment.day
    #Copy  booking:
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    
    weekdays = validWeekday(22)

    
    validateWeekdays = isWeekdayValid(weekdays)
    

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        animal = request.POST.get('animal')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        time = request.POST.get('time')

        
        request.session['day'] = day
        request.session['service'] = service
        request.session['name'] = name
        request.session['surname'] = surname
        request.session['animal'] = animal
        request.session['email'] = email
        request.session['gender'] = gender
        request.session['phone'] = phone
        request.session['time'] = time

        return redirect('userUpdateSubmit', id=id)


    return render(request, 'userUpdate.html', {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'delta24': delta24,
            'id': id,
        })

def userUpdateSubmit(request, id):
    user = request.user
    times = [
        "09:00 - 10:00", "10:00 - 11-00", "11:00 - 12:00", "12:00 - 13:00", "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00", "17:00 - 18:00"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')
    name = request.session.get('name')
    surname = request.session.get('surname')
    animal = request.session.get('animal')
    gender = request.session.get('gender')
    phone = request.session.get('phone')
    email = request.session.get('email')
    time = request.session.get('time')
    
    
    hour = checkEditTime(times, day, id)
    appointment = Appointment.objects.get(pk=id)
    userSelectedTime = appointment.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1 or userSelectedTime == time:
                            AppointmentForm = Appointment.objects.filter(pk=id).update(
                                service = service,
                                day = day,
                                time = time,
                                animal = animal,
                                name = name,
                                surname = surname,
                                gender = gender,
                                email = email,
                                phone = phone,
                            ) 
                            messages.success(request, "Randuvunuz Başarılı Bir Şekilde Düzenlendi!")
                            return redirect('index')
                        else:
                            messages.success(request, "Seçilen Zaman Daha Önce Ayrıldı!")
                    else:
                        messages.success(request, "Seçilen Gün Dolu!")
                else:
                    messages.success(request, "Seçilen Tarih Yanlış")
            else:
                    messages.success(request, "Seçilen Tarih Doğru Zaman Dilimi İçinde Değil!")
        else:
            messages.success(request, "Lütfen Bir Hizmet Seçin!")
        return redirect('userPanel')


    return render(request, 'userUpdateSubmit.html', {
        'times':hour,
        'id': id,
    })

def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    
    items = Appointment.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')

    return render(request, 'staffPanel.html', {
        'items':items,
    })

def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y

def validWeekday(days):
    
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Saturday' or y == 'Wednesday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays
    
def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays

def checkTime(times, day):
    
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x

def checkEditTime(times, day, id):
    
    x = []
    appointment = Appointment.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x
