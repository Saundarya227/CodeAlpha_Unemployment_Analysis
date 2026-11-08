# Unemployment Analysis with Python

## Project Overview
This project analyses unemployment trends in India using Python. It explores unemployment rates across different regions, compares rural and urban unemployment, and examines changes before and during the COVID-19 period.

## Objectives
- Analyse unemployment trends over time.
- Compare rural and urban unemployment rates.
- Identify regions with higher average unemployment.
- Compare unemployment rates before and after April 2020.
- Study unemployment across geographical regions of India.

## Datasets
This project uses two datasets:

1. **Unemployment in India.csv** – Contains unemployment rates, estimated employment, labour participation rates, dates, regions and area classifications.
2. **Unemployment_Rate_upto_11_2020.csv** – Contains unemployment data with additional geographical information, including latitude, longitude and geographical regions.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib

## Analysis Performed

1. **Unemployment Trend Analysis:** Visualises average unemployment rates over time.
2. **Rural vs Urban Analysis:** Compares average unemployment rates in rural and urban areas.
3. **Top 10 Regions:** Identifies the ten regions with the highest average unemployment rates.
4. **COVID-19 Period Comparison:** Compares average unemployment before April 2020 and from April 2020 onwards.
5. **Geographical Region Analysis:** Compares unemployment rates across North, South, East, West and Northeast India.

## Key Findings
- The average unemployment rate in urban areas is approximately 13.17%, compared with 10.32% in rural areas.
- Tripura has the highest average unemployment rate among the regions in the first dataset.
- The average unemployment rate was approximately 9.61% before April 2020 and 20.19% from April 2020 onwards.
- North India has the highest average unemployment rate (15.89%) among the geographical regions in the second dataset.
- West India has the lowest average unemployment rate (8.24%) among those geographical regions.

*Note: These findings are descriptive results from the supplied datasets and do not establish that COVID-19 alone caused the observed changes.*

## Project Structure
```text
Unemployment_Analysis/
│
├── unemployment_analysis.py
├── Unemployment in India.csv
├── Unemployment_Rate_upto_11_2020.csv
├── unemployment_trend.png
├── rural_vs_urban.png
├── top_10_states_unemployment.png
├── covid_impact.png
├── geographical_region_unemployment.png
└── README.md
```

## How to Run the Project

1. Install Python.
2. Install the required libraries:

```bash
pip install pandas numpy matplotlib
```

3. Keep both CSV files in the project folder.
4. Run the Python script:

```bash
python unemployment_analysis.py
```

## Conclusion
This project demonstrates how Python can be used for data cleaning, exploration, statistical analysis and visualisation to understand unemployment patterns in India.