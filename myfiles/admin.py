from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','name','company_name','link','deadline','type','description','picture1','picture2','picture3','date']

admin.site.register(Portfolio,AdminPortfolio)

class AdminType(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Type,AdminType)

class AdminServices(admin.ModelAdmin):
    list_display = ['id','name','description','picture','date']

admin.site.register(Services,AdminServices)

class AdminTeam(admin.ModelAdmin):
    list_display = ['id','name','lavozim','link1','link2','link3','link4','picture','date','description']

admin.site.register(Team,AdminTeam)

class AdminMalumot_saqlash(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message','date']

admin.site.register(Malumot_saqlash,AdminMalumot_saqlash)

class AdminSubject(admin.ModelAdmin):
    list_display = ['id','email','date']

admin.site.register(Subject,AdminSubject)

class AdminSubj(admin.ModelAdmin):
    list_display = ['id','email','date']

admin.site.register(Subj,AdminSubj)

class AdminAli(admin.ModelAdmin):
    list_display = ['id','email','date']

admin.site.register(Ali,AdminAli)