from fastmcp import FastMCP, Context
import logging
from openai import OpenAI
logger = logging.getLogger(__name__)

openai_api_base = "http://127.0.0.1:8001/v1"
def register_knowledge(mcp):
    @mcp.tool
    def get_meter():
        meter = ""
        meter += "Meter is composed of two components: The number of syllables in a line and a pattern of emphasis on those syllables. A line of poetry can be broken into “feet,” which are individual units within a line of poetry. A foot of poetry has a specific number of syllables and a specific pattern of emphasis. \n"
        + "In English poetry, the most common types of metrical feet are two syllables and three syllables long. They’re characterized by their particular combination of stressed syllables (DUH or /) and unstressed syllables (duh or -). The common types of feet include: \n"
        + "Trochee (trochaic): Pronounced DUH-duh (/-), as in 'ladder': LAD-der\n"
        + "Iamb (iambic): Pronounced duh-DUH, as in 'indeed': in-DEED\n"
        + "Spondee (spondaic). Pronounced DUH-DUH, as in 'TV.' \n"
        + "Dactyl (dactylic). Pronounced DUH-duh-duh, as in 'certainly': CER-tain-ly \n"
        + "Anapest (anapestic). Pronounced duh-duh-DUH, as in 'what the heck!' (Anapestic poetry typically divides its stressed syllables across multiple words.) \n \n"
        + "Metrical feet are repeated over the course of a line of poetry to create poetic meter. We describe the length of a poetic meter by using Greek suffixes: \n"
        + "one foot = monometer \n"
        + "two feet = dimeter \n"
        + "three feet = trimeter \n"
        + "four feet = tetrameter \n"
        + "five feet = pentameter \n"
        + "six feet = hexameter \n" 
        + "seven feet = heptameter \n"
        + "eight feet = octameter \n"
        + "eight feet = octameter \n"
        + "meter "


