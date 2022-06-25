from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from .views import RegisterView, UserView

app_name = 'accounts'

urlpatterns = [
    path("<int:pk>/", UserView.as_view(), name="user_view"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registration/', RegisterView.as_view(), name='registration'),
]