from django.contrib import admin


# Register your models here.
from .models import Video,Photo,Audio,Doc,Acctualite,Secteur,Type,pre_post,Assistance,Programme,ContactReception,faq,adresses

class AdminVideo(admin.ModelAdmin):
    model = Video
    list_display = ('name', 'date_of', 'secteur','langue')
admin.site.register(Video,AdminVideo)

class AdminPhoto(admin.ModelAdmin):
    model = Photo
    list_display = ('name', 'date_of', 'secteur')
admin.site.register(Photo,AdminPhoto)

class AdminAudio(admin.ModelAdmin):
    model = Audio
    list_display = ('name', 'date_of', 'secteur','langue')
admin.site.register(Audio,AdminAudio)

class AdminDoc(admin.ModelAdmin):
    model = Doc
    list_display = ('name', 'date_of', 'secteur','langue')
admin.site.register(Doc,AdminDoc)

class AdminAcctualite(admin.ModelAdmin):
    model = Acctualite
    list_display = ('titre', 'date_of', 'secteur','langue')
admin.site.register(Acctualite,AdminAcctualite)



class AdminAssistance(admin.ModelAdmin):
    model = Assistance
    list_display = ('titre', 'date_of', 'secteur','pre_post','langue')
admin.site.register(Assistance,AdminAssistance)

class AdminProgramme(admin.ModelAdmin):
    model = Programme
    list_display = ('titre', 'date', 'langue')
admin.site.register(Programme,AdminProgramme)

class AdminContactReception(admin.ModelAdmin):
    model = ContactReception
    list_display = ('nom', 'email', 'date_of')
admin.site.register(ContactReception,AdminContactReception)


class Adminfaq(admin.ModelAdmin):
    model = faq
    list_display = ('question', 'langue')
admin.site.register(faq,Adminfaq)



class Adminadresses(admin.ModelAdmin):
    model = adresses
    list_display = ('delegation', 'langue')
admin.site.register(adresses,Adminadresses)


admin.site.register(Secteur)

admin.site.register(Type)


admin.site.register(pre_post)
