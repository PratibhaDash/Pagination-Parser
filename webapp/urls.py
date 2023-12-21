from django.urls import include, path
from rest_framework.routers import DefaultRouter
from webapp import views


router = DefaultRouter()

router.register("yourmodel", views.YourModelViewSet, basename="yourmodel")

urlpatterns = [
    path('', include(router.urls)),
]