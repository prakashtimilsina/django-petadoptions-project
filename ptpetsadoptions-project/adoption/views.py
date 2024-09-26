from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Pet

def home(request):
    pets = Pet.objects.all()

    return render(request, 'home.html', {'pets': pets})

    #return HttpResponse('<h1>Hello It\'s a test</h1>')
def pet_detail(request, pet_id):
    try:    
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404("Pet is not found")
    return render(request, 'pet_detail.html', {'pet': pet})

    #return HttpResponse(f'<p>pet_detail view with pet_id {pet_id}</p>')