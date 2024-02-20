from habanero import Crossref

def search_articles_by_title(title):
    cr = Crossref()
    article_results = cr.works(query=title)
    return article_results