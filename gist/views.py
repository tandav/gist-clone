from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Gist

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

def index(request):
    latest_gists = Gist.objects.order_by('-pub_date')[:5]
    template = loader.get_template('gist/index.html')
    context = {'latest_gists_list': latest_gists,}
    return HttpResponse(template.render(context, request))

def detail(request, gist_id):
    return HttpResponse("You're looking at gist with ID= %s." % gist_id)
