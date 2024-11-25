from fish import Fish
from technician import Technician
from supplier import Supplier
from warehouse import Warehouse

class Hatchery:
    """
    Hatchery class contains attributes and associated functions about the supplies, cash status, and number of technicians.
    
    Attributes:
    cash(int) - The current cash of the hatchery
    technicians (list) - the list of technicians working at the hatchery
    max_technicians (int) - the initialized value of the maximum number of technicians that can work at the hatchery per quarter
    fish_types (dict) - dictionary of the fishes that are available at the hatchery
    warehouse (list) - list of supplies stored in warehouse
    suppliers (list) - list of suppliers for purchasing supplies to restock the warehouses
    bankrupt (bool) - value to check if the hatchery has gone bankrupt 
    """
    def __init__(self, cash = 10000):
        """
        Initializing the cash balance of £10,000, fish types, warehouse and suppliers at the beginning.
        """
        self.cash = cash
        self.technicians = []   #initializing a list to add technicians
        self.max_technicians = 5
        self.fish_types = {
            "Clef Fins": Fish("Clef Fins", 0.1, 12, 2, 2.0, 25, 250),
            "Timpani Snapper": Fish("Timpani Snapper", 0.05, 9, 2, 1.0, 10, 350),
            "Andalusian Brim": Fish("Andalusian Brim", 0.09, 6, 2, 0.5, 15, 250),
            "Plagal Cod": Fish("Plagal Cod", 0.1, 10, 2, 2.0, 20, 400),
            "Fugue Flounder": Fish("Fugue Flounder", 0.2, 12, 2, 2.5, 30, 550),
            "Modal Bass": Fish("Modal Bass", 0.3, 12, 6, 3.0, 50, 500)
        }
        #intializing the warehouse for supplies
        self.warehouse = [
            Warehouse("fertilizer", 20, 10, 0.4, 0.1),
            Warehouse("feed", 400, 200, 0.1, 1),
            Warehouse("salt", 200, 100, 0.1, 1)
        ]

        #initializing the suppliers for restocking
        self.suppliers = [
            Supplier("Slippery Lakes", 0.30, 0.10, 0.05),
            Supplier("Scaly Wholesaler", 0.20, 0.40, 0.25)
        ]
        
        self.bankrupt = False   #the hatchery is set to be not bankrupt at the start

    def add_technician(self, name, quarter, specialty=None):
        """
        adds the technicians to the hatchery.

        Parameters:
        name (str) - name of the technician
        quarter (int) - the quarter for which technician is being hired for
        specialty (str) - the fish type in which the technician specializes in (if any)

        Return:
        bool - it is true if the technician is added, false if otherwise
        """
        if len(self.technicians) < self.max_technicians:
            for techinician in self.technicians:
                    if techinician.name == name:    #checking if the name of the technician is being repeated
                        return False    # the name isn't added if the name is repeated
            new_technician = Technician(name, specialty=specialty)
            self.technicians.append(new_technician)     #the new technician is added into the list of technicians
            print(f"Hired {new_technician.name}, weekly rate = 500, for quarter {quarter}")
            return True
        else:
            return False
                 

    def remove_technician(self):
            """
            removes the technician from the hatchery

            Parameters: None
            Return: 
            str - a text is printed to indicate if the technician was let go or not
            """
            if len(self.technicians) > 0:
                print(f"Let go of {self.technicians[-1].name}")
                self.technicians.pop()     #the technician is removed from the list of technicians
            else:
                return "No technicians available to let go"
            
    def calculate_labour(self):
        """
        calculates the total labour weeks that are available in a quarter

        Returns: 
        total_time (int) - total number of weeks of labour available in a quarter
        """
         # Calculate totale labour available
        total_time = len(self.technicians) * 9    #each technician works for 9 weeks in a quarter
        return total_time
    
    def calculate_required_labour(self, fish_time, actual_quantity):
        """
        calculates the required labour for a fish type

        Parameters:
        fish_time - time required to maintain one fish of a specific type
        actual_quantity - the amount of fish that is to be sold
        Return:
        int - the required labour weeks to maintain and sell fish   
        """
        return (fish_time * actual_quantity)
    
    def check_supplies(
              self, 
              total_fertilizer_available, 
              total_fertilizer, 
              total_feed_available, 
              total_feed, 
              total_salt_available, 
              total_salt
              ):
        """
        checks if there are enough supplies to sell fish

        Parameters:
        total_fertilizer_available (float) - the fertilizer that is available in storage (including both warehouses)
        total_fertilizer (float) - fertilizer that is required
        total_feed_available (int) - feed that is available in storage
        total_feed (int) - feed that is required
        total_salt_available (int) - salt that is available in storage
        total_salt (int) - salt that is required

        Return:
        bool - True if all the conditions are met and there are enough supplies to sell the fish, false if otherwise.
        """
        
        if (total_fertilizer_available >= total_fertilizer and 
            total_feed_available >= total_feed and 
            total_salt_available >= total_salt):
            return True
        else:
            return False
         
         
    def check_labour(self, total_time, required_labour):
        """
        checks if there is enough labour for selling fish

        Parameters:
        total_time - time that is provided by the labour (in weeks)
        required_labour - time that is required to harvest fish (in weeks)
        Return:
        bool - True if the required labour is less than or equal to total time, false if otherwise
        """
        if (total_time >= required_labour):
            return True
        else:
            return False
        
    def sell_fish(self, fish_type, quantity, time_left):
            """
            Sells a specific type of fish if the supplies and labour are sufficient

            Parameters:
            fish_type (str) - the type of fish that is to be sold
            quantity (int) - the amount of fish to be sold
            time_left (int) - the available labour weeks

            Return:
            str - a text is printed to indicate if the amount of fish was sold or not.
            """
            if fish_type in self.fish_types:
                fish = self.fish_types[fish_type]
            
                # Calculate total available warehouse supplies
                total_fertilizer_available = self.warehouse[0].main + self.warehouse[0].auxiliary
                total_feed_available = self.warehouse[1].main + self.warehouse[1].auxiliary
                total_salt_available = self.warehouse[2].main + self.warehouse[2].auxiliary

                # Limit the quantity to the demand if it exceeds
                actual_quantity = min(quantity, fish.demand)
                total_fertilizer = fish.fertilizer * actual_quantity
                total_feed = fish.feed * actual_quantity
                total_salt = fish.salt * actual_quantity

                #check if we have enough labour
                required_labour = self.calculate_required_labour(fish.time, actual_quantity)
                print(f"Total labor available: {time_left} weeks")
                print(f"Labor required: {required_labour} weeks")
                
                supplies_checker = self.check_supplies(
                     total_fertilizer_available,
                     total_fertilizer,
                     total_feed_available,
                     total_feed,
                     total_salt_available,
                     total_salt
                )
                labour_checker = self.check_labour(time_left, required_labour)
                
                if  supplies_checker and labour_checker:
                    self.cash += fish.price * actual_quantity
                    self.use_supplies(total_fertilizer, total_feed, total_salt)
                    return f"Sold {actual_quantity} {fish_type} for {fish.price * actual_quantity} pounds"
                else:
                    if labour_checker and not supplies_checker:
                        return f"\n\nInsufficient ingredients: \
                        \nfertiliser need {total_fertilizer} storage {total_fertilizer_available} \
                        \nfeed need {total_feed} storage {total_feed_available} \
                        \nsalt need {total_salt} storage {total_salt_available}"
                    elif supplies_checker and not labour_checker:
                        return f"\n\nInsufficient labour: required {required_labour} weeks, available {time_left} weeks"
                    else: 
                        return f"\n\nInsufficient ingredients: \
                            \nfertiliser need {total_fertilizer} storage {total_fertilizer_available} \
                            \nfeed need {total_feed} storage {total_feed_available} \
                            \nsalt need {total_salt} storage {total_salt_available}\
                            \nInsufficient labour: required {required_labour} weeks, available {time_left}"
            else:
                return f"Invalid fish type"
        
    def use_supplies(self, fertilizer, feed, salt):
        """
        removes supplies from the warehouse that have been used to harvest the fish.

        Parameters:
        fertilizer (float): amount of fertilizer to use
        feed (float): amount of feed to use
        salt (float): amount of salt to use

        Raises:
        ValueError - if the supplies are not sufficient for the fish 
        """
        supplies = [fertilizer, feed, salt]
        for i, supply in enumerate(supplies):
            #calculates the total available supplies in main and auxiliary combined
            total_available = self.warehouse[i].main + self.warehouse[i].auxiliary
            if supply > total_available:
                raise ValueError(f"Not enough {self.warehouse[i].supply} available")
            elif supply > self.warehouse[i].main:
                #the supplies are taken from the auxiliary if the main warehouse doesn't have enough
                self.warehouse[i].auxiliary -= supply - self.warehouse[i].main
                self.warehouse[i].main = 0
            else:
                #deducts the supplies from the main warehouse
                self.warehouse[i].main -= supply

    def apply_depreciation(self):
        """
        applies the depreciation to the supplies in the main and auxiliary warehouse

        Return:
        str - text that displays that the depreciation is applied to the warehouses
        """
        for w in self.warehouse:
            w.deprecate()   #applied depreciation logic to the warehouses
        return "applied depreciation to the main and auxiliary warehouses"

    def pay_expenses(self):
        """
        deduces the expenses from the cash in the hatchery

        Return:
        str - a text that displays that the expenses are paid
        """
        fixed_cost = 1500   #fixed cost that needs to paid every quarter
        technician_cost = sum(tech.pay_perquarter() for tech in self.technicians)   #total cost that needs to be paid to the technicians
        ware_cost = sum(w.warehouse_cost() for w in self.warehouse) #storage cost of the warehouses combined
        total_cost = fixed_cost + technician_cost + ware_cost   #sum of all the costs for the quarter

        if self.cash >= total_cost:
            #deducts the total cost from the cash in the hatchery
            self.cash -= total_cost
            return f"\n(paid {total_cost} pounds in expenses with remaining balance: {self.cash})"
        else:
            #if the cash is less than the total cost, the hatchery goes bankrupt
            print(f"\n(not enough cash to pay expenses)")
            return self.bankruptcy()
                
                
        
    def restock(self, supplier_name):
        """
        restock the supplies in the warehouse from a specific supplier

        Parameter:
        supplier_name - the name of the supplier

        Return:
        str - a text that displays that the warehouses have been restocked
        """
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

        # calculate the amount of each stock to be refilled and the cost for them in both main and auxiliary respectively
        for w in self.warehouse:
            main_need = max(0, w.main_max_capacity - w.main) 
            aux_need = max(0, w.aux_max_capacity - w.auxiliary)
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
            #deduct the cost of restocking from the cash in hatchery
            self.cash -= restock_cost
            return f"supplies are restocked from {supplier.name} for £{restock_cost}"
        else:
            #if the supplies can't be restocked, the hatcery has gone bankrupt
            print(f"Not enough cash to restock supplies. Required: {restock_cost} pounds, Current cash: {self.cash} pounds")
            return self.bankruptcy()
            
    def bankruptcy(self):
        """
        declares that the hatchery has gone bankrupt

        Return:
        str - a text is displayed that shows the hatchery is bankrupt now
        """
        self.bankrupt = True
        return f"The hatchery is now bankrupt with the current cash: {self.cash} pounds"

    def __str__(self):
            return f"Cash: £{self.cash}\nFish Types: {self.fish_types}\
                \nWarehouse: {self.warehouse}\nSuppliers: {self.suppliers}\
                \nTechnicians: {self.technicians}\nBankrupt: {self.bankrupt}"
