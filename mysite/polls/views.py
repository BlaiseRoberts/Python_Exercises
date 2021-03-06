from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question {}.".format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question {}.".format(question_id)
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("You're voting on question {}.".format(question_id))
