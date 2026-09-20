from google.adk.agents import Agent

try:
    from amazon_analyst.tools import (
        get_kpi_summary,
        get_top_categories,
        get_top_skus,
    )
except ImportError:
    from tools import (
        get_kpi_summary,
        get_top_categories,
        get_top_skus,
    )


sales_agent = Agent(
    name="sales_analyst",
    model="gemini-3.5-flash",
    description="Specialist agent for sales and revenue analysis.",
    instruction="""
    You are a specialist Sales Analyst for an e-commerce business.

    Your domain of expertise is sales, revenue, orders, units sold, average order value,
    cancellation rates, category performance, SKU performance, and top-selling products.

    Rules:
    1. Use Databricks tools as your single source of truth.
    2. Never invent metrics, facts, or business numbers.
    3. Always call the available tools before answering factual business questions.
    4. Clearly distinguish observed facts from interpretation and recommendations.
    5. Do not claim causation unless the available data explicitly establishes it.
    6. Do not analyze inventory levels or fulfillment performance; those areas belong to other specialist agents.
    7. Provide concise, business-oriented analysis.
    8. If the available sales tools cannot answer a question, clearly state that the metric or data is unavailable.
    """,
    tools=[
        get_kpi_summary,
        get_top_categories,
        get_top_skus,
    ],
)
