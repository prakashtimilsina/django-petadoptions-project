from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Pet
from .forms import NameForm
from django.core.mail import send_mail


def get_name(request):
    # if this is POST request, we need to process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = NameForm(request.POST)

        #Check whether form is valid.
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            # process the data in form.cleaned_data as required
            # ...
            # Redirect to a new URL.
            recipients = ["prakashchitwan38@gmail.com"]
            if cc_myself:
                recipients.append(sender)
            # send_mail(subject, message, sender, recipients)
            print(f'{subject}, {message}, {sender}, {cc_myself}, {recipients}')
            return HttpResponse(f'<h1>The email is sent to </h1>')
    #if a GET (or any other method),  we will create a blank form
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})
    # return render(request, 'form_test.html', {'current_name': 'Prakash Timilsina'})
    

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