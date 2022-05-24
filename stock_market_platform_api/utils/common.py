

def get_statement_granularity(granularity):
    granularity_levels = {
            "sector": ["sector"],
            "industry": ["sector", "industry"],
            "company_name": ["sector", "industry", "company_name"]
    }
    return granularity_levels[granularity]
