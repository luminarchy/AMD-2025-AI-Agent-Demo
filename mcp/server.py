from fastmcp import FastMCP
import asyncio
import os
import argparse

mcp = FastMCP("Test server")

@mcp.tool()
def hello_world(name: str = "World"):
    """A simple hello world tool."""
    return {"message": f"Hello, {name}!"}

@mcp.tool()
def add(a: int, b: int):
    """Add two numbers."""
    return a + b

# async def run_search(params):
#     """Run SerpAPI search asynchronously"""
#     try:
#         logger.debug(f"Sending SerpAPI request with params: {json.dumps(params, indent=2)}")
#         result = await asyncio.to_thread(lambda: GoogleSearch(params).get_dict())
#         logger.debug(f"SerpAPI response received, keys: {list(result.keys())}")
#         return result
#     except Exception as e:
#         logger.exception(f"SerpAPI search error: {str(e)}")
#         return {"error": str(e)}

if __name__ == "__main__":
    print("Starting MCP server on default port...")
    mcp.run(transport = "sse", host = "127.0.0.1", port = 8001)