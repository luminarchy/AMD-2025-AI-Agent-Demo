from fastmcp import FastMCP
from poemtools import register_tools
import format


mcp = FastMCP("poetry server", port = 8002)

register_tools(mcp)


if __name__ == "__main__":
    print("Starting MCP server on default port...")
    mcp.run()

# command to run: mcpo --port 8002 -- python poem.py

