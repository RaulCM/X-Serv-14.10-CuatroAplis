#!/usr/bin/python3


class hola:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>Hola</h1></body></html>")


class adios:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>Adios</h1></body></html>")
