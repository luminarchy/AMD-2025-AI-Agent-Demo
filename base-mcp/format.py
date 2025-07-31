import numpy as np
import pandas




def format_list(list: pandas.DataFrame):
    """Formats a dataframe into a python list
        list: dataframe containing entries with a single value
        returns a list """
    result = np.concatenate(list.values).tolist()
    return result


def format_entry(entry: pandas.DataFrame, parameters):
    """Formats a dataframe entry into a python dictionary
        entry: a dataframe with one singular entry with multiple values
        returns a dict """
    poem = dict()
    for parameter in parameters: # using custom parameter names
        poem[parameter] = entry[parameter][0]
    return poem

def format_entry_2(entry: pandas.Series, parameters: list[str]):
    """Formats a series entry into a python dictionary
        entry: a series with one singular entry with multiple values
        returns a dict """
    poem = dict()
    for parameter in parameters: 
        poem[parameter] = entry[parameter]
    return poem

def format_entries(entries: pandas.DataFrame, parameters: list[str]):
    """Formats a dataframe with into python dictionaries
        entry: a dataframe with some number of entries with multiple values
        returns a list of dictionaries """
    poems = []
    formating = lambda x : format_entry_2(x, parameters)
    if entries.count(0)[parameters[0]] > 1:
        poems = (entries.apply(formating, axis = 1))
        return (poems.values).tolist()
    else:
        return format_entry(entries, parameters)
    
