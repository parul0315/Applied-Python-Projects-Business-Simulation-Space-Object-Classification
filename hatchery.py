from fish import Fish
from technician import Technician
from supplier import Supplier
from warehouse import Warehouse

class hatchery:
    """
    Hatchery class contains attributes and associated functions about the supplies, cash status, and number of technicians.
    """
    def __init__(self, cash = 10000):
        self.cash = cash
        self.technicians = []
        self.fish_types = {
            "Clef Fins": Fish("Clef Fins", 100.0, 12, 2, 2.0, 25, 250),
            "Timpani Snapper": Fish("Timpani Snapper", 50.0, 9, 2, 1.0, 10, 350),
            "Andalusian Brim": Fish("Andalusian Brim", 90.0, 6, 2, 0.5, 15, 250),
            "Plagal Cod": Fish("Plagal Cod", 100.0, 10, 2, 2.0, 20, 400),
            "Fugue Flounder": Fish("Fugue Flounder", 200.0, 12, 2, 2.5, 30, 550),
            "Modal Bass": Fish("Modal Bass", 300.0, 12, 6, 3.0, 50, 500)
        }
    