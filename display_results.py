def display_all_article_dois(article_results, title):
    if 'items' in article_results['message']:
        for item in article_results['message']['items']:
            article_doi = item['DOI']
            print(f"Le DOI de l'article '{title}' est : {article_doi}")
    else:
        print(f"Aucun DOI trouvé pour l'article '{title}'.")

def display_first_article_doi(article_results, title):
    if len(article_results['message']['items']) > 0:
        first_article = article_results['message']['items'][0]
        article_doi = first_article['DOI']
        print(f"Le DOI du premier article trouvé pour '{title}' est : {article_doi}")
    else:
        print(f"Aucun DOI trouvé pour l'article '{title}'.")
