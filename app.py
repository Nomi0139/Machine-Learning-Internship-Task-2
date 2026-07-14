import pandas as pd

required_columns = ["id", "name", "host_id", "host_name", "neighbourhood_group",
                     "neighbourhood", "latitude", "longitude", "room_type", "price",
                     "minimum_nights", "number_of_reviews", "last_review",
                     "reviews_per_month", "calculated_host_listings_count", "availability_365"]


def clean_data(path):
    df = pd.read_csv(path)

    missing_cols = [col for col in required_columns if col not in df.columns]
    print("Missing columns:", missing_cols)

    df["last_review"] = pd.to_datetime(df["last_review"], errors="coerce")
    df["price"] = df["price"].astype(float)

    df["name"] = df["name"].fillna("Unknown")
    df["host_name"] = df["host_name"].fillna("Unknown")
    df["reviews_per_month"] = df["reviews_per_month"].fillna(0)

    df = df[df["price"] > 0]
    df["minimum_nights"] = df["minimum_nights"].clip(upper=365)

    q1 = df["price"].quantile(0.25)
    q3 = df["price"].quantile(0.75)
    iqr = q3 - q1
    upper_limit = q3 + 1.5 * iqr
    df = df[df["price"] <= upper_limit]

    return df


df = clean_data("data/AB_NYC_2019.csv")
print(df.shape)
print(df.isnull().sum())
df.to_csv("data/AB_NYC_2019_cleaned.csv", index=False)
