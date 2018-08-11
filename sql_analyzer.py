import psycopg2

DB_CONNECTION_NAME = "dbname=news"

def topArticles():
    db_connection = psycopg2.connect(DB_CONNECTION_NAME)
    cursor = db_connection.cursor()
    cursor.execute("SELECT articles.title, top_articles.views FROM articles JOIN top_articles ON LOWER(articles.title) LIKE '%' || top_articles.short_name || '%' order by views desc")
    results = cursor.fetchall()
    print(results)
    db_connection.close()

def topAuthors():
    db_connection = psycopg2.connect(DB_CONNECTION_NAME)
    cursor = db_connection.cursor()
    cursor.execute("")
    results = cursor.fetchall()
    print(results)
    db_connection.close()