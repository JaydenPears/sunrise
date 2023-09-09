from django.urls import path, include
from .common import urlpatterns as common_urlpatterns

app_name = 'core'

urlpatterns = [
    path('/', include(common_urlpatterns)),
]
