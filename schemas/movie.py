def movieEntity(item) -> dict:
    return {
        "popularity": item["popularity"],
        "title": item["title"],
        "genres": item["genres"]
    }

def moviesEntity(entity) -> list:
    result = [movieEntity(item)for item in entity]
    return result
