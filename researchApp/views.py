from django.shortcuts import render

from researchApp.models import Research


# Create your views here.


def research(request):
    research = Research.objects.all()
    context = {
        'research': research
    }

    return render(request, 'research/research.html', context)
