from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()), # we update this part because we change our view from function based to class based 
    path('thank_you', views.thank_you)
]
