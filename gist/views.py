from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Gist

def index(request):
    latest_gists = Gist.objects.order_by('-pub_date')[:5]
    context = {'latest_gists_list': latest_gists,}
    return render(request, 'gist/index.html', context)

# def detail(request, gist_id):
#     return HttpResponse("You're looking at gist with ID= %s." % gist_id)

def detail(request, gist_id):
    gist = get_object_or_404(Gist, pk=gist_id)
    return render(request, 'gist/detail.html', {'gist': gist})
