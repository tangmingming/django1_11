from django.conf.urls import url
from django.views.generic import TemplateView

app_name = "c_test"

urlpatterns = [
    url(r'^index$', TemplateView.as_view(template_name="index.html")),
]