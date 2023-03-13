from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    #admin url
    path("admin/", admin.site.urls),

    #store app
    path('',include('store.urls')),

    path('account/', include('account.urls')),

    #cart app
    path('cart/', include('cart.urls')),

    path('payment/', include('payment.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)