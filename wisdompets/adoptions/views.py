# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pet


def home(request):

    # using HttpResponse
    # return HttpResponse('<p>home view</p>')

    # using render()
    pets = Pet.objects.all()
    return render(request, 'index_ori.html', {'pets': pets, })


def pet_detail(request, pet_id):

    # using HttpResponse
    # return HttpResponse(f'<p>pet_detail view with id {pet_id}</p>')

    # using render()
    try:
        pet = Pet.objects.get(id=pet_id)

    except Pet.DoesNotExist:
        raise Http404('pet not found')

    return render(request, 'pet_detail.html', {'pet': pet, })



