from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('all', views.Dictionary_View,'all')
router.register('ㄱ', views.Dictionary1_View, 'ㄱ')
router.register('ㄴ', views.Dictionary2_View, 'ㄴ')
router.register('ㄷ', views.Dictionary3_View,'ㄷ')
router.register('ㄹ', views.Dictionary4_View,'ㄹ')
router.register('ㅁ', views.Dictionary5_View,'ㅁ')
router.register('ㅂ', views.Dictionary6_View,'ㅂ')
router.register('ㅅ', views.Dictionary7_View,'ㅅ')
router.register('ㅇ', views.Dictionary8_View,'ㅇ')
router.register('ㅈ', views.Dictionary9_View,'ㅈ')
router.register('ㅊ', views.Dictionary10_View,'ㅊ')
router.register('ㅋ', views.Dictionary11_View,'ㅋ')
router.register('ㅌ', views.Dictionary12_View,'ㅌ')
router.register('ㅍ', views.Dictionary13_View,'ㅍ')
router.register('ㅎ', views.Dictionary14_View,'ㅎ')

urlpatterns = [

    path('dictionary/', include(router.urls)),

    ]