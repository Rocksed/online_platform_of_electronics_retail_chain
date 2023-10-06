from rest_framework.routers import DefaultRouter

from trade_network.views import FactoryViewSet

router = DefaultRouter()
router.register(r'Factory', FactoryViewSet, basename='factory')
urlpatterns = [

] + router.urls
