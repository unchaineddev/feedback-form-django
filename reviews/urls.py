from django.urls import path

from . import views 

urlpatterns = [
    path("", views.ReviewView.as_view()),
    # path("", views.reviews),
    # path("thank-you", views.thank_you)
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewListView.as_view()),
    path("reviews/<int:pk>", views.ReviewTextView.as_view())
]