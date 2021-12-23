import inspect
import pprint


class Names:
    def __init__(self):
        self.name = "Nata"


n = Names()

pprint.pprint(inspect.isclass(Names))