from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models
from django.http import HttpResponse
from .import forms
from . import models
# Create your views here.
def home(request):
    return render(request,'home.html')

    # category=QuizCategory.objects.all()
    # return render(request,'home.html',{'category':category})
def register(request):
    msg=None
    form=forms.RegisterUser
    if request.method=="POST":
        form=forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg='Data added'
    return render(request,'registration/register.html',{'form':form,msg:'msg'})

def all_categories(request):
    catData=models.QuizCategory.objects.all()
    return render(request,'all-category.html',{'data':catData})
@login_required
def category_questions(request, cat_id):
    category=models.QuizCategory.objects.get(id=cat_id)
    question=models.QuizQuestions.objects.filter(category=category).order_by('id').first()
    return render(request,'category-questions.html',{'question':question,'category':category})

@login_required
def submit_answer(request,cat_id,quest_id):
    if request.method=='POST':
        if 'skip' in request.POST:
            return HttpResponse("Skip is Clicked")
        category=models.QuizCategory.objects.get(id=cat_id)
        question=models.QuizQuestions.objects.filter(category=category,id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
        if question:     
            return render(request,'category-questions.html',{'question':question,'category':category})
            return HttpResponse("There is question")
        else:
            return HttpResponse("No More Questions !!")
    else:
        return HttpResponse("Method is not post")

