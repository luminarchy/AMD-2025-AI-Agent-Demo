from fastmcp import FastMCP
import asyncio
import os
import argparse
import requests
import logging
import json
import format

logger = logging.getLogger(__name__)


mcp = FastMCP("poetry server", port = 8002)

url = "https://poetrydb.org"


@mcp.tool()
async def get_all_authors(): # idk what the input would be for a get all? 
    """Gets a list of all poets in the database."""
    try: 
        result = await asyncio.to_thread(lambda:requests.get(url+"/author").json())
        return format.format_allauthors(result)
    except Exception as e:
        logger.exception(f"poetrydb search error: {str(e)}")

@mcp.tool()
async def get_author(author: str): # idk what the input would be for a get all? 
    """Gets a list of the titles of all poems written by a specific author."""
    try: 
        result = await asyncio.to_thread(lambda:requests.get(url+"/author/" + author + "/title").json())
        return format.format_author(result)
    except Exception as e:
        logger.exception(f"poetrydb search error: {str(e)}")

@mcp.tool()
async def get_poem_title(poem: str): # idk what the input would be for a get all? 
    """gets a poem by the title."""
    try: 
        result = await asyncio.to_thread(lambda:requests.get(url+"/title/" + poem).json())
        return result
    except Exception as e:
        logger.exception(f"poetrydb search error: {str(e)}")

@mcp.tool()
async def get_poems_keyword(keyword: str): # idk what the input would be for a get all? 
    """searches for poems with keyword in title."""
    try: 
        result = await asyncio.to_thread(lambda:requests.get(url+"/title/" + keyword + "/title").json())
        return result
    except Exception as e:
        logger.exception(f"poetrydb search error: {str(e)}")

@mcp.tool()
async def get_poems_line(line: str, args: list[str]): # idk what the input would be for a get all? 
    """searches for poems with a specific line and returns an output based on arguments in args such as title, author, and/or line count."""
    try: 
        output_field = ""
        if args != []:
            output_field += "/"
            output_field += ",".join(args)
        result = await asyncio.to_thread(lambda:requests.get(url+"/title/" + line + output_field).json())
        return result
    except Exception as e:
        logger.exception(f"poetrydb search error: {str(e)}")

@mcp.tool()
async def get_linecount(count: str, args: list[str]): # idk what the input would be for a get all? 
    """searches for poems with a specific linecount and returns an output based on arguments in args such as title, author, and/or line count."""
    try: 
        output_field = ""
        if args != []:
            output_field += "/"
            output_field += ",".join(args)
        result = await asyncio.to_thread(lambda:requests.get(url+"/title/" + count + output_field).json())
        return result
    except Exception as e:
        logger.exception(f"poetrydb search error: {str(e)}")

if __name__ == "__main__":
    print("Starting MCP server on default port...")
    mcp.run()

# command to run: mcpo --port 8002 -- python server.py

