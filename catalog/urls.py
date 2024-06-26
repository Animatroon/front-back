from rest_framework import routers
from django.urls import include, path
from .views import CatalogViewSet, ReestrViewSet, PoiskPravoobladateleyViewSet, InostrannyeOkupyViewSet


urlpatterns = [
    path('all/', CatalogViewSet.as_view({'get': 'get_all_catalogs'}), name="doc"),
    path('catalog/<int:pk>', CatalogViewSet.as_view({'get': 'get_catalog'}), name="doc"),
    path('delete/<int:pk>', CatalogViewSet.as_view({'delete': 'delete_catalog'}), name="doc"),
    path('change/', CatalogViewSet.as_view({'patch': 'change_catalog'}), name="doc"),
    path('add/', CatalogViewSet.as_view({'post': 'add_catalog'}), name="doc"),
    
    path('reestr/all/', ReestrViewSet.as_view({'get': 'get_all_reestrs'}), name="doc"),
    path('reestr/catalog/<int:pk>', ReestrViewSet.as_view({'get': 'get_reestr'}), name="doc"),
    path('reestr/delete/<int:pk>', ReestrViewSet.as_view({'delete': 'delete_reestr'}), name="doc"),
    path('reestr/change/', ReestrViewSet.as_view({'patch': 'change_reestr'}), name="doc"),
    path('reestr/add/', ReestrViewSet.as_view({'post': 'add_reestr'}), name="doc"),
    path('reestr/add/sub/<int:id>', InostrannyeOkupyViewSet.as_view({'post': 'addSub'}), name="doc"),
    path('reestr/add/sub/delete/<int:id>', InostrannyeOkupyViewSet.as_view({'post': 'addSu2b3'}), name="doc"),
    path('reestr/add/sub3/get/<int:id>', InostrannyeOkupyViewSet.as_view({'get': 'addSu2b2'}), name="doc"),

    
    path('poisk_pravoobladateley/all/', PoiskPravoobladateleyViewSet.as_view({'get': 'get_all_poisk_pravoobladateleys'}), name="doc"),
    path('poisk_pravoobladateley/catalog/<int:pk>', PoiskPravoobladateleyViewSet.as_view({'get': 'get_poisk_pravoobladateley'}), name="doc"),
    path('poisk_pravoobladateley/delete/<int:pk>', PoiskPravoobladateleyViewSet.as_view({'delete': 'delete_poisk_pravoobladateley'}), name="doc"),
    path('poisk_pravoobladateley/change/', PoiskPravoobladateleyViewSet.as_view({'patch': 'change_poisk_pravoobladateley'}), name="doc"),
    path('poisk_pravoobladateley/add/', PoiskPravoobladateleyViewSet.as_view({'post': 'add_poisk_pravoobladateley'}), name="doc"),
    
    path('inostrannye_okupy/all/', InostrannyeOkupyViewSet.as_view({'get': 'get_all_inostrannye_okupys'}), name="doc"),
    path('inostrannye_okupy/catalog/<int:pk>', InostrannyeOkupyViewSet.as_view({'get': 'get_inostrannye_okupy'}), name="doc"),
    path('inostrannye_okupy/delete/<int:pk>', InostrannyeOkupyViewSet.as_view({'delete': 'delete_inostrannye_okupy'}), name="doc"),
    path('inostrannye_okupy/change/', InostrannyeOkupyViewSet.as_view({'patch': 'change_inostrannye_okupy'}), name="doc"),
    path('inostrannye_okupy/add/', InostrannyeOkupyViewSet.as_view({'post': 'add_inostrannye_okupy'}), name="doc"),
]

