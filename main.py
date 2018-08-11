from sqlAnalyzer import SQLAnalyzer

def main():
    sql_analyzer = SQLAnalyzer()
    sql_analyzer.topArticles()
    sql_analyzer.topAuthors()
    sql_analyzer.reportFailedRequests()

if __name__ == "__main__":
    main()