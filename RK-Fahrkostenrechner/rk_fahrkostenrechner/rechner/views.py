from django.shortcuts import render
from .models import Kosten, MapBox


# Create your views here.

def rechner(request):

    price_object = Kosten.objects.first()
    # print(price_object)

    api_object = MapBox.objects.first()

    return render(request, "rechner/rechner.html", { 'price':price_object, 'mapbox':api_object })