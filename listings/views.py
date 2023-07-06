from django.shortcuts import render
from django.http import HttpResponse, Http404
from listings.models import Band
from listings.forms import ContactUsForm



def welcome(request):
    return HttpResponse('<h1>Welcome Master</h1>')

def contact(request):
    form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})

def band_list(request):
    band = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': band})

def band_detail(request, id):
    try:
        band = Band.objects.get(id = id) # On va recuperer la donnée correspondant a id
        # band = get_object_or_404(Band, id=id)
        return render(request, 'listings/band_detail.html', {'band': band})
        # Le probleme ici c'est que l'expcetion n'est pas levé
    except Band.DoesNotExist:
        return render(request, 'listings/404.html')
        


    
    




