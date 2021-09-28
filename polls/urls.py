from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'polls'
urlpatterns = [
        path('', TemplateView.as_view(template_name='polls/main.html')),
        path("some", views.some, name="some"),
        path("remain/<slug:guess>", views.RestMainView.as_view()),
        path("remain2", views.RestMainView2.as_view(), name="remain2"),
        ]
