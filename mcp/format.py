import numpy as np
import pandas



def format_list(list: pandas.DataFrame):
    result = np.concatenate(list.values).tolist()
    return result


def format_entry(entry: pandas.DataFrame):
    poem = {"Title": entry["Title"][0], "Poem": entry["Poem"][0], "Poet": entry["Poet"][0], "Tags": entry["Tags"][0]}
    return poem

def format_entries(entries: pandas.DataFrame):
    poems = []
    poems = format_list(entries.apply(format_entry, axis = 1))
    return poems