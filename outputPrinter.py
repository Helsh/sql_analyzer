#!/usr/bin/env python3
import datetime


class OutputPrinter:
    def printViews(self, message, results):
        print("\n"+message)
        for row in results:
            print(row[0]+" - "+str(row[1])+" views")

    def printFailedRequests(self, message, results):
        print("\n"+message)
        for row in results:
            requestDate = str(row[0])
            normalizedDate = datetime.datetime.strptime(
                             requestDate, "%Y-%m-%d").strftime("%B %d, %Y")
            print(normalizedDate+" - "+str(row[1])+"% errors")
