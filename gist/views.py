from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Gist
from .forms import GistForm

def all(request):
    latest_gists = Gist.objects.order_by('-pub_date')[:5]
    context = {'latest_gists_list': latest_gists,}
    return render(request, 'gist/all.html', context)

def detail(request, gist_id):
    gist = get_object_or_404(Gist, pk=gist_id)
    return render(request, 'gist/detail.html', {'gist': gist})

def new_gist(request):
    if request.method == "POST":
        form = GistForm(request.POST)
        if form.is_valid():
            gist = form.save(commit=False)
            gist.pub_date = timezone.now()
            gist.save()
            return redirect('gist:all')
        
    else:
        form = GistForm()
    return render(request, 'gist/new_gist.html', {'form': form})
    # return render(request, 'gist/new_gist.html')


# def create(request):
#     return render(request, 'gist/new_gist.html')

# def post_new(request):


# def create(request):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
