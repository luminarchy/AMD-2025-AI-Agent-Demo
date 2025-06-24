from fastmcp import FastMCP
from poemtools import initialize_tools
from poemprompts import register_prompts
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)
mcp = FastMCP("poetry server", port = "9002")
initialize_tools(mcp)
register_prompts(mcp)


if __name__ == "__main__":
    print("Starting MCP server on port")
    mcp.run(transport='stdio')

# command to run: mcpo --port 8002 -- python poem.py

