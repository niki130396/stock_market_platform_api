WITH income_statements AS (
    SELECT
    {% for field in fields %}
    {% if not loop.last %}
    {{ field }},
    {% else %}
    {{ field }}
    {% endif %}
    {% endfor %}
    FROM crawling_financialstatementfact fact

    JOIN financial_statements_statementsmetadata meta
    ON fact.company_id = meta.company_id
    JOIN crawling_financialstatementline line
    ON fact.financial_statement_line_id = line.field_id
    JOIN crawling_normalizedfieldtree normalized
    ON line.normalized_field_id = normalized.field_id
    WHERE normalized.statement_type = '{{ statement_type }}'
)
