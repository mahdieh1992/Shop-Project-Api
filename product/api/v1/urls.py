from django.urls import path
from .views import CategoryApiView



app_name='api-v1'

urlpatterns = [
    path('category/',CategoryApiView.as_view({'get':'list','post':'create'}),name='category')
    
]
