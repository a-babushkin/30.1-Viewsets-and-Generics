from django.urls import path
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserListApiView, UserUpdateApiView

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"payments", PaymentViewSet, basename="payments")

urlpatterns = [
    path("", UserListApiView.as_view(), name="user_list"),
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="users_update"),
]
urlpatterns += router.urls
