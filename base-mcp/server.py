from fastmcp import FastMCP
from tools import initialize_tools
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)
mcp = FastMCP("base mcp server", port = "8002")
initialize_tools(mcp)


if __name__ == "__main__":
    print("Starting MCP server on port")
    mcp.run(transport='stdio')

# command to run: mcpo --port 8002 -- python poem.py

