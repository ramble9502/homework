from django.contrib import admin

# Register your models here
from one.models import *



class Testoption(admin.TabularInline):
	model=Testoption

class Test_Class(admin.ModelAdmin):
	inlines=[Testoption,]
		


		

admin.site.register(StoryOfBartender)
admin.site.register(BrewWine)
admin.site.register(Lmessage)
admin.site.register(Divescore)
admin.site.register(Test,Test_Class)
admin.site.register(Testscore)
admin.site.register(UserProfile)

