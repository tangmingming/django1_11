from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from .views import *

app_name = "c_test"

urlpatterns = [
    url(r'^index$', TemplateView.as_view(template_name="m_test/index.html"), name="index"),
    url(r'^index_2$', RedirectView.as_view(url="https://www.baidu.com"), name="index_2"),
    url(r'^index_3$', Index_3.as_view(), name="index_3"),
    url(r'^book_list$', BookList.as_view(), name="book_list"),
    url(r'^index_4', Index_4.as_view(), name="index_4"),
    url(r'^index_5', Index_5.as_view(), name="index_5"),
    url(r'^index_6', Index_5.as_view(greeting="index_6"), name="index_6"),
]