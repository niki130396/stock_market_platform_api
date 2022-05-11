from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.db.models import F, Sum, FilteredRelation, Subquery, OuterRef, IntegerField, Max
from stock_market_platform_api.crawling.models import (
    FinancialStatementFact,
)
from stock_market_platform_api.financial_statements.api.serializers import (
    RevenueByCompanySerializer,
    RevenueBySectorSerializer,
    NOPATSerializer,
)

from stock_market_platform_api.utils.query_helpers import (
    get_gross_margins_by_company,
    get_gross_margins_by_sector,
    get_revenue_by_sector,
)


class RevenueViewSet(ViewSet):
    @action(
        detail=False,
        methods=["Get"],
        url_path="revenue-by-sector",
        url_name="revenue_by_sector"
    )
    def get_revenue_by_sector(self, request):
        income_statement_fields = FinancialStatementFact.objects.filter(
            financial_statement_line__normalized_field__statement_type="income_statement"
        ).values(
            "fiscal_period",
            "value",
            sector=F("company__sector"),
            field_name=F("financial_statement_line__normalized_field__name")
        )
        revenue_fields = income_statement_fields.filter(field_name="total_revenue")
        grouped = revenue_fields.values(
            "sector", "fiscal_period"
        ).annotate(total_revenue=Sum("value")).order_by("fiscal_period")
        serializer = RevenueBySectorSerializer(grouped, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["Get"],
        url_path="revenue-by-company",
        url_name="revenue_by_company"
    )
    def get_revenue_by_company(self, request):
        income_statement_fields = FinancialStatementFact.objects.filter(
            financial_statement_line__normalized_field__statement_type="income_statement"
        ).values(
            "fiscal_period",
            "value",
            sector=F("company__sector"),
            industry=F("company__industry"),
            company_name=F("company__name"),
            field_name=F("financial_statement_line__normalized_field__name")
        )
        revenue_fields = income_statement_fields.filter(field_name="total_revenue")
        grouped = revenue_fields.values(
            "company_name", "sector", "industry", "fiscal_period"
        ).annotate(total_revenue=Sum("value")).order_by("company_name", "fiscal_period")

        serializer = RevenueByCompanySerializer(grouped, many=True)
        return Response(serializer.data)


class ReturnOnInvestedCapitalViewSet(ViewSet):
    @action(
        detail=False,
        methods=["GET"],
        url_path="roic-by-sector",
        url_name="roic_by_sector"
    )
    def get_return_on_invested_capital_by_sector(self, request):
        income_statement_fields = FinancialStatementFact.objects.filter(
            financial_statement_line__normalized_field__statement_type="income_statement"
        ).values(
            "fiscal_period",
            sector=F("company__sector"),
            company_name=F("company__name"),
            field_name=F("financial_statement_line__normalized_field__name")
        )
        joined = income_statement_fields.annotate(
            operating_income=Subquery(
                income_statement_fields.filter(
                    field_name="operating_income",
                    company_name=OuterRef("company_name"),
                    fiscal_period=OuterRef("fiscal_period")
                ).values("value"),
                output_field=IntegerField()
            )
        )\
        .values("fiscal_period", "sector", "company_name")\
        .annotate(
            operating_income_value=Max("operating_income")
        )
        nopat_serializer = NOPATSerializer(joined, many=True)
        return Response(nopat_serializer.data)



class BalanceSheetMetricsViewSet(ViewSet):
    @action(
        detail=False,
        methods=["GET"],
        url_path="revenue-by-sector",
        url_name="revenue_by_sector"
    )
    def get_revenue_by_sector(self, request):
        response = get_revenue_by_sector()
        return Response(response)

    @action(
        detail=False,
        methods=["GET"],
        url_path="gross-margin-company-wise",
        url_name="gross_margin_company_wise",
    )
    def get_gross_margin_by_company(self, request):
        gross_margins = get_gross_margins_by_company()
        return Response(gross_margins)

    @action(
        detail=False,
        methods=["GET"],
        url_path="gross-margin-sector-wise",
        url_name="gross_margin_sector_wise",
    )
    def get_gross_margin_by_sector(self, request):
        response = get_gross_margins_by_sector()
        return Response(response)
