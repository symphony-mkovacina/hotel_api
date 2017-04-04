from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hotel
from .serializers import HotelSerializer, UserSerializer, ReviewSerializer


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
        hotel = Hotel.objects.get(pk=hotel_id)
        reviews = hotel.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view()
def get_hotel_favorites(request):
    """
    The api view that exposes favorite hotels for current user.
    :param request: The get request containing the authorisation token.
    :return: The favorite hotels.
    """
    hotels = Hotel.objects.filter(user=request.user)
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_to_favorites(request):
    try:
        hotel = Hotel.objects.get(pk=request.data.get('hotel_id'))
        is_favorite = request.data.get('is_favorite') if request.data.get('is_favorite') else ''

        if is_favorite.lower() == 'true':
            hotel.user.add(request.user)
            content = {'Message': 'Hotel added to favorites'}
        else:
            hotel.user.remove(request.user)
            content = {'Message': 'Hotel removed from favorites'}

        return Response(content, status=status.HTTP_200_OK)
    except Exception as e:
        content = {'Error': str(e)}
        return Response(content, status=status.HTTP_404_NOT_FOUND)


