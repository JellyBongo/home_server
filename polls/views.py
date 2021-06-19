from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_questions,
    }

    # Or this could be written using a shortcut from django.shortcuts.render:
    # return render(request=request, template_name='polls/index.html', context=context)
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    # Or it could be rewritten with a shortcut:
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})
    context = {
        'question': question,
    }
    return render(request=request, template_name='polls/detail.html', context=context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
