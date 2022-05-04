from django.urls import path

from pages.views import InfoPageView

url_patterns = [
    path('info', InfoPageView.as_view())]
