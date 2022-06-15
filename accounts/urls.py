from django.urls import path
from . import views as vs

urlpatterns = [
    path('register/', vs.SignUp.as_view(), name='signup'),
]
