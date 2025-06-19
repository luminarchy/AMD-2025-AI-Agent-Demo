import numpy as np
import pandas



def format_list(list: pandas.DataFrame):
    result = np.concatenate(list.values).tolist()
    return result


def format_entry(entry: pandas.DataFrame):
    poem = {"Title": entry["Title"][0], "Poem": entry["Poem"][0], "Poet": entry["Poet"][0], "Tags": entry["Tags"][0]}
    return poem

def format_entry_2(entry: pandas.Series):
    poem = {"Title": entry["Title"], "Poem": entry["Poem"], "Poet": entry["Poet"], "Tags": entry["Tags"]}
    return poem

def format_entries(entries: pandas.DataFrame):
    poems = []
    if entries.count(0)["Title"] > 1:
        poems = (entries.apply(format_entry_2, axis = 1))
        return (poems.values).tolist()
    else:
        return format_entry(entries)
    
def format_sqlauth(authors: list[str]):
    auth = "(Poet LIKE \"%"
    auth += "%\" OR Poet LIKE \"%".join(authors)
    auth += "%\") "

def format_sqlkey(keywords: list[str]):
    key += "(Tags LIKE \"%"
    key += "%\" OR Tags LIKE \"%".join(keywords)
    key += "\"%)"

def format_sqltags(tags: list[str]):
    tag += "(Tags LIKE \"%"
    tag += "%\" OR Tags LIKE \"%".join(tags)
    tag += "\"%) "