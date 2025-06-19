import numpy as np
import pandas



def format_list(list: pandas.DataFrame):
    result = np.concatenate(list.values).tolist()
    return result


def format_entry(entry: pandas.DataFrame):
    poem = {"Title": entry[0][0], "Poem": entry[1][0], "Poet": entry[2][0], "Tags": entry[3][0]}
    return poem

def format_entries(entries: pandas.DataFrame):
    poems = []
    poems = format_list(entries.apply(format_entry, axis = 1))
    return poems