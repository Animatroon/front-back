from rest_framework import routers
from django.urls import include, path
from .views import AuthorizationViewSet, RequestViewSet

app_name = 'users'


urlpatterns = [
    # path('test/', TestViewSet.as_view({'get': 'get_list'}), name="someTest"),
    # path('test/<str:name>/', TestViewSet.as_view({'get': 'get_list'}), name="someTest"),
#     path('test/post', TestViewSet.as_view({'post': 'post_req'}), name="someTest"),

    path('login/', AuthorizationViewSet.as_view({'post': 'login'}), name="authorization"),
    path('signup/', AuthorizationViewSet.as_view({'post': 'signup'}), name="authorization"),
    path('get/', AuthorizationViewSet.as_view({'get': 'get_user'}), name="authorization"),
    path('logout/', AuthorizationViewSet.as_view({'post': 'logout'}), name="authorization"),
    path('change/', AuthorizationViewSet.as_view({'post': 'change_password'}), name="authorization"),
    
    path('send_request/', RequestViewSet.as_view({'post': 'send_request'}), name="authorization"),
    path('get_requests/', RequestViewSet.as_view({'get': 'get_requests'}), name="authorization"),
    path('get_requestsUser/', RequestViewSet.as_view({'get': 'get_requests_byEmail'}), name="authorization"),
    path('delete_request/<int:id>', RequestViewSet.as_view({'delete': 'delete_request'}), name="authorization"),
    
]

# r = routers.DefaultRouter()

# r.register(r'test', TestViewSet)

# urlpatterns += r.urls



# [print('1', end= " ") for i in range(100)]
# print(r.urls)
