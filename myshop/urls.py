from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myshop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('', include('shop.urls')),
    path('', include(('shop.urls', 'shop'), namespace='shop')),

    path("__reload__/", include("django_browser_reload.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
