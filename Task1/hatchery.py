from fish import Fish
from technician import Technician
from supplier import Supplier
from warehouse import Warehouse

class Hatchery:
    """
    Hatchery class contains attributes and associated functions about the supplies, cash status, and number of technicians.
    """
    def __init__(self, cash = 10000):
        """
        Initializing the cash balance of £10,000 at the beginning.
        """
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
            Warehouse("fertilizer", 20, 10, 0.4, 0.1),
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
                        return f"do not have enough labour to maintain the amount of fish required" # P: put in the required labour variable and total labour here
                else:
                    return f"do not have enough supplies for the amount of fish required" # P: similarly put in the warehouse quantity required and total here
                    
            else:
                return f"Invalid fish type"
        
        def use_supplies(self, fertilizer, feed, salt):
            supplies = [fertilizer, feed, salt]
            for i, supply in enumerate(supplies):
                total_available = self.warehouse[i].main + self.warehouse[i].auxiliary
                if supply > total_available:
                    raise ValueError(f"Not enough {self.warehouse[i].supply} available")
                elif supply > self.warehouse[i].main:
                    self.warehouse[i].auxiliary -= supply - self.warehouse[i].main
                    self.warehouse[i].main = 0
                else:
                    self.warehouse[i].main -= supply

        def apply_depreciation(self):
            for w in self.warehouse:
                w.deprecate()
            return "applied depreciation to the main and auxiliary warehouses"
        
        def pay_expenses(self):
            fixed_cost = 1500
            technician_cost = sum(tech.pay_perquarter() for tech in self.technicians)
            warehouse_cost = sum(w.warehouse_cost() for w in warehouse_cost)
            total_cost = fixed_cost + technician_cost + warehouse_cost

            if self.cash >= total_cost:
                self.cash -= total_cost
                return f"(paid {total_cost} pounds in expenses)" # P: add remaining cash to output as well
            else:
                return f"(not enough cash to pay expenses)" # P: add required cash and cuurent cash here as well
        
        def restock(self, supplier_name):
            # initialize supplier variable
            supplier = None
            # find the supplier using the supplier name
            for s in self.suppliers:
                if s.name == supplier_name:
                    supplier = s
                break
            if supplier is None:
                print("No matching supplier is found")
                return None
                
            # initialize the cost of restocking
            restock_cost = 0

            # calculate the amount of each stock to be refilled and the cost for them.
            for w in self.warehouse:
                main_need = max(0, w.max_capacity - w.main) # P: the max capacity function here returns the capacity of main + aux so we cant use that here, better to add variable in the warehouse class to hold the max capacity for that warehouse
                aux_need = max(0, w.max_capacity - w.auxiliary) # P: ditto as above
                if w.supply == "fertilizer":
                    cost = (main_need + aux_need) * supplier.fertilizer_rate
                elif w.supply == "feed":
                    cost = (main_need + aux_need) * supplier.feed_rate
                elif w.supply == "salt":
                    cost = (main_need + aux_need) * supplier.salt_rate
                else:
                    cost = 0
                
                restock_cost += cost

                # update warehouse stock levels after restocking
                if main_need > 0:
                    w.main += main_need
                if aux_need > 0:
                    w.auxiliary += aux_need
            
            if self.cash >= restock_cost:
                self.cash -= restock_cost
                return f"supplies are restocked from {supplier.name} for £{total_cost}"
            else:
                return f"Not enough cash to restock supplies" # A: add required and total cash
            
        


        def __str__(self):
            return f"{self.cash}\n{self.fish_types}\n{self.warehouse}\n{self.suppliers}"

hatch = Hatchery()
print(hatch)