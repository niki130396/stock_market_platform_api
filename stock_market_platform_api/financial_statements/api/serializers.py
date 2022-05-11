from rest_framework import serializers

from stock_market_platform_api.financial_statements.models import StatementsMetaData


class StatementsMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatementsMetaData
        fields = "__all__"


class RevenueBySectorSerializer(serializers.Serializer):
    sector = serializers.CharField(max_length=50)
    fiscal_period = serializers.DateField()
    total_revenue = serializers.IntegerField()


class RevenueByCompanySerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=50)
    sector = serializers.CharField(max_length=50)
    industry = serializers.CharField(max_length=50)
    fiscal_period = serializers.DateField()
    total_revenue = serializers.IntegerField()


class NOPATSerializer(serializers.Serializer):
    fiscal_period = serializers.DateField()
    sector = serializers.CharField(max_length=50)
    company_name = serializers.CharField(max_length=50)
    operating_income = serializers.IntegerField()
    tax_provision = serializers.IntegerField()
