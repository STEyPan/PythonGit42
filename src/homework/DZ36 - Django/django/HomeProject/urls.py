from django.urls import path
import sites.views as view

urlpatterns = [
    path("", view.index),
]
