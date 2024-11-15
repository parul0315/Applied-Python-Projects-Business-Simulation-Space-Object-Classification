from fish import Fish
from technician import Technician
from supplier import Supplier
from warehouse import Warehouse

class Hatchery:
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
        self.warehouse = [
            Warehouse("fertilizers", 20, 10, 0.4, 0.1),
            Warehouse("feed", 400, 200, 0.1, 1),
            Warehouse("salt", 200, 100, 0.1, 1)
        ]
        self.suppliers = [
            Supplier("Slippery Lakes", 0.30, 0.10, 0.05),
            Supplier("Scaly Wholesaler", 0.20, 0.40, 0.25)
        ]

        def add_technician(self, name, quarter, specialty=None):
            if len(self.technicians) < 5:
                new_technician = Technician(name, specialty=specialty)
                self.technicians.append(new_technician)
                print("Hired {self.technician[-1].name}, weekly rate = 500, for quarter {quarter}")
                return True
            return "We already have the max amount of Technicians"

        def remove_technician(self):
            if len(self.technicians) < 0:
                print("Let go of {self.technician[-1].name}")
                self.technicians.pop()
            return "No technicians available to let go"
        
        def sell_fish(self, fish_type, quantity):
            if fish_type in self.fish_types:
                fish = self.fish_types[fish_type]
            
                # Limit the quantity to the demand if it exceeds
                actual_quantity = min(quantity, fish.demand)
                total_fertilizer = fish.fertilizer * quantity
                total_feed = fish.feed * quantity
                total_salt = fish.salt * quantity

                if (self.warehouse[0].main + self.warehouse[0].auxiliary >= total_fertilizer and
                    self.warehouse[1].main + self.warehouse[1].auxiliary >= total_feed and 
                    self.warehouse[2].main + self.warehouse[2].auxiliary >= total_salt):

                    #check if we have enough labour
                    total_time = len(self.technicians) * 9 * 7
                    required_labour = fish.time * quantity
                    if total_time >= required_labour:
                        self.cash += fish.price * quantity
                        self.use_supplies(total_fertilizer, total_feed, total_salt)
                        return f"Sold {quantity} {fish_type} for {fish.price * quantity} pounds"
                    else:
                        return f"do not have enough labour to maintain the amount of fish required"
                else:
                    return f"do not have enough supplies for the amount of fish required"
                    
            else:
                return f"Invalid fish type"
        
        

        def __str__(self):
            return f"{self.cash}\n{self.fish_types}\n{self.warehouse}\n{self.suppliers}"

hatch = Hatchery()
print(hatch)