import psycopg2

DB_CONNECTION_NAME = "dbname=news"
class SQLAnalyzer:
    def topArticles(self):
        db_connection = psycopg2.connect(DB_CONNECTION_NAME)
        cursor = db_connection.cursor()
        cursor.execute("select articles.title, extracted_paths.views from articles join extracted_paths on articles.slug = extracted_paths.extracted_name limit 3")
        results = cursor.fetchall()
        print(results)
        db_connection.close()

    def topAuthors(self):
        db_connection = psycopg2.connect(DB_CONNECTION_NAME)
        cursor = db_connection.cursor()
        cursor.execute("select authors_titles_slugs.name, sum(extracted_paths.views) as summary from authors_titles_slugs join extracted_paths on extracted_paths.extracted_name = authors_titles_slugs.slug group by authors_titles_slugs.name order by summary desc")
        results = cursor.fetchall()
        print(results)
        db_connection.close()

    def reportFailedRequests(self):
        db_connection = psycopg2.connect(DB_CONNECTION_NAME)
        cursor = db_connection.cursor()
        cursor.execute("")
        results = cursor.fetchall()
        print(results)
        db_connection.close()
