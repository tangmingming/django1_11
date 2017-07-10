from django.conf.urls import url

from . import views

app_name = "polls"

url_patterns = [
    url(r'^index$', views.Index.as_view()),
]