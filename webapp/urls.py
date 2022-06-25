from django.urls import path

from webapp.views import IndexView, AdvertisementCreateView, AdvertisementUpdateView, AdvertisementView, \
    AdvertisementDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('advertisement/create/', AdvertisementCreateView.as_view(), name='advertisement_create'),
    path('advertisement/<int:pk>/update/', AdvertisementUpdateView.as_view(), name='advertisement_update'),
    path('advertisement/<int:pk>/', AdvertisementView.as_view(), name='advertisement_view'),
    path('advertisement/<int:pk>/delete/', AdvertisementDeleteView.as_view(), name='advertisement_delete'),

]