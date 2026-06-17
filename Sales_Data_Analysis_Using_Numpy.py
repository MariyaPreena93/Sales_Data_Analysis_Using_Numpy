#------------Sales Data Analysis Using NumPy---------------#
#creating array -productid,sales amount,quantity sold
import numpy as np

sales = np.array([[101, 1200, 5],[102, 1500, 8],[103, 1800, 10],[104, 1000, 4],[105, 2500, 15],
                 [106, 1700, 9],[107, 3000, 20],[108, 2200, 12]])
print(sales)

#total Sales

total_sales = np.sum(sales[:,1])
print("Total sales amount:",total_sales)

#Average sales

Avg_sales = np.mean(sales[:,1])
print("Average sales Amount:",Avg_sales)

#Highest sales

print("-----Highest sale-----")

max_index = np.argmax(sales[:,1])

print("Product ID:", sales[max_index,0])
print("Highest Sales:", sales[max_index,1])

#product with sales amount above 2000

print("-----product with sales amount above 2000-----")
high_sales = sales[sales[:,1]>2000]
print(high_sales)

#Total quantity sold

tot_quan = np.sum(sales[:,2])
print("Total Quantity:",tot_quan)

#Revenue per unit

revenue = sales[:,1]/sales[:,2]
print("Revenue per unit:",revenue)

#sort by sales amount
sorted_sales = sales[sales[:,1].argsort()]
print(sorted_sales)

#Median sales
med = np.median(sales[:,1])
print("Median sales:",med)

#Standard Deviation of Sales
std_dev =np.std(sales[:,1])
print("Standard Deviation of Sales:",std_dev)

#Top 3 Products by Sales
print("-------Top 3 Products by Sales--------")
sort =sales[sales[:,1].argsort()]
top_3 = sort[-3:]
print(top_3)

#Products below Average Sales
print("-----Products below Average Sales-----")
bel_avg = sales[sales[:,1]<Avg_sales]
print(bel_avg)

#Percentage Contribution of each Product to Total Sales
print("---Percentage Contribution of each Product to Total Sales---")
percent = (sales[:,1]/total_sales)*100

for i in range(len(sales)):
    print(
        f"Product {sales[i,0]} contributes {percent[i]:.2f}%"
    )

