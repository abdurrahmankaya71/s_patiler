from django.shortcuts import render
from .models import Shop

# Create your views here.
def shop(request):
    # tum shop urunlerini shops adi altinda topladim
    shops = Shop.objects.all()

    # simdi bu tum shop urunlerini context_shop adli bir dictionary'de yerlestirecem
    context_shop = {
        'shops': shops
    }
    
    return render(request, 'partials/gallery.html', context_shop)