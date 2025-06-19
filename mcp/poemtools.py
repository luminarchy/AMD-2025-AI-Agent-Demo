from fastmcp import FastMCP, Context
import asyncio
import requests
import logging
import pandas as pd
from sqlalchemy import create_engine
import format as f

logger = logging.getLogger(__name__)


def initialize_tools(mcp: FastMCP):
    logger.info("setup started")
    url = "https://poetrydb.org"
    rep = lambda x: x.replace("_x000D_", "").strip()
    pf = pd.read_excel("PoetryFoundationData.xlsx", header = 0, index_col=0, usecols = "A:E", converters = {1: rep, 2: rep, 3: rep, 4: rep})
    engine = create_engine('sqlite://', echo=False)
    pf.to_sql(name='poemsf', con=engine)
    register_authors(mcp, url, engine)
    register_poems(mcp, engine)
    register_lines(mcp, url, engine)
    register_tags(mcp, url, engine)
    logger.info("setup ended")

def register_authors(mcp, url, engine):
    @mcp.tool()
    async def get_all_authors(): 
        """Gets a list of all poets in the database."""
        try: 
            result = await asyncio.to_thread(lambda:requests.get(url+"/author").json())
            return result
        except Exception as e:
            logger.exception(f"poetrydb search error: {str(e)}")
            


    @mcp.tool()
    async def get_author(author: str): 
        """Gets a list of the titles of all poems written by a specific author."""
        with engine.connect() as conn, conn.begin():
            authors = pd.read_sql_query("SELECT DISTINCT Poet FROM poemsf WHERE Poet LIKE \"%" + author + "%\"", conn)
            if authors.shape[0] == 0:
                logger.exception(f"poetry foundation invalid author name: {author}")
                return "Not Found"
            elif authors.shape[0] != 1:
                return ("There are multiple authors found in the database: " + f.format_list(authors) + ". Which one did you mean?")
            else: 
                authors = pd.read_sql_query("SELECT title FROM poemsf WHERE Poet LIKE \"%" + author + "%\"", conn)
                return f.format_list(authors)
            

def register_poems(mcp, engine):
    @mcp.tool()
    async def get_poem_title(poem: str, author: str = ""): 
        """gets a poem by the title."""
        
        with engine.connect() as conn, conn.begin():
            poe = pd.read_sql_query("SELECT * FROM poemsf WHERE Title LIKE \"%" + poem + "%\" AND Poet LIKE \"%" + author + "%\"", conn)
            if poe.shape[0] == 0:
                logger.exception(f"poetry foundation invalid poem name: {poem}")
                return "Not Found"
            elif poe.shape[0] != 1:
                return ("There are multiple poems found in the database: " + f.format_list(poe[0]) + ". Which one did you mean?")
            else:
                return f.format_entry(poe)


    @mcp.tool()
    async def get_poems_keyword_titles(keyword: str, author: str = "", tag = ""): 
        """searches for the titles of poems that contain specific keyword."""
    
        with engine.connect() as conn, conn.begin():
            poe = pd.read_sql_query("SELECT Title FROM poemsf WHERE Poem LIKE \"%" + keyword + "%\" AND Poet LIKE \"%" + author + "%\" AND Tag LIKE \"%" + tag + "%\"", conn)
            if poe.shape[0] == 0:
                logger.exception(f"poetry foundation invalid keyword: {keyword}")
                return "Not Found"
            else:
                return f.format_list(poe)
 

    @mcp.tool()
    async def get_poems_keyword(keyword: str, author: str = "", tag = ""): 
        """searches for poems that contain specific keyword."""
        with engine.connect() as conn, conn.begin():
            poe = pd.read_sql_query("SELECT * FROM poemsf WHERE Poem LIKE \"%" + keyword + "%\" AND Poet LIKE \"%" + author + "%\" AND Tag LIKE \"%" + tag + "%\"", conn)
            if poe.shape[0] == 0:
                logger.exception(f"poetry foundation invalid keyword: {keyword}")
                return "Not Found"
            else:
                return f.format_entries(poe)
    
def register_lines(mcp, url, engine):
    @mcp.tool()
    async def get_poems_line(line: str, author: str = ""): 
        """searches for poems with a specific line."""
        with engine.connect() as conn, conn.begin():
            poe = pd.read_sql_query("SELECT * FROM poemsf WHERE Poem LIKE \"%" + line + "%\" AND Poet LIKE \"%" + author + "%\"", conn)
            if poe.shape[0] == 0:
                logger.exception(f"poetry foundation invalid poem name: {line}")
                return "Not Found"
            else:
                return f.format_entries(poe)


    @mcp.tool()
    async def get_line_title(line: str, author: str = ""): 
        """searches for title of poems with a specific line."""
        
        with engine.connect() as conn, conn.begin():
            poe = pd.read_sql_query("SELECT Title FROM poemsf WHERE Poem LIKE \"%" + line + "%\" AND Poet LIKE \"%" + author + "%\"", conn)
            if poe.shape[0] == 0:
                logger.exception(f"poetry foundation invalid poem name: {line}")
                return "Not Found"
            else:
                return f.format_list(poe)
        return result 
    
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
    async def get_linecount(count: str): 
        """given a specific linecount and output format, searches for poems and returns the specific parameters of the data."""
        try: 
            output_field = ""
            result = await asyncio.to_thread(lambda:requests.get(url+"/title/" + count).json())
            return result
        except Exception as e:
            logger.exception(f"poetrydb search error: {str(e)}")
    
def register_tags(mcp, url, engine):
    @mcp.tool()
    def get_tag(tag: str, author: str = ""):
        """searches for poems that have a specific theme, images, and categories."""
        with engine.connect() as conn, conn.begin():
            poe = pd.read_sql_query("SELECT * FROM poemsf WHERE Tags LIKE \"%" + tag + "%\" AND Poet LIKE \"%" + author + "%\"", conn)
            if poe.shape[0] == 0:
                logger.exception(f"poetry foundation cannot find any poems under tag '{tag}'")
                raise Exception
            else: 
                return f.format_entries(poe)

    @mcp.tool()
    async def get_reference(authors: list[str], tags: list[str], ctx: Context):
        """searches for poems to refer to the user as inspiration or reccommended reading, based on context 
        and any authors, tags or keywords they are looking for or have a preference for"""
        sql = ("SELECT poemsf.* FROM poemsf WHERE ")
        result = []
        with engine.connect() as conn, conn.begin():
            if authors: 
                auth = sql + "(Poet LIKE \"%"
                auth += "%\" OR Poet LIKE \"%".join(authors)
                auth += "%\") "
                poe = pd.read_sql_query(auth, conn)
                result += f.format_entries(poe)
            if tags:
                tag += sql + "(Tags LIKE \"%"
                tag += "%\" OR Tags LIKE \"%".join(authors)
                tag += "\"%) "
                poe = pd.read_sql_query(tag, conn)
                result += f.format_entries(poe)
        if len(result) == 0:
            try: 
                result = await asyncio.to_thread(lambda:requests.get(url+"/random").json())
            except Exception as e:
                logger.exception(f"poetryDB error: {e}")
        return result






        
        
    