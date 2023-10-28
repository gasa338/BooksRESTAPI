from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
# router.register('rating', BookRateViewSet)
router.register('reserve', ReservationViewSet)

urlpatterns = [
    path('genre_list', GenreViewListAPI.as_view(), name="genre_list"),
    path('genre_post', GenreViewCreateAPI.as_view(), name="genre_post"),
    path('genre/<int:id>', GenreViewRUDAPI.as_view(), name="genre"),

    path('writer_list', WriterViewListAPI.as_view(), name="writer_list"),
    path('writer_post', WriterViewCreateAPI.as_view(), name="writer_post"),
    path('writer/<int:id>', WriterViewRUDAPI.as_view(), name="writer"),

    path('publishers', PublisherViewAPIView.as_view(), name="publishers"),
    path('publisher/<int:id>', PublisherRUDViewSet.as_view(), name="publisher"),

    path('book_list', BookListAPIView.as_view(), name="book_list"),
    path('book_create', BookCreateAPIView.as_view(), name="book_create"),
    path('book/<int:id>', BookRUDView.as_view(), name="book"),

    path('review_create/', BookReviewViewAPICreate.as_view(), name="review_create"),
    path('review_update/<int:id>', BookReviewViewAPIUpdate.as_view(), name="review_update"),
    path('review_delete/<int:id>', BookReviewViewAPIDelete.as_view(), name="review_delete"),
    path('review_list/<int:id>', BookReviewViewAPIList.as_view(), name="review_list"),
    path('review_lists', BookReviewViewAPILists.as_view(), name="review_lists"),
    path('review_by_book/<int:id>', BookReviewViewAPIListByBook.as_view(), name="review_by_book"),
    path('review_by_user/<int:id>', BookReviewViewAPIListByUser.as_view(), name="review_by_user"),


    path('cart/<int:id>', CartRUDViewSet.as_view(), name="cart"),
    path('cart_create', CartCreateAPIView.as_view(), name='cart_create'),
    path('cart_lists', CartListAPIView.as_view(), name='cart_lists'),
    path('cart_list_by_user', CartUserListAPIView.as_view(), name='cart_list_by_user'),
    path('profile_create', ProfileCreateAPIView.as_view(), name='profile_create'),
    path('profile_get_all', ProfileAllListAPIView.as_view(), name='profile_get_all'),
    path('profile/<int:id>', ProfileRUDView.as_view(), name='profile'),
    path("", include(router.urls))
    # path("", include(review_router.urls))
    # path('review/<int:id>', ReviewViewSet.as_view({'post': 'create', 'get': 'list'}), name="review"),
]
