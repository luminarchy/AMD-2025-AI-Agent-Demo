import numpy as np
import pandas



def format_list(list: pandas.DataFrame):
    """Formats a dataframe into a python list
        list: dataframe containing entries with a single value
        returns a list """
    result = np.concatenate(list.values).tolist()
    return result


def format_entry(entry: pandas.DataFrame):
    """Formats a dataframe entry into a python dictionary
        entry: a dataframe with one singular entry with multiple values
        returns a dict """
    poem = {"Title": entry["Title"][0], "Poem": entry["Poem"][0], "Poet": entry["Poet"][0], "Tags": entry["Tags"][0]}
    return poem

def format_entry_2(entry: pandas.Series):
    """Formats a series entry into a python dictionary
        entry: a series with one singular entry with multiple values
        returns a dict """
    poem = {"Title": entry["Title"], "Poem": entry["Poem"], "Poet": entry["Poet"], "Tags": entry["Tags"]}
    return poem

def format_entries(entries: pandas.DataFrame):
    """Formats a dataframe with into python dictionaries
        entry: a dataframe with some number of entries with multiple values
        returns a list of dictionaries """
    poems = []
    if entries.count(0)["Title"] > 1:
        poems = (entries.apply(format_entry_2, axis = 1))
        return (poems.values).tolist()
    else:
        return format_entry(entries)
    
def format_sqlauth(authors: list[str]):
    """Formats a sql query for filtering by a list of authors
        authors: a list of author names
        returns a string with a sql query """
    auth = "(Poet LIKE \"%"
    auth += "%\" OR Poet LIKE \"%".join(authors)
    auth += "%\") "

def format_sqlkey(keywords: list[str]):
    """Formats a sql query for filtering by a list of keywords
        authors: a list of keywords
        returns a string with a sql query """
    key += "(Tags LIKE \"%"
    key += "%\" OR Tags LIKE \"%".join(keywords)
    key += "\"%)"

def format_sqltags(tags: list[str]):
    """Formats a sql query for filtering by a list of tags
        authors: a list of tags
        returns a string with a sql query """
    tag += "(Tags LIKE \"%"
    tag += "%\" OR Tags LIKE \"%".join(tags)
    tag += "\"%) "

def format_tags(tags: list[str]):
    """Formats a list of tags into a string
        tags: a list of tags
        returns a string separating each tag with a comma """
    tags = []
    for tag in tags:
        tags += tag.split(",")
    return set(tags)