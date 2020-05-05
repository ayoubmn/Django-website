"""odcowebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from odcoapp.views import Index,IndexAR,Acctualite,AcctualiteAR,ConseilEco,ConseilEcoAR,ConseilJuri,ConseilJuriAR,Assistance,AssistanceAR,Pre,PreAR,Post,PostAR,faq,faqAR,Contact,ContactAR

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',Index,name="first"),
    path(r'/', Index, name="Index"),
    path(r'ar', IndexAR, name="indexAR"),
    path(r'acctualite', Acctualite, name="Acctualite"),
    path(r'acctualitear', AcctualiteAR, name="AcctualiteAR"),
    path(r'conseileco', ConseilEco, name="ConseilEco"),
    path(r'conseilecoar', ConseilEcoAR, name="ConseilEcoAR"),
    path(r'conseiljuri', ConseilJuri, name="ConseilJuri"),
    path(r'conseiljuriar', ConseilJuriAR, name="ConseilJuriAR"),
    path(r'assistance', Assistance, name="Assistance"),
    path(r'assistancear', AssistanceAR, name="AssistanceAR"),
    path(r'pre', Pre, name="Pre"),
    path(r'prear', PreAR, name="PreAR"),
    path(r'post', Post, name="Post"),
    path(r'postar', PostAR, name="PostAR"),
    path(r'faq', faq, name="faq"),
    path(r'faqar', faqAR, name="faqAR"),
    path(r'contact', Contact, name="Contact"),
    path(r'contactar', ContactAR, name="ContactAR"),

]
