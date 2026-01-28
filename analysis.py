import pandas as pd
import numpy as np

data = {
    "OrderID": [101,102,103,104,105,106,107,108,109,110],
    "OrderDate": [
        "2023-01-05","2023-01-15","2023-02-10","2023-02-20",
        "2023-03-05","2023-03-18","2023-01-25","2023-02-28",
        "2023-03-22","2023-03-30"
    ],
    "Customer": ["Asha","Rohan","Asha","Kunal","Ritu","Asha","Rohan","Kunal","Ritu","Asha"],
    "City": ["Delhi","Mumbai","Delhi","Pune","Delhi","Delhi","Mumbai","Pune","Delhi","Delhi"],
    "Product": ["Pen","Notebook","Notebook","Pen","Notebook","Pen","Pen","Notebook","Pen","Notebook"],
    "Quantity": [2,1,3,2,4,3,2,1,5,2],
    "Price": [10,50,50,10,50,10,10,50,10,50]
}

df = pd.DataFrame(data)
print(df)


# STEP 1: Basic Inspection
print(df.head())
print(df.info())
print(df.isnull().sum())

# STEP 2: Data Cleaning
# Convert OrderDate to datetime
# Remove duplicates (if any)
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
print(df.dtypes)
df = df.drop_duplicates()

# step 3 
# create a new column
df["Total"] = df["Quantity"] * df["Price"]
print(df)

# step 4 time analysis
df["Month"] = df["OrderDate"].dt.month
# print(df["Month"])
# monthly total revenue
monthlyrevenue = df.groupby("Month")["Total"].sum()
print(monthlyrevenue)

# step 5 business analysis
revenuepercust = df.groupby("Customer")["Total"].sum()
revenuepercity = df.groupby("City")["Total"].sum()
revenueperprod = df.groupby("Product")["Total"].sum()
print("------Total Revenue Per Customer, City and Product------------")
print(revenuepercust)
print(revenuepercity)
print(revenueperprod)
print("---------------------------------------------------------------\n")

#step 6
cityProdPerRevenue = pd.pivot_table(df, index = ["City", "Product"], values = "Total", aggfunc = "sum", fill_value = 0)
monthCustPerRevenue = pd.pivot_table(df, index = ["Month", "Customer"], values = "Total", aggfunc = "sum", fill_value = 0)
print("-------Pivot Tables-------")
print(cityProdPerRevenue)
print(monthCustPerRevenue)
print("--------------------------\n")

#step 7
highestRevenueGenerator = df.groupby("Customer")["Total"].sum().sort_values(ascending = False).head(1)
print("Top Customer: ",highestRevenueGenerator, "\n")
# Asha generated the higfhest revenue

bestCity = df.groupby("City")["Total"].sum().sort_values(ascending = False).head(1)
print("Top City: ",bestCity,"\n")
# Delhi is the best performing City

productSoldMost = df.groupby("Product")["Total"].sum().sort_values(ascending = False).head(1)
print("Top Product: ",productSoldMost,"\n")
# Notebook generated most revenue

monthHighestSales = df.groupby("Month")["Total"].sum().sort_values(ascending = False).head(1)
print("Top Month: ",monthHighestSales,"\n")
#Month 3 had highset sales