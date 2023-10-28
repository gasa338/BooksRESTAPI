from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *


class GenreViewListAPI(ListAPIView):
    """
    Get list of all GENRE with detail view. <strong> only for login user</strong>
    """
    serializer_class = GenreSerializerDetail
    queryset = Genre.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)


class GenreViewCreateAPI(CreateAPIView):
    """
    Create Genre using only if <strong>login as superuser</strong>
    """
    serializer_class = GenreSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.create(request, *args, **kwargs)
        return Response({"message: You are not authorized to create item!"}, status=status.HTTP_401_UNAUTHORIZED)


class GenreViewRUDAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    http_method_names = ["get", 'delete', 'put']
    lookup_field = 'id'

    def get_queryset(self):
        return Genre.objects.all()

    def put(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        res = {"message": "You are not authorized to change data!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.partial_update(request, *args, **kwargs)
        res = {"message": "You are not authorized to change data!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        res = {"message": "You are not authorized to delete items!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)


class WriterViewListAPI(ListAPIView):
    """
    Get list of all writer with detail view. <strong> only for login user</strong>
    """
    serializer_class = WriterSerializerDetail

    queryset = Writer.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)


class WriterViewCreateAPI(CreateAPIView):
    """
    Create Genre using only if <strong>login as superuser</strong>
    """
    serializer_class = WriterSerializerCreate

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.create(request, *args, **kwargs)
        return Response({"message: You are not authorized to create item!"}, status=status.HTTP_401_UNAUTHORIZED)


class WriterViewRUDAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = WriterSerializer
    http_method_names = ["get", 'post', 'delete', 'put']
    lookup_field = 'id'

    def get_queryset(self):
        return Writer.objects.all()

    def put(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        res = {"message": "You are not authorized to change data!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.partial_update(request, *args, **kwargs)
        res = {"message": "You are not authorized to change data!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            # return self.destroy(request, *args, **kwargs)
            self.destroy(request, *args, **kwargs)
            return Response(data='{"message": "Deleted"}', status=status.HTTP_204_NO_CONTENT)
        res = {"message": "You are not authorized to delete items!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)


class PublisherViewAPIView(ListCreateAPIView):
    serializer_class = PublisherSerializer

    def get_queryset(self):
        return Publisher.objects.all()

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"message: You are not authorized to create item!"}, status=status.HTTP_401_UNAUTHORIZED)

    def perform_create(self, serializer):
        serializer.save()


class PublisherRUDViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = PublisherSerializer
    http_method_names = ["get", 'post', 'delete', 'put']
    lookup_field = 'id'

    def get_queryset(self):
        return Publisher.objects.all()

    def put(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        res = {"message": "You are not authorized to change data!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.partial_update(request, *args, **kwargs)
        res = {"message": "You are not authorized to change data!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            # return self.destroy(request, *args, **kwargs)
            self.destroy(request, *args, **kwargs)
            return Response(data='{"message": "Deleted"}', status=status.HTTP_204_NO_CONTENT)
        res = {"message": "You are not authorized to delete items!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)


class BookCreateAPIView(CreateAPIView):
    """
    <b>Kreiranje knjige ukoliko si ulogovan kao super user</b>
    """
    serializer_class = BookSerializerCreate

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.create(request, *args, **kwargs)
        res = {"message": "You are not authorized to create book!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializerList

    def get_queryset(self):
        return Book.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BookRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializerCreate
    http_method_names = ["get", 'delete', 'put']
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == "GET":
            self.serializer_class = BookSerializerList
        else:
            self.serializer_class = BookSerializerCreate
        return Book.objects.all()

    def put(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        res = {"message": "You are not authorized to change data!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.partial_update(request, *args, **kwargs)
        res = {"message": "You are not authorized to change data!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            # return self.destroy(request, *args, **kwargs)
            self.destroy(request, *args, **kwargs)
            return Response(data='{"message": "Deleted"}', status=status.HTTP_204_NO_CONTENT)
        res = {"message": "You are not authorized to delete items!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)


class BookReviewViewAPICreate(CreateAPIView):
    """
    Create review for book, if user login
    """
    serializer_class = ReviewSerializerCreate

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                serializer = ReviewSerializerCreate(data=request.data)
                book = Book.objects.get(pk=request.data.get('book'))
                rating = request.data.get('rating')
                comment = request.data.get('comment')
                serializer.is_valid(raise_exception=True)
                serializer.save(book=book, user=request.user, rating=rating, comment=comment)

                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        res = {"message": "You are not authorized to create review", "error": False}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)


class BookReviewViewAPIUpdate(UpdateAPIView):
    """
    Concrete view for updating Book review.
    @:argument review id
    """
    serializer_class = ReviewSerializerCreate
    queryset = Review.objects.all()
    lookup_field = 'id'
    http_method_names = ['put']

    def put(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            review_obj = Review.objects.get(pk=kwargs.get('id'))
            user_id = review_obj.user_id  # Ukoliko hocu da dobijem ID od ForenKey dodajem "obj_name" i "_id"

            if request.user.id is user_id:
                return self.update(request, *args, **kwargs)
            else:
                res = {"message": "You are not authorize to change this review", "error": True}
                return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

        res = {"message": "You are not authorized to create review", "error": True}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class BookReviewViewAPIDelete(DestroyAPIView):
    """
    Concrete view for deleting a model instance.
    """
    serializer_class = ReviewSerializerDelete
    queryset = Review.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            review_obj = Review.objects.get(pk=kwargs.get('id'))
            user_id = review_obj.user_id  # Ukoliko hocu da dobijem ID od ForenKey dodajem "obj_name" i "_id"

            if request.user.id is user_id:
                return self.destroy(request, *args, **kwargs)
            else:
                res = {"message": "You are not authorize to delete this review", "error": True}
                return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)
        res = {"message": "You are not authorized to delete review", "error": False}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)


class BookReviewViewAPIList(ListAPIView):
    """
    Concrete view for listing a queryset.
    """
    serializer_class = ReviewSerializerDetail
    queryset = Review.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BookReviewViewAPILists(ListAPIView):
    """
    Concrete view for listing a queryset.
    """
    serializer_class = ReviewSerializerDetail
    queryset = Review.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.list(request, *args, **kwargs)
        res = {"message": "You are not authorized to get all review", "error": False}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)


class BookReviewViewAPIListByBook(ListAPIView):
    """
    Concrete view for listing a queryset.
    """
    serializer_class = ReviewSerializerDetail
    # queryset = Review.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return Review.objects.filter(book=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BookReviewViewAPIListByUser(ListAPIView):
    """
    Concrete view for listing a queryset.
    """
    serializer_class = ReviewSerializerDetail
    lookup_field = "id"

    def get_queryset(self):
        return Review.objects.filter(user=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    http_method_names = ['get', 'post', 'delete']
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def reserve(self, request, pk=None):
        if request.user.is_authenticated:

            book = Book.objects.get(id=pk)
            quantity = request.data['quantity']
            user = request.user

            try:
                reserve = Reservation.objects.get(user=user.id, books=pk)

                reserve.quantity = quantity
                reserve.save()
                serializer = ReservationSerializer(reserve)

                response = {'message': 'Reservation updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                reserve = Reservation.objects.create(user=user, quantity=quantity, books=book)
                reserve.save()
                serializer = ReservationSerializer(reserve, many=True)
                response = {'message': 'Rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide quantity'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class CartCreateAPIView(CreateAPIView):
    """
    <b>Kreiranje knjige ukoliko si ulogovan kao super user</b>
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    http_method_names = ['get', 'post', 'delete']
    permission_classes = (IsAuthenticated,)


class CartRUDViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = CartListSerializer
    http_method_names = ["get", 'delete', 'put']
    lookup_field = 'id'

    def get_queryset(self):
        return Cart.objects.all()

    def put(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.update(request, *args, **kwargs)
        res = {"message": "You are not authorized to change data!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.partial_update(request, *args, **kwargs)
        res = {"message": "You are not authorized to change data!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            # return self.destroy(request, *args, **kwargs)
            self.destroy(request, *args, **kwargs)
            return Response(data={"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
        res = {"message": "You are not authorized to delete items!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)


class CartListAPIView(ListAPIView):
    """
    Prikaz svih s tavki iz korpe
    """
    serializer_class = CartListSerializer

    def get_queryset(self):
        return Cart.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.list(request, *args, **kwargs)
        res = {"message": "You are not authorized to get this data!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)


class CartUserListAPIView(ListAPIView):
    """
    Prikaz korpe iskljucivo za trenutnog ulogovoanog usera
    """
    serializer_class = CartListSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProfileCreateAPIView(CreateAPIView):
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except:
            print(request.user.id)
            profile_exist = Profile.objects.filter(user=request.user.id)
            if profile_exist:
                res = {"message": "The profile exists, it is not possible to create it twice. Please check the request"}
                return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

            res = {"message": "nesto nije uredu, molim vas proverite"}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)


class ProfileAllListAPIView(ListAPIView):
    serializer_class = ProfileSerializerDetail

    def get_queryset(self):
        return Profile.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.list(request, *args, **kwargs)
        res = {"message": "You are not authorized to get list of profiles"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)


class ProfileRUDView(RetrieveUpdateDestroyAPIView):
    """
    For <strong>GET</strong> method return detail data <hr>
    For <strong>PUT</strong><small>Update</small> use simple ID system
    """
    serializer_class = ProfileSerializer
    http_method_names = ["get", 'delete', 'put']
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.method == "GET":
            self.serializer_class = ProfileSerializerDetail
        else:
            self.serializer_class = ProfileSerializer
        return Profile.objects.filter(user=self.request.user.id)

    def put(self, request, *args, **kwargs):
        # self.serializer_class = ProfileSerializer
        if request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        res = {"message": "You are not authorized to change this profile"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.partial_update(request, *args, **kwargs)
        res = {"message": "You are not authorized to change data!"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.destroy(request, *args, **kwargs)
            return Response(data='{"message": "Deleted"}', status=status.HTTP_204_NO_CONTENT)
        res = {"message": "You are not authorized to delete this profile"}
        return Response(data=res, status=status.HTTP_401_UNAUTHORIZED)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (IsAuthenticated,)
#
#     @action(detail=True, methods=['POST'])
#     def rate_movie(self, request, pk=None):
#         if 'stars' in request.data:
#
#             movie = Movie.objects.get(id=pk)
#             stars = request.data['stars']
#             user = request.user
#
#             try:
#                 rating = Rating.objects.get(user=user.id, movie=movie.id)
#                 rating.stars = stars
#                 rating.save()
#                 serializer = RatingSerializer(rating, many=False)
#                 response = {'message': 'Rating updated', 'result': serializer.data}
#                 return Response(response, status=status.HTTP_200_OK)
#             except:
#                 rating = Rating.objects.create(user=user, movie=movie, stars=stars)
#                 serializer = RatingSerializer(rating, many=False)
#                 response = {'message': 'Rating created', 'result': serializer.data}
#                 return Response(response, status=status.HTTP_200_OK)
#
#         else:
#             response = {'message': 'You need to provide stars'}
#             return Response(response, status=status.HTTP_400_BAD_REQUEST)
# class RatingViewSet(viewsets.ModelViewSet):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (IsAuthenticated,)
#
#     def update(self, request, *args, **kwargs):
#         response = {'message': 'You cant update rating like that'}
#         return Response(response, status=status.HTTP_400_BAD_REQUEST)
#
#     def create(self, request, *args, **kwargs):
#         response = {'message': 'You cant create rating like that'}
#         return Response(response, status=status.HTTP_400_BAD_REQUEST)
