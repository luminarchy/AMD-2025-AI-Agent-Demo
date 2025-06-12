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

if __name__ == "__main__":
    print("Starting MCP server on default port...")
    mcp.run()

# command to run: mcpo --port 8002 -- python server.py