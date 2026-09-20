# 🛒 Amazon E-Commerce AI Analytics Platform

### From Raw E-Commerce Data → Lakehouse → ML → AI Agents → Business Intelligence

An end-to-end **Data Analytics, Machine Learning, and Generative AI platform** built to transform historical Amazon e-commerce data into actionable business intelligence.

The project combines:

**Databricks + SQL + PySpark + Python + Machine Learning + Google Gemini + Google ADK + Power BI**

to build a complete analytical workflow covering data engineering, business analysis, predictive analytics, anomaly detection, inventory intelligence, AI agents, and interactive dashboards.

---

## 🚀 Why This Project?

Traditional dashboards answer:

> **"What happened?"**

This project goes further.

It is designed to answer:

> **"What happened?"**  
> **"What changed?"**  
> **"Which products/categories are driving performance?"**  
> **"Where are potential inventory risks?"**  
> **"Which patterns look unusual?"**  
> **"What does the historical model predict?"**  
> **"How can an AI analyst help interpret the results?"**

The goal is to demonstrate how a modern analytics platform can combine:

📊 Business Intelligence  
🧹 Data Engineering  
🐍 Python Analytics  
🤖 Machine Learning  
🧠 Generative AI  
👥 Multi-Agent Systems  
📈 Predictive Analytics

into one end-to-end solution.

---

# 🎯 Project Objectives

The platform was designed to:

- Analyze historical e-commerce sales performance
- Build a scalable data pipeline using Databricks
- Transform raw data into analytics-ready datasets
- Answer business questions using SQL
- Identify high-performing categories and products
- Analyze cancellation behavior
- Detect inventory-risk products
- Detect unusual revenue/order patterns
- Forecast historical revenue patterns
- Generate analytical recommendation signals
- Use AI agents to interpret business data
- Build an interactive Power BI business dashboard

---

# 🏗️ End-to-End Architecture

```text
                         ┌──────────────────────┐
                         │ Amazon Historical    │
                         │ E-Commerce Data      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Databricks     │
                         │      Lakehouse      │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ▼                               ▼
             ┌─────────────┐                ┌─────────────┐
             │   BRONZE    │                │   SILVER    │
             │ Raw Data    │ ─────────────► │ Clean Data  │
             └─────────────┘                └──────┬──────┘
                                                    │
                                                    ▼
                                             ┌─────────────┐
                                             │    GOLD     │
                                             │ Business    │
                                             │ Analytics   │
                                             └──────┬──────┘
                                                    │
                         ┌──────────────────────────┼───────────────────────┐
                         │                          │                       │
                         ▼                          ▼                       ▼
                  Sales Analytics          Inventory Intelligence    Operations
                         │                          │                       │
                         └──────────────────────────┼───────────────────────┘
                                                    │
                                                    ▼
                                           ┌─────────────────┐
                                           │  AI Analytics   │
                                           └────────┬────────┘
                                                    │
                         ┌──────────────────────────┼───────────────────────┐
                         ▼                          ▼                       ▼
                  Anomaly Detection          Revenue Forecasting      Recommendation
                                                                         Signals
                         │                          │                       │
                         └──────────────────────────┼───────────────────────┘
                                                    │
                                                    ▼
                                           ┌─────────────────┐
                                           │ Google Gemini   │
                                           │   + Google ADK  │
                                           └────────┬────────┘
                                                    │
                                                    ▼
                                           ┌─────────────────┐
                                           │ Multi-Agent AI  │
                                           │ Business Layer  │
                                           └────────┬────────┘
                                                    │
                         ┌──────────────────────────┼───────────────────────┐
                         ▼                          ▼                       ▼
                    Sales Agent              Inventory Agent         Operations Agent
                         │                          │                       │
                         └──────────────────────────┼───────────────────────┘
                                                    │
                                                    ▼
                                            Manager Agent
                                                    │
                                                    ▼
                                           ┌─────────────────┐
                                           │    Power BI     │
                                           │    Dashboard    │
                                           └────────┬────────┘
                                                    │
                                                    ▼
                                           Business Insights
