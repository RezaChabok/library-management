from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('books.urls')),
    path('', include('borrower.urls')),
    path('', include('category.urls')),
    path('', include('shelf.urls')),
    path('', include('user_auth.urls')),
    path('',include('home.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


