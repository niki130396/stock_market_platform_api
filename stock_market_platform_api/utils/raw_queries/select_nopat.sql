

SELECT
    operating_income.company_name,
    operating_income.industry,
    operating_income.sector,
    operating_income.fiscal_period,
    operating_income.value - tax_provision.value AS nopat
FROM
    (SELECT * FROM income_statement_fields
    WHERE field_name = 'operating_income') operating_income

    JOIN

    (SELECT * FROM income_statement_fields
    WHERE field_name = 'tax_provision') tax_provision

    ON operating_income.company_name = tax_provision.company_name
    AND operating_income.fiscal_period = tax_provision.fiscal_period
ORDER BY company_name, fiscal_period
