  #include setting form file setting 
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from api import views 

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


router = routers.DefaultRouter()
router.register('customer', views.CustomerViewSet)
router.register('product', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



