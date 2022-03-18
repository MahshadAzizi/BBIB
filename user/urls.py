from django.urls import path
from .views import *

urlpatterns = [
    path('logout/', logout_user, name='logout'),

    path('user_panel/', user_panel, name='user_panel'),
    path('user_list/', UserList.as_view(), name='user_list'),
    path('user_update/<int:id>', user_update, name='user_update'),
    path('user_detail/<int:pk>', UserDetail.as_view(), name='user_detail')
]