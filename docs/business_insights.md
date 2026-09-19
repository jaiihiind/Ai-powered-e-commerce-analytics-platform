# Business Insights

## Executive Summary

The Amazon historical e-commerce dataset contains approximately 91 days of
sales activity from March 31, 2022 to June 29, 2022.

The analysis focuses on revenue performance, order cancellations, product
categories, SKU performance, inventory risk, fulfillment, anomalies, and
revenue forecasting.

---

## 1. Overall Business Performance

| KPI | Value |
|---|---:|
| Total Orders | 120,378 |
| Cancelled Orders | 17,185 |
| Total Units Sold | 110,992 |
| Gross Order Value | ₹78,592,678.30 |
| Net Revenue | ₹71,673,394.00 |
| Average Order Value | ₹694.56 |
| Cancellation Rate | 14.28% |

The dataset records ₹71.67 million in net revenue across the analyzed period.

---

## 2. Category Performance

The highest-revenue categories were:

| Category | Net Revenue |
|---|---:|
| Set | ₹35,731,673 |
| Kurta | ₹19,425,870 |
| Western Dress | ₹10,209,590 |
| Top | ₹4,904,066 |
| Ethnic Dress | ₹732,744 |

Set generated the largest net revenue among the analyzed categories.

---

## 3. Cancellation Analysis

The overall cancellation rate was 14.28%.

Category-level cancellation rates varied across the product categories.

Examples include:

- Set: 14.61%
- Kurta: 14.64%
- Western Dress: 13.81%
- Top: 12.12%
- Ethnic Dress: 12.54%

These values can be used to identify categories that warrant further
investigation into cancellation patterns.

The analysis does not establish the cause of cancellations.

---

## 4. Top SKU Performance

Several individual SKUs generated significant revenue.

Examples include:

- J0230-SKD-M: ₹483,611
- JNE3797-KR-L: ₹470,083
- J0230-SKD-S: ₹448,825
- JNE3797-KR-M: ₹403,850
- JNE3797-KR-S: ₹360,194

These SKUs can be prioritized for further inventory and sales analysis.

---

## 5. Inventory Risk

The inventory analysis identifies products using the project's inventory
classification rules:

- OUT_OF_STOCK
- LOW_STOCK
- NORMAL
- NO_SALES

Several high-revenue SKUs were classified as LOW_STOCK or OUT_OF_STOCK.

Examples include:

- JNE3797-KR-L — LOW_STOCK
- J0230-SKD-S — LOW_STOCK
- JNE3797-KR-M — LOW_STOCK
- JNE3797-KR-S — LOW_STOCK
- JNE3797-KR-XXL — OUT_OF_STOCK

These signals can help analysts investigate potential inventory
prioritization opportunities.

The classification is a portfolio-project heuristic and should not be
treated as a validated production replenishment policy.

---

## 6. Anomaly Detection

Historical revenue and order patterns were analyzed using rolling historical
statistics and z-score based anomaly thresholds.

The anomaly framework identifies unusual observations and classifies them as:

- HIGH
- MEDIUM

The detected anomalies indicate unusual patterns in the historical dataset.

An anomaly does not automatically establish a business cause.

---

## 7. Revenue Forecasting

A Random Forest regression model was developed to generate historical
revenue predictions.

Features included:

- Day of week
- Month
- Revenue lag 1
- Revenue lag 7
- Orders lag 1
- Orders lag 7

The dataset was divided chronologically into training and evaluation periods.

The Power BI dashboard presents actual revenue alongside predicted revenue.

Because the dataset contains approximately 91 daily observations, the forecast
should be interpreted as a portfolio demonstration and historical backtest,
not as a production forecasting system.

---

## 8. Business Questions Addressed

The project answers questions such as:

1. How much revenue was generated?
2. How many orders were placed?
3. What percentage of orders were cancelled?
4. Which categories generate the most revenue?
5. Which SKUs generate the most revenue?
6. Which states contribute the most revenue?
7. Which fulfillment types generate revenue?
8. Which products have inventory risk?
9. Are there unusual revenue patterns?
10. How does predicted revenue compare with actual revenue?
11. What analytical signals can be generated automatically?

---

## 9. Recommended Analytical Actions

Based on the analysis, the following areas can be investigated:

### Inventory

Prioritize investigation of high-revenue SKUs that are classified as
LOW_STOCK or OUT_OF_STOCK.

### Cancellations

Investigate categories and products with comparatively higher cancellation
rates to identify operational or customer-experience patterns.

### Revenue

Monitor high-revenue categories and SKUs to understand their contribution
to overall business performance.

### Anomalies

Investigate detected anomalous dates against operational events, order
patterns, fulfillment behavior, and product-level changes.

### Forecasting

Continue collecting more historical observations before using the forecasting
approach for production decision-making.

---

## Important Analytical Disclaimer

The findings in this document are descriptive and analytical observations
from the available historical dataset.

They do not establish causal relationships unless separately validated.
