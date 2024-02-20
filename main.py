from crossref_search import search_articles_by_title
from display_results import display_all_article_dois, display_first_article_doi

def main():
    # Demander à l'utilisateur de saisir le nom de l'article
    article_title = input("Veuillez saisir le nom de l'article que vous souhaitez rechercher : ")

    # Effectuer la recherche d'articles en utilisant le titre saisi par l'utilisateur
    article_results = search_articles_by_title(article_title)

    # Afficher les DOI de tous les articles trouvés
    display_all_article_dois(article_results, article_title)

    # Afficher le DOI du premier article trouvé, s'il y en a
    display_first_article_doi(article_results, article_title)

if __name__ == "__main__":
    main()
