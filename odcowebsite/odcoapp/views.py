from django.http import HttpResponse
from django.shortcuts import render
from odcoapp.models import Video,Photo,Audio,Doc,Acctualite,Secteur,Type,pre_post,Assistance,Programme

# Create your views here.
def Index(request):
    img = Photo.objects.all()[:4]
    prog = Programme.objects.all()[:2]
    return render(request,'index.html', {"img": img, "prog": prog})
def IndexAR(request):
    return render(request,'indexAR.html')
def Acctu(request):
    return render(request,'acctualite.html')
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
def Contact(request):
    return render(request,'contact.html')
def ContactAR(request):
    return render(request,'contactAR.html')
