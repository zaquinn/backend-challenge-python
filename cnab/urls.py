from django.urls import path

from .views import CnabView

urlpatterns = [
    path("cnabparser/", CnabView.as_view()),
]