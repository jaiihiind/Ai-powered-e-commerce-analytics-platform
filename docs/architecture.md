# Project Architecture

## Amazon E-Commerce AI Analytics Platform

This project is an end-to-end data analytics and AI-powered business intelligence
solution built using Databricks, SQL, Python, Google Gemini/ADK, and Power BI.

## Architecture

```text
Amazon Historical E-Commerce Data
              │
              ▼
       Databricks Lakehouse
              │
       ┌──────┴──────┐
       ▼             ▼
    Bronze          Silver
   Raw Data       Clean Data
       │             │
       └──────┬──────┘
              ▼
             Gold
      Business Analytics
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
   Sales   Inventory  Operations
   KPIs      Risk      Analysis
      │       │        │
      └───────┼────────┘
              ▼
        AI Analytics Layer
      ┌───────┼────────┐
      ▼       ▼        ▼
   Anomaly  Forecast  Recommendations
  Detection  Revenue     Signals
              │
              ▼
        Google Gemini
          + Google ADK
              │
       Multi-Agent Layer
              │
      ┌───────┼────────────┐
      ▼       ▼            ▼
    Sales  Inventory   Operations
    Agent    Agent        Agent
              │
              ▼
        Manager Agent
              │
              ▼
        Power BI Dashboard
              │
              ▼
       Business Insights
