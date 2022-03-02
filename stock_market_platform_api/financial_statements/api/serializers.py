from rest_framework import serializers

from stock_market_platform_api.financial_statements.models import StatementsMetaData


class StatementsMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatementsMetaData
        fields = "__all__"


class BalanceSheetMetricsSerializer(serializers.Serializer):
    pass
