# Sales Data Analysis Using NumPy

## Project Overview

This project demonstrates how to perform basic data analysis using the NumPy library in Python. The dataset contains product sales information, including Product ID, Sales Amount, and Quantity Sold.

The project calculates key business metrics such as total sales, average sales, median sales, standard deviation, top-selling products, and percentage contribution of each product.

---

## Technologies Used

- Python 3
- NumPy

---

## Dataset

The dataset is stored as a NumPy array.

| Product ID | Sales Amount | Quantity Sold |
|------------|--------------|---------------|
| 101 | 1200 | 5 |
| 102 | 1500 | 8 |
| 103 | 1800 | 10 |
| 104 | 1000 | 4 |
| 105 | 2500 | 15 |
| 106 | 1700 | 9 |
| 107 | 3000 | 20 |
| 108 | 2200 | 12 |

---

## Features Implemented

### 1. Total Sales Calculation

Calculates the total revenue generated from all products.

### 2. Average Sales

Calculates the average sales amount.

### 3. Highest Sales Product

Identifies:
- Product ID with highest sales
- Highest sales amount

### 4. Revenue Per Unit

Calculates revenue generated per unit sold.

### 5. Median Sales

Calculates the median sales value.

### 6. Standard Deviation

Measures the variation in sales values.

### 7. Top 3 Products by Sales

Sorts products by sales amount and displays the top 3 performers.

### 8. Products Below Average Sales

Filters products whose sales are below the average sales value.

### 9. Percentage Contribution

Calculates the percentage contribution of each product to total sales.

---

## Sample Output

```text
Total Sales: 14900

Average Sales: 1862.5

Highest Sales Product:
Product ID: 107
Highest Sales: 3000

Median Sales: 1750.0

Standard Deviation of Sales: 651.32

Top 3 Products by Sales:
[[108 2200 12]
 [105 2500 15]
 [107 3000 20]]

Products Below Average Sales:
[[101 1200    5]
 [102 1500    8]
 [103 1800   10]
 [104 1000    4]
 [106 1700    9]]

Percentage Contribution:
Product 101 contributes 8.05%
Product 102 contributes 10.07%
Product 103 contributes 12.08%
...
