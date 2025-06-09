from django.contrib import admin
from .models import ProfileInfo,TechStack,Projects,Experience,Ceritifications,Resume
# Register your models here.
# username: ramsy
# password: ramsy

admin.site.register(ProfileInfo)
admin.site.register(TechStack)
admin.site.register(Projects)
admin.site.register(Experience)
admin.site.register(Ceritifications)
admin.site.register(Resume)