#!/usr/bin/python3


class sumador:

    def parse(self, request, rest):
        parsedReq = rest.split('/')[1:]
        return parsedReq

    def process(self, parsedRequest):
        try:
            operation = (str(parsedRequest[0]) + " + " +
                         str(parsedRequest[1]) + " = ")
            sumResult = str(int(parsedRequest[0]) + int(parsedRequest[1]))
        except IndexError:
            operation = "Introduzca los sumandos en la URL "
            operation += "como /suma/operando1/operando2."
            sumResult = ""
        except ValueError:
            operation = "Operación no realizada.\n"
            sumResult = "Sumandos incorrectos."
        finally:
            htmlAnswer = ("<html><h2>App id: /suma</h2><p>" +
                          operation + sumResult + "</p></html>")
            return ("200 OK", htmlAnswer)
