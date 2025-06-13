



def format_allauthors(results: dict[str, list]):
    return results.get("authors")

def format_author(results: list[dict]):
    poems = []
    for x in results:
        poems.append(x.get("title"))
    return poems
