from django.urls import path

from . import views 

urlpatterns = [
    path("", views.ReviewView.as_view()),
    # path("", views.reviews),
    path("thank-you", views.thank_you)
]