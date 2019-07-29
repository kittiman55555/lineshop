from django.conf import settings  #include setting form file setting 
from django.conf.urls.static import static #call static in setting
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from api import views 
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


router = routers.DefaultRouter()
router.register('customer', views.CustomerViewSet)
router.register('product', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'api/v1/customer/$', views.CustomerList.as_view()),
    #url(r'customer/(?P<line_id>[0-9]+)/$', views.CustomerDetail.as_view()),
     url(r'api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)