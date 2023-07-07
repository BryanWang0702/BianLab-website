from django.shortcuts import render

from teamApp.models import Team


# Create your views here.

def team(request):
    team = Team.objects.all().order_by('-positionType')
    context = {
        'team': team
    }
    return render(request, 'team/team.html', context)


def member(request):
    name = request.GET.get('name')
    member = [each for each in Team.objects.filter(name__contains=name)][0]

    context = {
        'member': member
    }
    return render(request, 'team/member.html', context)
