
from django.urls import path
from . import views  # ayni projede oldugum icin . import yaptim


urlpatterns = [
    # path('', views.index, name='index'),
    # path (rout, view, opt(kisayo ismi))
    # path (yon, ilgili view fonksiyonu, opsiyonel olarak kisa isim)
    path('', views.form, name='contact'),
    #     path('contact/', views.contact, name = 'contact'),
    #     path('services/', views.services, name = 'services'),
    #     path('booking/', views.booking, name = 'booking'),
]
