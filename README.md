# Airbnb NYC 2019 - Data Cleaning Pipeline

A reusable data cleaning pipeline built for the Airbnb NYC 2019 dataset, done as part of my ML internship tasks. The goal was to take raw, messy data and turn it into a clean dataset ready for analysis or modeling, while handling missing values, outliers, type issues, and basic schema checks.

Dataset source: [Kaggle - New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)

## What This Project Covers

- **Schema validation** - checks that all expected columns exist in the dataset before processing
- **Type inference** - converts `last_review` to a proper date type and makes sure `price` is numeric
- **Missing values** - fills in missing `name`/`host_name` values, and fills `reviews_per_month` with 0 for listings that never got a review
- **Outlier handling** - removes listings with `price = 0` (data errors), caps `minimum_nights` at 365, and removes extreme price outliers using the IQR method

## Why These Choices

- `last_review` and `reviews_per_month` are missing together for the same rows - these are listings that have zero reviews, so a missing review date makes sense and `reviews_per_month = 0` is the logical fill
- `price = 0` doesn't make sense for a real listing, so these rows are treated as data errors and removed
- `minimum_nights` had values as high as 1250, which isn't realistic for a short-term rental, so it's capped at 365 days
- The IQR method is used to catch remaining extreme price outliers without manually picking a cutoff

## Project Structure

```
airbnb-nyc-cleaning/
├── app.py                  # cleaning pipeline
├── data/
│   └── AB_NYC_2019.csv
├── requirements.txt
└── README.md
```

## How to Run

1. Clone this repo
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
3. Run the script:
   ```
   python app.py
   ```

The cleaned dataset will be saved as `data/AB_NYC_2019_cleaned.csv`.

## Tools Used

Python, Pandas
