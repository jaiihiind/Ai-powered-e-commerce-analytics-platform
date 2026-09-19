import datetime
from decimal import Decimal
import os
from typing import Any, Dict, List
from databricks import sql


def _json_safe(value: Any) -> Any:
    """Convert database values into JSON-serializable Python types."""
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return float(value)
    return value


def _get_connection():
    """Create and return a Databricks SQL connection using environment variables."""
    server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME")
    http_path = os.getenv("DATABRICKS_HTTP_PATH")
    access_token = os.getenv("DATABRICKS_TOKEN")

    missing = []
    if not server_hostname:
        missing.append("DATABRICKS_SERVER_HOSTNAME")
    if not http_path:
        missing.append("DATABRICKS_HTTP_PATH")
    if not access_token:
        missing.append("DATABRICKS_TOKEN")

    if missing:
        raise ValueError(
            f"Missing required Databricks environment variable(s): {', '.join(missing)}"
        )

    return sql.connect(
        server_hostname=server_hostname,
        http_path=http_path,
        access_token=access_token,
    )


def _execute_query(query: str) -> List[Dict[str, Any]]:
    """Execute a read-only SELECT query and return results as a list of dictionaries."""
    if not query.strip().upper().startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed.")

    with _get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            return [
                {col: _json_safe(val) for col, val in zip(columns, row)}
                for row in rows
            ]


def get_kpi_summary() -> List[Dict[str, Any]]:
    """Retrieve high-level business KPI summary including total orders, revenue, and cancellation rate."""
    return _execute_query("SELECT * FROM ecommerce_ai.ai.v_kpi_summary")


def get_top_categories() -> List[Dict[str, Any]]:
    """Retrieve performance metrics for top product categories."""
    return _execute_query(
        """
        SELECT *
        FROM ecommerce_ai.ai.v_top_categories
        ORDER BY net_revenue DESC
        LIMIT 10
        """
    )


def get_top_skus() -> List[Dict[str, Any]]:
    """Retrieve top-selling SKU metrics including sales volume and revenue."""
    return _execute_query(
        """
        SELECT *
        FROM ecommerce_ai.ai.v_top_skus
        ORDER BY net_revenue DESC
        LIMIT 20
        """
    )


def get_inventory_risk() -> List[Dict[str, Any]]:
    """Retrieve inventory risk analysis including stock levels and low-stock indicators."""
    return _execute_query(
        """
        SELECT *
        FROM ecommerce_ai.ai.v_inventory_risk
        WHERE inventory_status IN ('OUT_OF_STOCK', 'LOW_STOCK')
        ORDER BY net_revenue DESC
        LIMIT 20
        """
    )


def get_fulfillment_performance() -> List[Dict[str, Any]]:
    """Retrieve fulfillment performance data across shipping and delivery methods."""
    return _execute_query(
        """
        SELECT *
        FROM ecommerce_ai.ai.v_fulfillment
        ORDER BY net_revenue DESC
        """
    )


def get_anomaly_events() -> List[Dict[str, Any]]:
    """Retrieve detected sales anomaly events and their severity."""
    return _execute_query(
        """
        SELECT *
        FROM ecommerce_ai.ai.anomaly_events
        ORDER BY Date DESC
        LIMIT 20
        """
    )


def get_anomaly_root_cause() -> List[Dict[str, Any]]:
    """Retrieve daily category, fulfillment, and state breakdowns for anomaly root-cause analysis."""
    return _execute_query(
        """
        SELECT *
        FROM ecommerce_ai.ai.v_root_cause_daily
        ORDER BY Date DESC
        LIMIT 20
        """
    )


def get_revenue_forecast() -> List[Dict[str, Any]]:
    """Retrieve historical and predicted revenue data from the revenue forecasting model."""
    return _execute_query(
        """
        SELECT *
        FROM ecommerce_ai.ai.revenue_forecast
        ORDER BY Date
        """
    )


