from mcp.server.fastmcp import FastMCP
import os
import argparse

mcp = FastMCP("SimpleServer")

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
    mcp.run("sse")