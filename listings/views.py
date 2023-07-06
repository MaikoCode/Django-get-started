from django.shortcuts import render
from django.http import HttpResponse, Http404
from listings.models import Band
from listings.forms import ContactUsForm, BandForm
from django.shortcuts import redirect
from django.core.mail import send_mail



def welcome(request):
    return HttpResponse('<h1>Welcome Master</h1>')

def contact(request):
    
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            
           send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
        return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})


def email_sent(request):
    return render(request, 'listings/email_sent.html')



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
    
def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
        return render(request, 'listings/band_creation.html', {'form': form})
    
def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band) # Il contient une instande de la donnée qu'on a deja dans notre base de donnée
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                'listings/band_update.html',
                {'form': form})
    



    
    




# Voici votre liste de tâches pour ce chapitre :

# ajouter une page « Create new Listing » (modèle d'URL, vue et gabarit) ;

# ajouter un ListingForm et l’utiliser dans la nouvelle page pour créer des objets Listing ;

# lier la liste des annonces à la page de création d'une annonce ;

# réactiver la validation côté client pour tous vos formulaires.