from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_post_v1 = DefaultRouter()
router_post_v1.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                        basename='comment')
router_post_v1.register('v1/posts', PostViewSet,
                        basename='post')
router_post_v1.register('v1/group', GroupViewSet,
                        basename='group')
router_post_v1.register('v1/follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include(router_post_v1.urls)),
]
