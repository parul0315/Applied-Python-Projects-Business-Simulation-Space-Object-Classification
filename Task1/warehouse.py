import math
class Warehouse:
    """
    The warehouse class represents supplies in the main and auxiliary storage space, along with the per quarter depreciation and costs.
    """
    def __init__(self, supply, main, auxiliary, depreciation, costs):
        """
        Initializes the warehouse with the requires attributes.

        Parameters:
        supply (str) - the type of supply (i.e. fertilizer, feed, salt)
        main (int) - the amount of supply stored in the main warehouse
        auxiliary (int) - the amount of supply stored in the auxiliary warehouse
        depreciation (float) - the depreciation per quarter for the supply
        costs (float) - cost of the storage space per unit for the supply
        """
        self.supply = supply    #the type of supply
        self.main = main    #the amount of supply in main warehouse
        self.auxiliary = auxiliary  #the amount of supply in auxiliary warehouse
        self.depreciation = depreciation    #the depreciation per quarter
        self.costs = costs  #the cost of storage space
        # added variables for main_max_capacity and aux_max_capacity for using in hatchery
        self.main_max_capacity = main   #maximum capacity of main warehouse for the specific supply
        self.aux_max_capacity = auxiliary   #maximum capacity of auxiliary warehouse for the specific supply

    def deprecate(self):
        """
        calculates the amount of supply left in each warehouse, after applying depreciation to it.
        the new amount calculated are rounded off to the nearest integer.
        """
        self.main = math.ceil(self.main - (self.main * self.depreciation))
        self.auxiliary  = math.ceil(self.auxiliary - (self.auxiliary * self.depreciation))

    def warehouse_cost(self):
        """
        calculates the total storage cost of the warehouses that is incured during a quarter.
        Returns: 
        float - the total storage cost for each supply
        """
        return (self.main + self.auxiliary) * self.costs
        
    def __str__(self):
        return f"{self.supply} \n{self.main} \n{self.auxiliary}"
