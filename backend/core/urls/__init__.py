from django.urls import path, include
from .admin import urlpatterns as admin_urlpatterns
from .common import urlpatterns as common_urlpatterns

app_name = 'core'

urlpatterns = [
    path('/admin/', include(admin_urlpatterns)),
    path('/common/', include(common_urlpatterns)),
]
