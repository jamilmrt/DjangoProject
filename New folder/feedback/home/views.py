from django.shortcuts import render
from .models import *




# Create your views here.
def index(request):
    feedbacks = CustomerFeedback.objects.all().order_by('-timestamp')

    return render(request,'survey.html', {'feedbacks': feedbacks})


def customer_feedback(request, id):
    feedbacks = CustomerFeedback.objects.get(id=id)
    return render(request, 'surveys.html', {'questions': feedbacks.question.all()})
    