from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import AccountHeads
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    heads=AccountHeads.objects.all()
    return render(request,'base.html')
@login_required
def head_detail(request,head_id):
    try:
        head=AccountHeads.objects.get(id=head_id)
    except AccountHeads.DoesNotExist:
        raise Http404("Path not found")
    return render(request,"Head_Detail.html",{'head':head})