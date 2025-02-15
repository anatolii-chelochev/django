
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("prince", views.prince, name="prince"),
    path("<str:name>", views.greet, name="greet")

]