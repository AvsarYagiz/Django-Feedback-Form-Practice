from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()), # we update this part because we change our view from function based to class based 
    path('thank-you', views.ThankYouView.as_view()),
    path('reviews', views.ReviewsListView.as_view()),
    path('reviews/favorite', views.AddFavoriteView.as_view()),
    path('reviews/<int:pk>', views.SingleReviewView.as_view())
]
