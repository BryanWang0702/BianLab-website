from django.shortcuts import render

from GalleryApp.models import GalleryLife, GalleryExperiment


# Create your views here.


def galleryLife(request):
    gallery = GalleryLife.objects.all().order_by('-time')
    context = {
        'gallery': gallery,
        'field': 'life'
    }
    return render(request, 'gallery/gallery.html', context)


def galleryExperiment(request):
    gallery = GalleryExperiment.objects.all().order_by('-time')
    context = {
        'gallery': gallery,
        'field': 'experiment'
    }
    return render(request, 'gallery/gallery.html', context)
