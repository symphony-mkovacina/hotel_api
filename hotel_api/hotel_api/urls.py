from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers

from hotel_app import views
from hotel_app.views import HotelViewSet

router = routers.DefaultRouter()
router.register(r'hotel_api', HotelViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^hotel_api/get_hotel_reviews/(?P<hotel_id>[0-9]+)/$', views.GetHotelReview.as_view(), name='reviews'),
    url(r'^favorites/$', views.get_hotel_favorites, name='favorites'),
    url(r'^favorites/add_remove$', views.add_to_favorites, name='add_favorite'),
    url(r'^increment_counter/$', views.increment_counter, name='increment_counter'),
    url(r'^register/$', views.CreateUserView.as_view(), name='user'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.Login.as_view(), name='login'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
