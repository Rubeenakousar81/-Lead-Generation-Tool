
def score_leads(df):
    def score(row):
        loc_score = 10 if row["Location"] == "USA" else 5
        emp_score = 10 if row["Employees"] > 150 else 5
        domain_score = row["Domain_Rating"] / 10
        return round((loc_score + emp_score + domain_score), 2)

    df["Lead_Score"] = df.apply(score, axis=1)
    return df
