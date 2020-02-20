from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from history.views import History_View
from genre.views import Genre_View
from image.views import Image_View

router = routers.DefaultRouter()
router.register('history', History_View)
router.register('genre', Genre_View)
router.register('image',Image_View)
#router.register('dictionary', Dictionary_View)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('dictionary.urls')),
]