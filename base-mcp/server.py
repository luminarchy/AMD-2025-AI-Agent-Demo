from fastmcp import FastMCP
from tools import initialize_tools
import logging
import asyncio


async def main():
    # setup logger
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    # set up MCP server
    mcp = FastMCP("base mcp server", port = "8002")
    await initialize_tools(mcp)
    await mcp.run_async(transport='stdio')


if __name__ == "__main__":
    print("Starting MCP server on port")
    asyncio.run(main())
    

# command to run: mcpo --port 8002 -- python poem.py

