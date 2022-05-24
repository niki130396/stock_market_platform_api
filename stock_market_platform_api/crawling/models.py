from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from stock_market_platform_api.financial_statements.models import StatementsMetaData


class NormalizedFieldTree(MPTTModel):
    STATEMENT_TYPE_CHOICES = [
        ("income_statement", "Income Statement"),
        ("balance_sheet", "Balance Sheet"),
        ("cash_flow", "Cash Flow"),
        ("other", "Other"),
    ]

    field_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    humanized_name = models.CharField(max_length=256, null=True, blank=True)
    statement_type = models.CharField(
        max_length=256, choices=STATEMENT_TYPE_CHOICES, default="income_statement"
    )
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, related_name="children", blank=True, null=True
    )

    def __str__(self):
        return f"{self.humanized_name} - {self.statement_type}"


class CrawlingSourceDetails(models.Model):
    SOURCE_TYPE_CHOICES = [("API", "API"), ("HTML", "HTML")]
    crawling_source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    source_type = models.CharField(
        max_length=256, choices=SOURCE_TYPE_CHOICES, default="API"
    )

    def __str__(self):
        return self.name


class StatementTypeLocalDefinition(models.Model):
    statement_type_definition_id = models.AutoField(primary_key=True)
    statement_type_local_name = models.CharField(max_length=256)

    def __str__(self):
        return self.statement_type_local_name


class FinancialStatementLine(models.Model):
    field_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256, null=True, blank=True)
    statement_type = models.ForeignKey(
        StatementTypeLocalDefinition, on_delete=models.DO_NOTHING, blank=True
    )
    crawling_source = models.ForeignKey(CrawlingSourceDetails, on_delete=models.CASCADE)
    normalized_field = TreeForeignKey(
        NormalizedFieldTree, on_delete=models.PROTECT, blank=True, null=True
    )


class FinancialStatementFact(models.Model):
    fact_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(StatementsMetaData, on_delete=models.PROTECT)
    financial_statement_line = models.ForeignKey(
        FinancialStatementLine, on_delete=models.PROTECT
    )
    fiscal_period = models.DateField(null=True, blank=True)
    unit = models.CharField(max_length=30, null=True, blank=True)
    value = models.IntegerField()

    class Meta:
        unique_together = ('company', 'financial_statement_line', 'fiscal_period')


class AbstractFinancialStatementModel(models.Model):
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=50, null=True, blank=True)
    sector = models.CharField(max_length=50, null=True, blank=True)
    fiscal_period = models.DateField()

    class Meta:
        abstract = True


class IncomeStatementFieldsMaterializedView(AbstractFinancialStatementModel):
    total_revenue = models.IntegerField(null=True, blank=True)
    cost_of_revenue = models.IntegerField(null=True, blank=True)
    gross_profit = models.IntegerField(null=True, blank=True)
    selling_general_and_administrative = models.IntegerField(null=True, blank=True)
    research_and_development = models.IntegerField(null=True, blank=True)
    operating_expense = models.IntegerField(null=True, blank=True)
    net_non_operating_interest_income_expense = models.IntegerField(null=True, blank=True)
    operating_income = models.IntegerField(null=True, blank=True)
    pretax_income = models.IntegerField(null=True, blank=True)
    tax_provision = models.IntegerField(null=True, blank=True)
    net_income = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = "income_statement_fields"


class BalanceSheetFieldsMaterializedView(AbstractFinancialStatementModel):
    cash_and_cash_equivalents = models.IntegerField(null=True, blank=True)
    other_short_term_investments = models.IntegerField(null=True, blank=True)
    cash_cash_equivalents_and_short_term_investments = models.IntegerField(null=True, blank=True)
    receivables = models.IntegerField(null=True, blank=True)
    inventory = models.IntegerField(null=True, blank=True)
    other_current_assets = models.IntegerField(null=True, blank=True)
    current_assets = models.IntegerField(null=True, blank=True)
    net_ppe = models.IntegerField(null=True, blank=True)
    investments_and_advances = models.IntegerField(null=True, blank=True)
    other_non_current_assets = models.IntegerField(null=True, blank=True)
    total_non_current_assets = models.IntegerField(null=True, blank=True)
    total_assets = models.IntegerField(null=True, blank=True)
    accounts_payable = models.IntegerField(null=True, blank=True)
    current_deferred_liabilities = models.IntegerField(null=True, blank=True)
    current_debt = models.IntegerField(null=True, blank=True)
    other_current_liabilities = models.IntegerField(null=True, blank=True)
    current_liabilities = models.IntegerField(null=True, blank=True)
    long_term_debt = models.IntegerField(null=True, blank=True)
    other_non_current_liabilities = models.IntegerField(null=True, blank=True)
    total_non_current_liabilities_net_minority_interest = models.IntegerField(null=True, blank=True)
    total_liabilities_net_minority_interest = models.IntegerField(null=True, blank=True)
    total_debt = models.IntegerField(null=True, blank=True)
    common_stock = models.IntegerField(null=True, blank=True)
    retained_earnings = models.IntegerField(null=True, blank=True)
    stockholders_equity = models.IntegerField(null=True, blank=True)
    total_equity_gross_minority_interest = models.IntegerField(null=True, blank=True)
    working_capital = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = "balance_sheet_fields"


class CashFlowFieldsMaterializedView(AbstractFinancialStatementModel):
    depreciation_and_amortization = models.IntegerField(null=True, blank=True)
    operating_cash_flow = models.IntegerField(null=True, blank=True)
    net_ppe_purchase_and_sale = models.IntegerField(null=True, blank=True)
    net_investment_purchase_and_sale = models.IntegerField(null=True, blank=True)
    net_other_investing_changes = models.IntegerField(null=True, blank=True)
    investing_cash_flow = models.IntegerField(null=True, blank=True)
    cash_dividends_paid = models.IntegerField(null=True, blank=True)
    net_common_stock_issuance = models.IntegerField(null=True, blank=True)
    net_issuance_payments_of_debt = models.IntegerField(null=True, blank=True)
    net_other_financing_charges = models.IntegerField(null=True, blank=True)
    financing_cash_flow = models.IntegerField(null=True, blank=True)
    end_cash_position = models.IntegerField(null=True, blank=True)
    free_cash_flow = models.IntegerField(null=True, blank=True)
    
    class Meta:
        managed = False
        db_table = "cash_flow_fields"
