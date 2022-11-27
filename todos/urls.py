from rest_framework.routers import DefaultRouter

from todos.views import TodoViewSet

urlpatterns = []
router = DefaultRouter()
router.register(r'reviews', TodoViewSet, basename='todo')
urlpatterns += router.urls
