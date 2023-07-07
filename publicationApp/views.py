from django.shortcuts import render

from publicationApp.models import Publication


# Create your views here.


def publication(request):
    publication = Publication.objects.all().order_by('-year')
    context = {
        'publication': publication
    }
    return render(request, 'publication/publication.html', context)
