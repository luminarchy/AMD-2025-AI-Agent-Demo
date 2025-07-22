import numpy as np
import pandas




def format_list(list: pandas.DataFrame):
    result = np.concatenate(list.values).tolist()
    return result


def format_entry(entry: pandas.DataFrame, parameters):
    poem = dict()
    for parameter in parameters:
        poem[parameter] = entry[parameter][0]
    return poem

def format_entry_2(entry: pandas.Series, parameters: list[str]):
    poem = dict()
    for parameter in parameters:
        poem[parameter] = entry[parameter]
    return poem

def format_entries(entries: pandas.DataFrame, parameters: list[str]):
    poems = []
    formating = lambda x : format_entry_2(x, parameters)
    if entries.count(0)[parameters[0]] > 1:
        poems = (entries.apply(formating, axis = 1))
        return (poems.values).tolist()
    else:
        return format_entry(entries, parameters)
    
