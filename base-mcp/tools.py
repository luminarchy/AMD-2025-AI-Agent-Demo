from fastmcp import FastMCP
import asyncio

@mcp.tool()
async def hello_world(name: str = "World"):
    """A simple hello world tool."""
    return {"message": f"Hello, {name}!"}

@mcp.tool()
async def add(a: int, b: int):
    """Add two numbers."""
    return a + b