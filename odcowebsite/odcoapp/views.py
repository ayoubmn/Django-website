from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json
from .forms import Cont
from django.core.mail import send_mail
from odcowebsite.settings import EMAIL_HOST_USER
from .models import Video,faq, Photo, Audio, Doc, Acctualite, Secteur, Type, pre_post, Assistance, Programme,adresses
from django import forms


# Create your views here.

def Faq(request):
    q = faq.objects.filter(langue="fr")
    return render(request, 'faq.html',{"faq": q})


def faqAR(request):
    q = faq.objects.filter(langue="ar")
    return render(request, 'faqAR.html', {"faq": q})

def Index(request):
    img = Photo.objects.all()[:4]
    prog = Programme.objects.all()[:3]
    acct = Acctualite.objects.filter(langue="fr")[:3]
    video = Video.objects.all()[:6]
    return render(request, 'index.html', {"img": img, "prog": prog, "acct": acct, "video": video})


def IndexAR(request):
    img = Photo.objects.all()[:4]
    prog = Programme.objects.all()[:3]
    acct = Acctualite.objects.filter(langue="ar")[:3]
    video = Video.objects.all()[:6]
    return render(request, 'indexAR.html', {"img": img, "prog": prog, "acct": acct, "video": video})


def Acctu(request):
    acct = Acctualite.objects.filter(langue="fr")
    return render(request, 'acctualite.html', {"acct": acct})


def AcctualiteAR(request):
    acct = Acctualite.objects.filter(langue="ar")
    return render(request, 'acctualiteAR.html', {"acct": acct})

def ConseilEco(request):
    video = Video.objects.filter(type__namefr="economique")
    doc = Doc.objects.filter(type__namefr="economique")
    return render(request, 'conseileco.html', {"video": video, "doc": doc})


def ConseilEcoAR(request):
    video = Video.objects.filter(type__namefr="economique")
    doc = Doc.objects.filter(type__namefr="economique")
    return render(request, 'conseilecoAR.html', {"video": video, "doc": doc})


def ConseilJuri(request):
    video = Video.objects.filter(type__namefr="juridique")
    doc = Doc.objects.filter(type__namefr="juridique")
    return render(request, 'conseiljuri.html', {"video": video, "doc": doc})


def ConseilJuriAR(request):
    video = Video.objects.filter(type__namefr="juridique")
    doc = Doc.objects.filter(type__namefr="juridique")
    return render(request, 'conseiljuriAR.html', {"video": video, "doc": doc})


def Assist(request):
    return render(request, 'assistance.html')


def AssistanceAR(request):
    return render(request, 'assistanceAR.html')


def Pre(request):
    video = Video.objects.filter(pre_post__namefr="pre_creation")
    pre = Assistance.objects.filter(pre_post__namefr="pre_creation")
    sect = Secteur.objects.all()
    doc = Doc.objects.filter(pre_post__namefr="pre_creation")
    audio = Audio.objects.filter(pre_post__namefr="pre_creation",langue="fr")
    return render(request, 'pre.html', {"pre": pre, "sect": sect, "video": video, "doc": doc, "audio": audio})


def PreAR(request):
    video = Video.objects.filter(pre_post__namefr="pre_creation")
    pre = Assistance.objects.filter(pre_post__namefr="pre_creation")
    sect = Secteur.objects.all()
    doc = Doc.objects.filter(pre_post__namefr="pre_creation")
    audio = Audio.objects.filter(pre_post__namefr="pre_creation",langue="ar")

    return render(request, 'preAR.html', {"pre": pre, "sect": sect, "video": video, "doc": doc, "audio": audio})


def Post(request):
    video = Video.objects.filter(pre_post__namefr="post_creation")
    post = Assistance.objects.filter(pre_post__namefr="post_creation")
    sect = Secteur.objects.all()
    doc = Doc.objects.filter(pre_post__namefr="post_creation")
    audio = Audio.objects.filter(pre_post__namefr="post_creation", langue="fr")

    return render(request, 'post.html', {"post": post, "sect": sect, "video": video, "doc": doc, "audio": audio})


def PostAR(request):
    video = Video.objects.filter(pre_post__namefr="post_creation")
    post = Assistance.objects.filter(pre_post__namefr="post_creation")
    sect = Secteur.objects.all()
    doc = Doc.objects.filter(pre_post__namefr="post_creation")
    audio = Audio.objects.filter(pre_post__namefr="post_creation", langue="ar")

    return render(request, 'postAR.html', {"post": post, "sect": sect, "video": video, "doc": doc, "audio": audio})


def ContactAR(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Cont(request.POST)
        # check whether it's valid:
        if form.is_valid():
            canPost = False
            # if this is the first time the client will post smth
            if 'numberOfSubmits' not in request.session:
                # set session to expire after 2 hours
                request.session.set_expiry(7200)
                request.session['numberOfSubmits'] = 1
                canPost = True

            # if session expired
            elif request.session.get_expiry_age() <= 0:
                canPost = True
                # set new session
                request.session.set_expiry(7200)
                request.session['numberOfSubmits'] = 1

                # if client didnt reach maximum amount of submits (3 each 2 hours for our case)
            elif request.session['numberOfSubmits'] < 3:
                request.session['numberOfSubmits'] += 1
                canPost = True

            # else the client cant submit

            if canPost:
                nom = form.cleaned_data['nom']
                email = form.cleaned_data['email']
                sujet = form.cleaned_data['sujet']
                msg = form.cleaned_data['msg']
                form.save()

                return HttpResponseRedirect('/contactar')

            # else should send a message to the client to inform him that he must wait

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Cont()
    adresse = adresses.objects.filter(langue="ar")
    return render(request, 'contactAR.html', {'form': form, "adresse":adresse})


def Contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Cont(request.POST)
        # check whether it's valid:
        if form.is_valid():
            canPost = False
            # if this is the first time the client will post smth
            if 'numberOfSubmits' not in request.session:
                # set session to expire after 2 hours
                request.session.set_expiry(7200)
                request.session['numberOfSubmits'] = 1
                canPost = True

            # if session expired
            elif request.session.get_expiry_age() <= 0:
                canPost = True
                # set new session
                request.session.set_expiry(7200)
                request.session['numberOfSubmits'] = 1

                # if client didnt reach maximum amount of submits (3 each 2 hours for our case)
            elif request.session['numberOfSubmits'] < 3:
                request.session['numberOfSubmits'] += 1
                canPost = True

            # else the client cant submit

            if canPost:
                nom = form.cleaned_data['nom']
                email = form.cleaned_data['email']
                sujet = form.cleaned_data['sujet']
                msg = form.cleaned_data['msg']
                form.save()
                send_mail(sujet,msg, EMAIL_HOST_USER,[str(email)], fail_silently=False)

                return HttpResponseRedirect('/contact')

            # else should send a message to the client to inform him that he must wait

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Cont()
    adresse = adresses.objects.filter(langue="fr")
    return render(request, 'contact.html', {'form': form, "adresse":adresse})


def AcctuSpe(request):
    acct = Acctualite.objects.filter(secteur__namefr=request.GET.get('secteur', 'Generale'),langue="fr")
    photo = Photo.objects.filter(secteur__namefr=request.GET.get('secteur', 'Generale'))
    video = Video.objects.filter(secteur__namefr=request.GET.get('secteur', 'Generale'))
    doc = Doc.objects.filter(secteur__namefr=request.GET.get('secteur', 'Generale'),langue="fr")
    audio = Audio.objects.filter(secteur__namefr=request.GET.get('secteur', 'Generale'),langue="fr")
    return render(request, 'acctuspe.html', {"acct": acct, "photo": photo, "video": video, "doc": doc, "audio":audio})


def AcctuSpeAR(request):
    acct = Acctualite.objects.filter(secteur__namefr=request.GET.get('secteur', 'Generale'),langue="ar")
    photo = Photo.objects.filter(secteur__namefr=request.GET.get('secteur', 'Generale'))
    video = Video.objects.filter(secteur__namefr=request.GET.get('secteur', 'Generale'))
    doc = Doc.objects.filter(secteur__namefr=request.GET.get('secteur', 'Generale'),langue="ar")
    audio = Audio.objects.filter(secteur__namefr=request.GET.get('secteur', 'Generale'),langue="ar")
    return render(request, 'acctuspeAR.html', {"acct": acct, "photo": photo, "video": video, "doc": doc, "audio":audio})




def Lactu(request):
    actu = Acctualite.objects.filter(titre=request.GET.get('id', 'id'),langue="fr")
    return render(request, 'lactu.html', {"actu": actu})

def LactuAR(request):
    actu = Acctualite.objects.filter(titre=request.GET.get('id', 'id'),langue="ar")
    return render(request, 'lactuAR.html', {"actu": actu})


def Search(request):
    acct = Acctualite.objects.filter(titre__contains=request.GET.get('objet', 'a'))
    return render(request, 'search.html', {"acct": acct})

