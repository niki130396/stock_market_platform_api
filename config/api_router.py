from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from stock_market_platform_api.financial_statements.api.views import (
    RevenueViewSet,
    ReturnOnInvestedCapitalViewSet,
)
from stock_market_platform_api.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

router.register("revenue", RevenueViewSet, basename="revenue")
router.register("roic", ReturnOnInvestedCapitalViewSet, basename="roic")

app_name = "api"
urlpatterns = router.urls
