from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #urls for the admin site
 path('admin/', admin.site.urls),

 #register urls for the cart app
 path('cart/', include('cart.urls', namespace='cart')),

 #register urls for the shop app
 path('', include('shop.urls', namespace='shop')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)