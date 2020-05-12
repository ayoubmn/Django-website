from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json

from .models import Video,Photo,Audio,Doc,Acctualite,Secteur,Type,pre_post,Assistance,Programme
from django import forms
# Create your views here.
def Index(request):
    img = Photo.objects.all()[:4]
    prog = Programme.objects.all()[:3]
    acct = Acctualite.objects.all()[:3]

    return render(request,'index.html', {"img": img, "prog": prog, "acct": acct})
def IndexAR(request):
    return render(request,'indexAR.html')
def Acctu(request):

    acct = Acctualite.objects.all()
    return render(request,'acctualite.html',{"acct":acct})
def AcctualiteAR(request):
    return render(request,'acctualiteAR.html')
def faq(request):
    return render(request,'faq.html')
def faqAR(request):
    return render(request,'faqAR.html')

def ConseilEco(request):


    video = Video.objects.filter(type__name="economique")
    doc = Doc.objects.filter(type__name="economique")
    return render(request,'conseileco.html', {"video": video, "doc": doc})

def ConseilEcoAR(request):
    video = Video.objects.filter(type__name="economique")
    doc = Doc.objects.filter(type__name="economique")
    return render(request,'conseilecoAR.html',{"video": video, "doc": doc})

def ConseilJuri(request):



    video = Video.objects.filter(type__name="juridique")
    doc = Doc.objects.filter(type__name="juridique")
    return render(request,'conseiljuri.html',{"video": video, "doc": doc})

def ConseilJuriAR(request):
    video = Video.objects.filter(type__name="juridique")
    doc = Doc.objects.filter(type__name="juridique")
    return render(request,'conseiljuriAR.html',{"video": video, "doc": doc})

def Assist(request):




    return render(request,'assistance.html')

def AssistanceAR(request):
    return render(request,'assistanceAR.html')

def Pre(request):




    pre = Assistance.objects.filter(pre_post__name="pre_creation")
    sect = Secteur.objects.all()
    return render(request,'pre.html',{"pre": pre, "sect": sect})

def PreAR(request):
    return render(request,'preAR.html')
def Post(request):



    post = Assistance.objects.filter(pre_post__name="post_creation")
    sect = Secteur.objects.all()
    return render(request,'post.html',{"post": post, "sect": sect})
def PostAR(request):
    return render(request,'postAR.html')
def ContactAR(request):
    return render(request,'contactAR.html')

from .forms import Cont

def Contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Cont(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            nom= form.cleaned_data['nom']
            email= form.cleaned_data['email']
            sujet= form.cleaned_data['sujet']
            msg= form.cleaned_data['msg']
            form.save()
            return HttpResponseRedirect('/contact')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Cont()

    return render(request, 'contact.html', {'form': form})


def AcctuSpe(request):
    acct = Acctualite.objects.filter(secteur__name=request.GET.get('secteur', 'Generale'))
    photo = Photo.objects.filter(secteur__name=request.GET.get('secteur', 'Generale'))
    video = Video.objects.filter(secteur__name=request.GET.get('secteur', 'Generale'))
    doc = Doc.objects.filter(secteur__name=request.GET.get('secteur', 'Generale'))

    return render(request,'acctuspe.html',{"acct": acct, "photo": photo, "video": video, "doc":doc})

def Lactu(request):

    actu = Acctualite.objects.filter(titre=request.GET.get('id', 'id'))

    return render(request,'lactu.html',{"actu":actu})

def Search(request):

    acct = Acctualite.objects.filter(titre__contains=request.GET.get('objet','a'))
    print(acct)
    return render(request,'search.html',{"acct": acct})