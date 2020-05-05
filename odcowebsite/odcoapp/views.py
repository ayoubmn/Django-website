from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,'index.html')
def IndexAR(request):
    return render(request,'indexAR.html')
def Acctualite(request):
    return render(request,'acctualite.html')
def AcctualiteAR(request):
    return render(request,'acctualiteAR.html')
def faq(request):
    return render(request,'faq.html')
def faqAR(request):
    return render(request,'faqAR.html')
def ConseilEco(request):
    return render(request,'conseileco.html')
def ConseilEcoAR(request):
    return render(request,'conseilecoAR.html')
def ConseilJuri(request):
    return render(request,'conseiljuri.html')
def ConseilJuriAR(request):
    return render(request,'conseiljuriAR.html')
def Assistance(request):
    return render(request,'assistance.html')
def AssistanceAR(request):
    return render(request,'assistanceAR.html')
def Pre(request):
    return render(request,'pre.html')
def PreAR(request):
    return render(request,'preAR.html')
def Post(request):
    return render(request,'post.html')
def PostAR(request):
    return render(request,'postAR.html')
def Contact(request):
    return render(request,'contact.html')
def ContactAR(request):
    return render(request,'contactAR.html')
