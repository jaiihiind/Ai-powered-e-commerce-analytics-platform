# Ai-powered-e-commerce-analytics-platform

# 🛒 Amazon E-Commerce AI Analytics Platform

An end-to-end **Data Analytics + AI project** that analyzes historical
Amazon e-commerce sales data using **Databricks, SQL, Python, Google Gemini,
Google ADK, and Power BI**.

The project combines data engineering, business analytics, machine learning,
AI agents, anomaly detection, revenue forecasting, and interactive
visualization into a single analytical workflow.

---

## 📌 Project Overview

The objective of this project is to transform raw historical e-commerce
data into actionable business insights.

The workflow covers:

- Data ingestion
- Data cleaning and transformation
- Business KPI analysis
- Product and category analysis
- Inventory-risk analysis
- Cancellation analysis
- Anomaly detection
- Revenue forecasting
- AI-powered business analysis
- Interactive Power BI reporting

---

## 🏗️ Architecture

```text
                 Amazon Historical Data
                          │
                          ▼
                    Databricks
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
           Bronze                  Silver
         Raw Data              Cleaned Data
              │                       │
              └───────────┬───────────┘
                          ▼
                         Gold
                  Business Analytics
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
        Sales         Inventory       Operations
       Analytics        Risk            Analysis
          │               │               │
          └───────────────┼───────────────┘
                          ▼
                    AI Analytics
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
       Anomaly         Revenue       Recommendation
       Detection       Forecasting       Signals
          │               │               │
          └───────────────┼───────────────┘
                          ▼
                   Google Gemini
                      + ADK
                          │
                  Multi-Agent Layer
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
      Sales           Inventory         Operations
      Agent             Agent              Agent
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                    Manager Agent
                          │
                          ▼
                     Power BI
                          │
                          ▼
                  Business Insights
