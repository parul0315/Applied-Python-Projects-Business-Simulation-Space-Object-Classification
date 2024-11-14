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

    def deprecate(self):
        self.main = math.ceil(self.main - (self.main * self.depreciation))
        self.auxiliary  = math.ceil(self.auxiliary - (self.auxiliary * self.depreciation))

    def warehouse_cost(self):
        return (self.main + self.auxiliary) * self.costs
        
    def __str__(self):
        return f"{self.supply} \n{self.main} \n{self.auxiliary}"


# warehouse = [
#     ("fertilizers", 20, 10, 0.4, 0.1),
#     ("feed", 400, 200, 0.1, 1),
#     ("salt", 200, 100, 0.1, 1)
# ]
