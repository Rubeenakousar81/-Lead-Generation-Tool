
import pandas as pd

def enrich_company_data(df):
    enriched_data = []
    for idx, row in df.iterrows():
        domain = row['Website']
        enriched = {
            "Company": row['Company'],
            "Website": domain,
            "Location": "USA" if "us" in domain else "India",
            "Employees": 100 + idx * 10,
            "Domain_Rating": 50 + idx
        }
        enriched_data.append(enriched)
    return pd.DataFrame(enriched_data)
