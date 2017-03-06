#!/usr/bin/python3


import random


class urlaleat:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        randomURL = ("http://localhost:1234/aleat/" +
                     str(random.randint(1, 1000000)))
        htmlAnswer = ("<html><body><h1><a href=" + randomURL +
                      ">'Dame otra'</a></h1></body><html>")
        return ("200 OK", htmlAnswer)
