from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.db.models import F, Sum, Q
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from stock_market_platform_api.crawling.models import (
    IncomeStatementFieldsMaterializedView,
)
from stock_market_platform_api.financial_statements.api.serializers import (
    RevenueBySectorSerializer,
    NOPATSerializer,
)
from stock_market_platform_api.utils.common import get_statement_granularity


class RevenueViewSet(ViewSet):
    @action(
        detail=False,
        methods=["Get"],
        url_path="revenue-by-sector",
        url_name="revenue_by_sector"
    )
    @method_decorator(cache_page(60 * 60))
    def get_revenue_by_sector(self, request):
        aggregate_by = request.query_params.get("granularity")
        if not aggregate_by:
            raise ValueError("Choose a granularity")
        granularity = get_statement_granularity(aggregate_by)
        field_values = [
            *granularity,
            "fiscal_period",
        ]
        income_statement_fields = IncomeStatementFieldsMaterializedView.objects.all().values(*field_values) \
            .filter(~Q(sector=""), ~Q(industry=""), total_revenue__isnull=False)\
            .annotate(total_revenue=Sum("total_revenue"))\
            .order_by(*field_values)
        serializer = RevenueBySectorSerializer(income_statement_fields, many=True)
        return Response(serializer.data)


class ReturnOnInvestedCapitalViewSet(ViewSet):
    @action(
        detail=False,
        methods=["GET"],
        url_path="roic-by-sector",
        url_name="roic_by_sector"
    )
    def get_return_on_invested_capital_by_sector(self, request):
        # income_statement_fields = IncomeStatementFieldsMaterializedView.objects.all().values(
        #     "fiscal_period",
        #     "sector",
        #     "company_name",
        #     "field_name"
        # )
        # joined = income_statement_fields.annotate(
        #     operating_income_value=Subquery(
        #         income_statement_fields.filter(
        #             field_name="operating_income",
        #             company_name=OuterRef("company_name"),
        #             fiscal_period=OuterRef("fiscal_period")
        #         ).values("value"),
        #         output_field=IntegerField()
        #     ),
        #     tax_provision_value=Subquery(
        #         income_statement_fields.filter(
        #             field_name="tax_provision",
        #             company_name=OuterRef("company_name"),
        #             fiscal_period=OuterRef("fiscal_period")
        #         ).values("value")
        #     )
        # )\
        # .values("fiscal_period", "sector", "company_name")\
        # .annotate(
        #     nopat=(Max("operating_income_value") - Max("tax_provision_value"))
        # ).order_by("company_name", "fiscal_period")

        nopat = IncomeStatementFieldsMaterializedView.objects.all().values(
            "fiscal_period",
            "sector",
            "company_name",
        ).annotate(
            nopat=(F("operating_income") - F("tax_provision"))
        )

        nopat_serializer = NOPATSerializer(nopat, many=True)
        return Response(nopat_serializer.data)
