from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, LikeViewSet, CommentViewSet, FollowViewSet

# create router 
router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'following', FollowViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

