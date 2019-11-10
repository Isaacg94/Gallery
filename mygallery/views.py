from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from models import Image

# Create your views here.
def gallery(request):
    images = Image.get_all_images()
    return render(request, 'gallery.html', {"images":images})


