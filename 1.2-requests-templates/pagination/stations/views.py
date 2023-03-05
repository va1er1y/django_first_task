from django.shortcuts import render, redirect
from django.urls import reverse
import  csv
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import  Paginator

def index(request):
    return redirect(reverse('bus_stations'))

txt = list()
with open(BUS_STATION_CSV, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        txt.append(row)

def bus_stations(request):
    page_namber = int(request.GET.get("page", 1))
    paginator = Paginator(txt, 10)
    page = paginator.get_page(page_namber)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
