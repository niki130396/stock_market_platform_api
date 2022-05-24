from rest_framework import serializers

from stock_market_platform_api.financial_statements.models import StatementsMetaData


class StatementsMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatementsMetaData
        fields = "__all__"


class RevenueBySectorSerializer(serializers.Serializer):
    industry = serializers.CharField(max_length=50, required=False)
    sector = serializers.CharField(max_length=50, required=False)
    company_name = serializers.CharField(max_length=100, required=False)
    fiscal_period = serializers.DateField()
    total_revenue = serializers.IntegerField()


class NOPATSerializer(serializers.Serializer):
    fiscal_period = serializers.DateField()
    sector = serializers.CharField(max_length=50)
    company_name = serializers.CharField(max_length=50)
    nopat = serializers.IntegerField()
