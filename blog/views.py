from django.shortcuts import render
from .models import Question,Choice,directions_dict
from django.utils import timezone

def index(request):
    for item in sorted(directions_dict.keys()):
        q = Question(q_text=item[1:])
        q.save()
        print q.id
        for x in directions_dict[item]:
            q.choice_set.create(choice_text=x[0],q_link=x[1])
    question = Question.objects.get(id=1)
    return render(request,"blog/post_list.html",context={"quest":question,"ans":question.choice_set.all()})

def detail(request,question_id):
    question = Question.objects.get(pk=question_id)
    if int(question_id) != 26:
        return render(request,"blog/post_list.html",context={"quest":question,"ans":question.choice_set.all()})
    else:
        return render(request,"blog/second_to_last.html")

def final(request):
    return render(request,"blog/final.html")
