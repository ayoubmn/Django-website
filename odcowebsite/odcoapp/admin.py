from django.contrib import admin


# Register your models here.
from odcoapp.models import Video,Photo,Audio,Doc,Acctualite,Secteur,Type,pre_post,Assistance


admin.site.register(Video)
admin.site.register(Photo)
admin.site.register(Audio)
admin.site.register(Doc)
admin.site.register(Acctualite)
admin.site.register(Secteur)
admin.site.register(Type)
admin.site.register(pre_post)
admin.site.register(Assistance)