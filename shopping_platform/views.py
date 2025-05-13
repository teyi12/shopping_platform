from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Startseite
def home_view(request):
    
    # popular_products = Product.objects.filter(is_popular=True)[:6]  # Beispiel: Beliebte Produkte
    return render(request, 'home.html')



# About Us / Impressum
def about_view(request):
    return render(request, 'about.html')

# Contact View
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        # Formulardaten abrufen
        name = request.POST.get('Ihr Name')
        email = request.POST.get('Ihre E-Mail-Adresse')
        subject = request.POST.get('subject')
        message = request.POST.get('Nachricht')

        if not (name and email and subject and message):
            messages.error(request, "Alle Felder müssen ausgefüllt werden.")
            return render(request, 'contact.html')
        print(name)

        # E-Mail vorbereiten
        full_message = f"Nachricht von {name} ({email}):\n\n{message}"
        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL, "teyi9lawson9@gmail.com", # Ihre Absenderadresse
                [settings.CONTACT_EMAIL], "teyi9lawson9@gmail.com",  # Zieladresse (z. B. Support-Adresse),
                fail_silently=False,
            )
            messages.success(request, "Ihre Nachricht wurde erfolgreich gesendet.")
        except Exception as e:
            messages.error(request, f"Fehler beim Senden der Nachricht: {e}")

    return render(request, 'contact.html')


# Bedanken View
def danken_view(request):
    
    return HttpResponse("Danke")












