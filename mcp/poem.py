from fastmcp import FastMCP
from poemtools import initialize_tools
from poemprompts import register_prompts
import asyncio
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
mcp = FastMCP("poetry server", port = "8002")
initialize_tools(mcp)
register_prompts(mcp)
#register_knowledge(mcp)


if __name__ == "__main__":
    print("Starting MCP server on port")
    mcp.run()

# command to run: mcpo --port 8002 -- python poem.py

