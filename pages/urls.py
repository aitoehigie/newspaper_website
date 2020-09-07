from django.urls import path, reverse_lazy
from . import views


urlpatterns = [
	path("", views.HomePageView.as_view(), name = "home"),
]
