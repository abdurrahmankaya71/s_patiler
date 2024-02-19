from django.shortcuts import render
from django.http import HttpResponseRedirect
from form.models import ContactFormModel
# Create your views here.


def form(request):

    context = dict()
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone_num = request.POST.get('phone_num')
        obj = ContactFormModel(user_name=user_name, email=email,
                               message=message, phone_num=phone_num)
        obj.save()
        if obj:
            HttpResponseRedirect(url)

    return render(request, 'partials/contact.html', context)
