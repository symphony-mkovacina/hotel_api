from django.contrib.auth import get_user_model
from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hotel, Counter
from .serializers import HotelSerializer, UserSerializer, ReviewSerializer, FavoriteSerializer


class HotelViewSet(viewsets.ModelViewSet):
    """
    The api view that exposes all CRUD operations on hotels.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Hotel.objects.all().order_by('-date')
    serializer_class = HotelSerializer


class CreateUserView(CreateAPIView):
    """
    The api view for user registration.
    """
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class GetHotelReview(APIView):
    """
    The api view that exposes reviews for passed hotel ID.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        reviews = hotel.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view()
def get_hotel_favorites(request):
    """
    The api view that exposes favorite hotels for current user.
    :param request: The GET request containing the authorisation token.
    :return: The favorite hotels.
    """
    hotels = Hotel.objects.filter(user=request.user)
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_to_favorites(request):
    """
    Add/remove hotel from favorites.
    :param request: The POST request containing hotel_id and is_favorite flag.
    :return: 200 OK 0r 404 not found, depending on result.
    """
    try:
        serializer = FavoriteSerializer(request.data)
        hotel = Hotel.objects.get(pk=serializer.data['hotel_id'])
        is_favorite = serializer.data['is_favorite']

        if is_favorite:
            hotel.user.add(request.user)
            content = {'Message': 'Hotel added to favorites'}
        else:
            hotel.user.remove(request.user)
            content = {'Message': 'Hotel removed from favorites'}

        return Response(content, status=status.HTTP_200_OK)
    except Exception as e:
        content = {'Error': str(e)}
        return Response(content, status=status.HTTP_404_NOT_FOUND)


@api_view()
def increment_counter(request):
    """
    Hit counter. If count is even number, method returns 200 OK, otherwise handled 400 BAD REQUEST
    :param request: The GET request object.
    :return:  200 OK 0r 400 bad request, depending on count number.
    """
    try:
        counter, created = Counter.objects.get_or_create(name='test', defaults={'hit_count': 1})
        is_even = counter.hit_count % 2 == 0

        if not created:
            counter.hit_count = F('hit_count') + 1
            counter.save()

        if not is_even:
            raise Exception('Not even number!')

        return Response({'Success': 'It is even number!'}, status=status.HTTP_200_OK)
    except Exception as e:
        content = {'Error': str(e)}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
