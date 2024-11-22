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
            "Clef Fins": Fish("Clef Fins", 0.1, 12, 2, 2.0, 25, 250),
            "Timpani Snapper": Fish("Timpani Snapper", 0.05, 9, 2, 1.0, 10, 350),
            "Andalusian Brim": Fish("Andalusian Brim", 0.09, 6, 2, 0.5, 15, 250),
            "Plagal Cod": Fish("Plagal Cod", 0.1, 10, 2, 2.0, 20, 400),
            "Fugue Flounder": Fish("Fugue Flounder", 0.2, 12, 2, 2.5, 30, 550),
            "Modal Bass": Fish("Modal Bass", 0.3, 12, 6, 3.0, 50, 500)
        }

        """
        Initializing the warehouse and the supplier values.
        """
        self.warehouse = [
            Warehouse("fertilizer", 20, 10, 0.4, 0.1),
            Warehouse("feed", 400, 200, 0.1, 1),
            Warehouse("salt", 200, 100, 0.1, 1)
        ]
        self.suppliers = [
            Supplier("Slippery Lakes", 0.30, 0.10, 0.05),
            Supplier("Scaly Wholesaler", 0.20, 0.40, 0.25)
        ]
        self.bankrupt = False

    def add_technician(self, name, quarter, specialty=None):
            if len(self.technicians) < 5:
                new_technician = Technician(name, specialty=specialty)
                self.technicians.append(new_technician)
                print(f"Hired {self.technicians[-1].name}, weekly rate = 500, for quarter {quarter}")
                return True
            else:
                return "We already have the max amount of Technicians"

    def remove_technician(self):
            if len(self.technicians) < 0:
                print(f"Let go of {self.technician[-1].name}")
                self.technicians.pop()
            else:
                return "No technicians available to let go"
        
    def sell_fish(self, fish_type, quantity):
            if fish_type in self.fish_types:
                fish = self.fish_types[fish_type]
            
                # Limit the quantity to the demand if it exceeds
                actual_quantity = min(quantity, fish.demand)
                total_fertilizer = fish.fertilizer * actual_quantity
                total_feed = fish.feed * actual_quantity
                total_salt = fish.salt * actual_quantity

                total_fertilizer_available = self.warehouse[0].main + self.warehouse[0].auxiliary
                total_feed_available = self.warehouse[1].main + self.warehouse[1].auxiliary
                total_salt_available = self.warehouse[2].main + self.warehouse[2].auxiliary

                if (total_fertilizer_available >= total_fertilizer and
                    total_feed_available >= total_feed and 
                    total_salt_available >= total_salt):

                    #check if we have enough labour
                    total_time = len(self.technicians) * 9 * 7
                    required_labour = fish.time * actual_quantity
                    print(f"Total labor available: {total_time} hours")
                    print(f"Labor required: {required_labour} hours")

                    if total_time >= required_labour:
                        self.cash += fish.price * actual_quantity
                        self.use_supplies(total_fertilizer, total_feed, total_salt)
                        return f"Sold {actual_quantity} {fish_type} for {fish.price * actual_quantity} pounds"
                    else:
                        return f"\nInsufficient labour: required {required_labour} weeks, available {total_time}"
                else:
                    return f"\nInsufficient ingredients: \nfertiliser need {total_fertilizer} storage {total_fertilizer_available} \nfeed need {total_feed} storage {total_feed_available} \nsalt need {total_salt} storage {total_salt_available}"
                    
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
            ware_cost = sum(w.warehouse_cost() for w in self.warehouse)
            total_cost = fixed_cost + technician_cost + ware_cost

            if self.cash >= total_cost:
                self.cash -= total_cost
                return f"(paid {total_cost} pounds in expenses with remaining balance: {self.cash})" # P: add remaining cash to output as well
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
                main_need = max(0, w.main_max_capacity - w.main) # P: the max capacity function here returns the capacity of main + aux so we cant use that here, better to add variable in the warehouse class to hold the max capacity for that warehouse
                aux_need = max(0, w.aux_max_capacity - w.auxiliary) # P: ditto as above
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
                return f"supplies are restocked from {supplier.name} for £{restock_cost}"
            else:
                self.bankrupt = True
                return f"Not enough cash to restock supplies. Required: {restock_cost} pounds, Current cash: {self.cash} pounds" # A: add required and total cash
            
    def bankrupcy(self):
            #to check for bankrupcy at each step of the simulation
            if self.cash <= 0:
                self.bankrupt = True
                return f"The hatchery is now bankrupt with the current cash: {self.cash} pounds"
            return None

    def __str__(self):
            return f"Cash: £{self.cash}\nFish Types: {self.fish_types}\nWarehouse: {self.warehouse}\nSuppliers: {self.suppliers}\nTechnicians: {self.technicians}\nBankrupt: {self.bankrupt}"

hatch = Hatchery()
print(hatch)