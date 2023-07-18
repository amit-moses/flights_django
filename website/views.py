from django.http import HttpResponse
from django.shortcuts import redirect, render

from website.models import Flight

def flightlist(request):
    context = {'flights': Flight.objects.all()}
    return render(request, 'temp.html', context)
    # return HttpResponse('<br>'.join(fl))

def buy_ticket(request, flight_id):
    fl = Flight.objects.filter(pk = flight_id)
    if fl:
        fl[0].tickets -= int(request.POST.get("tickets", 0))
        fl[0].save()
    return redirect('flightlist')
    
    
