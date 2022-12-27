from django.urls import path, include
from watchlist_app.api.views import StreamlistAV, WatchlistAV, WatchDetailAV ,StreamDetailAV , ReviewList ,ReviewDetail , ReviewCreate


urlpatterns = [
    path('list/', WatchlistAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-details'),
    
    path('stream/', StreamlistAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name='stream-details'),
    
    # path('review', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-list'),
    
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'), # i need all the reviews for this particular movie
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'), # i need all the reviews for this particular movie
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-list'),
    
]
