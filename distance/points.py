from parser.value_objects.router import Router


class Points:
    def __init__(self, source: Router, destination: Router):
        self.source = source
        self.destination = destination
