import math
class Warehouse:
    """
    The warehouse class represents the main and auxiliary storage space, along with the per quarter depreciation and costs.
    """
    def __init__(self,  supply, main, auxiliary, depreciation, costs):
        self.supply = supply
        self.main = main
        self.auxiliary = auxiliary
        self.depreciation = depreciation
        self.costs = costs
        # added variables for main_max_capacity and aux_max_capacity for using in hatchery
        self.main_max_capacity = main
        self.aux_max_capacity = auxiliary

    def max_capacity(self): # P: if we are not using this anywhere else can delete or update accordingly
        return self.main + self.auxiliary

    def deprecate(self):
        self.main = math.ceil(self.main - (self.main * self.depreciation))
        self.auxiliary  = math.ceil(self.auxiliary - (self.auxiliary * self.depreciation))

    def warehouse_cost(self):
        return (self.main + self.auxiliary) * self.costs
        
    def __str__(self):
        return f"{self.supply} \n{self.main} \n{self.auxiliary}"
