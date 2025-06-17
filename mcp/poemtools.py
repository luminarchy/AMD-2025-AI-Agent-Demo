from fastmcp import FastMCP
import asyncio
import requests
import logging
import pandas as pd
import pandas.io.sql as sql
from sqlalchemy import create_engine
import numpy as np
import format as f

logger = logging.getLogger()
url = "https://poetrydb.org"
rep = lambda x: x.replace("_x000D_", "").strip()
pf = pd.read_excel("PoetryFoundationData.xlsx", header = 0, index_col=0, usecols = "A:E", converters = {1: rep, 2: rep, 3: rep, 4: rep})
engine = create_engine('sqlite://', echo=False)
pf.to_sql(name='poemsf', con=engine)


def register_authors(mcp):
    @mcp.tool()
    async def get_all_authors(): 
        """Gets a list of all poets in the database."""
        try: 
            result = await asyncio.to_thread(lambda:requests.get(url+"/author").json())
            return format.format_allauthors(result)
        except Exception as e:
            logger.exception(f"poetrydb search error: {str(e)}")
            


    @mcp.tool()
    async def get_author(author: str): 
        """Gets a list of the titles of all poems written by a specific author."""
        try: 
            result = await asyncio.to_thread(lambda:requests.get(url+"/author/" + author + "/title").json())
            return format.format_author(result)
        except requests.HTTPError as e:
            with engine.connect() as conn, conn.begin():
                authors = pd.read_sql_query("SELECT DISTINCT Poet FROM poemsf WHERE Poet LIKE \"%" + author + "%\"", conn)
            if authors.shape[0] == 0:
                logger.exception(f"poetry foundation invalid author name: {str(e)}")
                raise Exception
            elif authors.shape[0] != 1:
                return ("There are multiple authors found in the database: " + f.format_list(authors) + ". Which one did you mean?")
            else: 
                authors = pd.read_sql_query("SELECT title FROM poemsf WHERE Poet LIKE \"%" + author + "%\"", conn)
                return f.format_list(authors)
        except Exception as e:
            logger.exception(f"poetrydb search error: {str(e)}")
            

def register_poems(mcp):
    @mcp.tool()
    async def get_poem_title(poem: str): 
        """gets a poem by the title."""
        try: 
            result = await asyncio.to_thread(lambda:requests.get(url+"/title/" + poem).json())
            return result
        except requests.HTTPError as e:
            with engine.connect() as conn, conn.begin():
                poe = pd.read_sql_query("SELECT * FROM poemsf WHERE Title LIKE \"%" + poem + "%\"", conn)
            if poe.shape[0] == 0:
                logger.exception(f"poetry foundation invalid poem name: {str(e)}")
                raise Exception
            elif poe.shape[0] != 1:
                return ("There are multiple authors found in the database: " + f.format_list(poe) + ". Which one did you mean?")
            else:
                return f.format_entry(poe)
        except Exception as e:
            logger.exception(f"poetrydb search error: {str(e)}")


    @mcp.tool()
    async def get_poems_keyword(keyword: str): 
        """searches for poems that contain specific keyword and return the titles of those poems."""
        try: 
            result = await asyncio.to_thread(lambda:requests.get(url+"/title/" + keyword + "/title").json())
            return result
        except requests.HTTPError as e:
            with engine.connect() as conn, conn.begin():
                poe = pd.read_sql_query("SELECT Title FROM poemsf WHERE Poem LIKE \"%" + keyword + "%\"", conn)
            if poe.shape[0] == 0:
                logger.exception(f"poetry foundation invalid poem name: {str(e)}")
                raise Exception
            else:
                return f.format_list(poe)
        except Exception as e:
            logger.exception(f"poetrydb search error: {str(e)}")

    @mcp.tool()
    async def get_poems_keyword(keyword: str): 
        """searches for poems that contain specific keyword."""
        try: 
            result = await asyncio.to_thread(lambda:requests.get(url+"/title/" + keyword).json())
            return result
        except Exception as e:
            logger.exception(f"poetrydb search error: {str(e)}")

def register_lines(mcp):
    @mcp.tool()
    async def get_poems_line(line: str): 
        """searches for poems with a specific line."""
        try: 
            result = await asyncio.to_thread(lambda:requests.get(url+"/title/" + line).json())
            return result
        except Exception as e:
            logger.exception(f"poetrydb search error: {str(e)}")

    @mcp.tool()
    async def get_poems_line_output(line: str, args: list[str]): 
        """given a specific line and output format, searches for poems with a specific line and returns the specific parameters of the data"""
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
    async def get_linecount(count: str, args: list[str]): 
        """given a specific linecount and output format, searches for poems with a specific line and returns the specific parameters of the data."""
        try: 
            output_field = ""
            if args != []:
                output_field += "/"
                output_field += ",".join(args)
            result = await asyncio.to_thread(lambda:requests.get(url+"/title/" + count + output_field).json())
            return result
        except Exception as e:
            logger.exception(f"poetrydb search error: {str(e)}")