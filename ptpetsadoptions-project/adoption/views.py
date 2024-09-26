from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello It\'s a test</h1>')
def pet_detail(request, pet_id):
    return HttpResponse(f'<p>pet_detail view with pet_id {pet_id}</p>')