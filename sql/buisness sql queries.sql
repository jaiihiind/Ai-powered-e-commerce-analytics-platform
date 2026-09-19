-- Databricks notebook source
-- ============================================================
-- Amazon E-Commerce AI Analytics Project
-- Business Questions & SQL Analysis
-- ============================================================

USE CATALOG ecommerce_ai;

-- ============================================================
-- 1. Overall Business KPIs
-- ============================================================

SELECT *
FROM ai.v_kpi_summary;


-- ============================================================
-- 2. Which product categories generate the most revenue?
-- ============================================================

SELECT *
FROM ai.v_top_categories
ORDER BY net_revenue DESC;


-- ============================================================
-- 3. Which SKUs generate the most revenue?
-- ============================================================

SELECT *
FROM ai.v_top_skus
ORDER BY net_revenue DESC
LIMIT 20;


-- ============================================================
-- 4. Which SKUs have inventory risk?
-- ============================================================

SELECT *
FROM ai.v_inventory_risk
WHERE inventory_status IN ('OUT_OF_STOCK', 'LOW_STOCK')
ORDER BY net_revenue DESC;


-- ============================================================
-- 5. How does revenue vary by fulfillment type?
-- ============================================================

SELECT *
FROM ai.v_fulfillment
ORDER BY net_revenue DESC;


-- ============================================================
-- 6. What are the daily sales trends?
-- ============================================================

SELECT *
FROM gold.daily_sales
ORDER BY Date;


-- ============================================================
-- 7. Which states generate the most revenue?
-- ============================================================

SELECT *
FROM gold.state_performance
ORDER BY net_revenue DESC;


-- ============================================================
-- 8. International Sales Performance
-- ============================================================

-- SELECT *
-- FROM ai.v_international_sales
-- ORDER BY net_revenue DESC;