#!/usr/bin/env python3
from outputPrinter import OutputPrinter
from sqlConnector import SQLConnector

printer = OutputPrinter()


class SQLAnalyzer:
    def topArticles(self):
        connector = SQLConnector()
        results = connector.fetchData("select articles.title, "
                                      "extracted_paths.views from articles "
                                      "join extracted_paths "
                                      "on articles.slug = "
                                      "extracted_paths.extracted_name limit 3")
        printer.printViews("1. Most popular articles:", results)
        connector.closeConnection()

    def topAuthors(self):
        connector = SQLConnector()
        results = connector.fetchData("select authors_titles_slugs.name, "
                                      "sum(extracted_paths.views) as summary "
                                      "from authors_titles_slugs "
                                      "join extracted_paths "
                                      "on extracted_paths.extracted_name = "
                                      "authors_titles_slugs.slug group by "
                                      "authors_titles_slugs.name order by "
                                      "summary desc")
        printer.printViews("2. Most popular authors:", results)
        connector.closeConnection()

    def reportFailedRequests(self):
        connector = SQLConnector()
        results = connector.fetchData("select date, round(percentage,2) "
                                      "from failure_percentage where "
                                      "failure_percentage.percentage > 1.0")
        printer.printFailedRequests("3. The day with high error date "
                                    "(higher than 1%):", results)
        connector.closeConnection()
