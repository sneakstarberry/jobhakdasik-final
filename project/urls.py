
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import board.views
import log.views
import debate.views
import mypage.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.home, name='home'),
    path('board/', include('board.urls')),
    path('log/', include('log.urls')),
    path('debate/', include('debate.urls')),
    path('mypage/', include('mypage.urls')),


    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
