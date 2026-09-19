try:
    from amazon_analyst.manager_agent import manager_agent
except ImportError:
    from manager_agent import manager_agent

root_agent = manager_agent