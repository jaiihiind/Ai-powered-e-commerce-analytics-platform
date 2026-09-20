import os
import sys
from databricks import sql


def main():
    server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME")
    http_path = os.getenv("DATABRICKS_HTTP_PATH")
    access_token = os.getenv("DATABRICKS_TOKEN")

    missing_vars = []
    if not server_hostname:
        missing_vars.append("DATABRICKS_SERVER_HOSTNAME")
    if not http_path:
        missing_vars.append("DATABRICKS_HTTP_PATH")
    if not access_token:
        missing_vars.append("DATABRICKS_TOKEN")

    if missing_vars:
        print(f"Error: Missing required environment variable(s): {', '.join(missing_vars)}")
        sys.exit(1)

    query = "SELECT * FROM ecommerce_ai.ai.v_kpi_summary"

    try:
        with sql.connect(
            server_hostname=server_hostname,
            http_path=http_path,
            access_token=access_token,
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)

                # Fetch column names
                columns = [desc[0] for desc in cursor.description]
                row = cursor.fetchone()

                print("Column names:")
                print(columns)
                print("\nReturned KPI values:")
                if row:
                    for col_name, val in zip(columns, row):
                        print(f"  {col_name}: {val}")
                else:
                    print("  No rows returned.")

                print("\nDatabricks connection successful!")

    except Exception as e:
        print(f"Connection or query execution failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
