from django.urls import path
from .views import LoginUserView

app_name='api-v1'
urlpatterns = [
        path('login/',LoginUserView.as_view(),name='login')
]