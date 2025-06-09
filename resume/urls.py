from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.home, name='home'),
   path('about',views.about, name='about'),
   path('projects',views.projects, name='projects'),
   path('experience',views.experience, name='experience'),
   path('certifications',views.certifications, name='cert'),
   path('contact',views.contacts, name='contact'),
   path('Resume',views.resume, name='resume'),
   path('cert/<str:pk>',views.certificate, name='cert'),
]