import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("sales.csv") 
print("Data:\n", data) 
average = data["Sales"].mean() 
print("Average sales per month :", average) 
plt.bar(data["Month"], data["Sales"]) 
plt.xlabel("Month")
plt.ylabel("Sales") 
plt.title("Monthly sales of a product") 
plt.show()
