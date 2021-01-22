from django.shortcuts import render, HttpResponse
from .forms import ContactForm

def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'index.html', context)
