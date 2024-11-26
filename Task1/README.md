# uv24946_EMATM0048

# Fish Hatchery Management Simulation

## Description
The Fish Hatchery Management Simulation is a python based project that aims at creating a simulation for managing a fish hatchery. It involves various aspects that an owner of the hatchery has to look after while running the business such as the resources, fish types, labour, storage and financial management. It interacts with the user, asking for the input and running the management simulation accordingly.
The project consists of several classes that are interconnected, each representing a different aspect of the hatchery. Below are the classes created and the function that each of the class performs:

## Classes and their functions

### 1. Fish Class
The fish class represents the core product of the hatchery i.e., the fish specied being harvestd and sold. Each fish type is defined by its attributes which are the supplies required by each type and maintenance time. The class also keeps track of the financial properties of the fish which are its price and demand. All these attributes are encapsulated in the fish class, providing a foundation which ensures that each fish's characteristics are applied consistently throughout the simulation.

Methods:<br/>
`__init__()` intialized the fish attributes

Attributes:<br/>
`name` - name of the fish<br/>
`fertilizer` - the amount of fertilizer needed for the fish<br/>
`feed` - the amount of feed needed for the fish<br/>
`salt` - the amount of salt needed for the fish<br/>
`time` - the time required to maintain each fish type<br/>
`price` - the price of each fish type<br/>
`demand` - the demand of each fish type<br/>

### 2. Technician
The technician class represents the workers that work in the hatchery. Each technician is defined by their name, pay per week, and if they specialize in any fish type. This class is critical for managing all the labour hiring and their availability, cost incured and the specialization of the technician that can reduce the maintenance time for the fish, making the hatchery more productive and profitable.

Attributes:<br/>
`name` - the name of the technician<br/>
`ratepw` - the weekly pay of the technician which is £500<br/>
`specialty` - the fish type in which the technician specializes in<br/>
`labour_weeks` - the number of weeks that the technician works for

Methods:<br/>
`__init__()` initialized a technician in the hatchery. Each technician had its own attributes like the weekly pay, number of working weeks and any specialization. 

`pay_perquarter()` is used to calculate the pay of each technician per quarter. The technicians are paid for 12 weeks in each quarter. Therefore, the total amount is calculated accordingly.

`maintain_fish()` is a method that is used in the extension of the project. Each technician specializes in one fish which reduced the maintainance time for that specific fish type to 2/3rd of its original time. Therefore, this method is used to calculate the new maintenance time for the fish type given that the technician specialises in that fish type.

### 3. Warehouse
The warehouse class represents the supplies that are stored in the warehouses, namely main and auxiliary warehouse. The supplies that are stored are fertilizer, feed and salt respectively. This class ensures encapsulation of all the supplies and their maximum limit in each warehouse, accounts for the depreciation of the supplies and calculates the warehouse storage costs. All these factors offers a more realistic approach to the management of the hatchery, prompting the user to manage the resources and plan accordingly.

Attributes:<br/>
`supply` - the type of supply (i.e. fertilizer, feed, salt)<br/>
`main` - the amount of supply stored in the main warehouse<br/>
`auxiliary` - the amount of supply stored in the auxiliary warehouse<br/>
`depreciation` - the depreciation per quarter for the supply<br/>
`costs` - cost of the storage space per unit for the supply<br/>

Methods:<br/>
`__init__()` initialized a supply type in the warehouses, its depreciation rate and cost for the warehouse storage per unit.

`deprecate()` applies the depreciation to the unused supplies by the end of the quarter. It subtracts the depreciated amount from the supplies amount that is in the warehouse. 

`warehouse_cost()` calculates the cost incured through the storage space taken up by the supplies in the warehouses. This method calculates the total cost for each supply from both the main and the auxiliary warehouses. 

### 4. Supplier
The supplier class represents the supplier from which the hatchery restocks its supplies. Each supplier has different rates for each of the supplies, and the user is prompted to make the decision based on the cost efficiency for the hatchery. This class serves as a place to store all the pricing information of the supplies.

Methods:<br/>
`__init__()` initialized a supplier with the required attributes, which are their name and rates provided for each supply.

Attributes:<br/>
`name` - the name of the supplier<br/>
`fertilizer_rate` - the rate for the fertilizer by the supplier<br/>
`feed_rate` - the rate for the feed by the supplier<br/>
`salt_rate` - the rate for the salt by the supplier<br/>

### 4. Hatchery
The hatchery class works as the central hub of the simulation, encapsulating all the methods that are required for the hatchery management. It brings together all the other classes and uses their components to manage various tasks of the hatchery. It oversees the hiring of the technician, selling fish, using and restocking supplies, applying depreciation, paying expenses and checking for banrupcy at each step of the simulation. To understand how the hatchery is created the following flowchart is designed for a better understanding.<br/>
The flow of the simulation can be described through the following flowchart:<br/>

**Start simulation -> Set number of quarters -> Add/remove technician -> Sell fish -> Pay expenses -> Restock supplies ->Check for bankrupcy -> End of quarter status -> End simulation**<br/>

Each of the hatchery methods are created to do these specific tasks for the simulation. Rest of the classes created are called in the hatchery class, to initialize those values and use the attributes for creating methods.

Attributes:<br/>
`cash` - The current cash of the hatchery<br/>
`technicians` - the list of technicians working at the hatchery<br/>
`max_technicians` - the initialized value of the maximum number of technicians that can work at the hatchery per quarter<br/>
`fish_types` - dictionary of the fishes that are available at the hatchery<br/>
`warehouse` - list of supplies stored in warehouse<br/>
`suppliers` - list of suppliers for purchasing supplies to restock the warehouses<br/>
`bankrupt` - value to check if the hatchery has gone bankrupt<br/>

Methods:<br/>
`__init__()` initializes the cash balance of the hatchery at £10,000 at the start, the fish types, warehouse and suppliers.<br/>

`add_technician()` adds the technician to the list of technicians that are working at the hatchery for a given quarter. It ensures that no two technicians are given the same name, the number of technicians doesn't exceed 5 and returns a message that indicates the hiring of the technician.

`remove_technician()` removes the technician that the user select from the hatchery. It ensures that the hatchery always have atleast one technician working and removes the last hired technician from the list. It returns the message indicating whether the technician was removed or not.

`calculate_labour()` calculates the total labour that is available for a quarter (in weeks). The number of technician hired is multiplies by 9 since each technican works for 9 weeks in one quarter.

`calculate_required_labour()` calculates the required labour for a fish type (in weeks).

`check_supplies()` is created as an indicator for checking if the warehouse has enough supplies for harvesting a fish type. Its attributes involve all the supplies that are available and the supplies amount that is required for the fish type. It returns a simple bool value which is true if the conditions are met and is false given otherwise. This functions help encapsulate the checking process of the supplies which is essential for selling fish and can be called later while we sell fish.

`sell_fish()` is a method that checks for all the conditions that are required to sell a fish. Once all the conditions are met, it sells the required fish amount. It starts by selecting a fish type from the class Fish, then all the available supplies are accounted for. Next, we make sure that the quantity of fish being sold does not exceed the demand. The supplies and labour requirements are checked and then the required amount of fish is sold. The method uses if statements to check for each condition and displays the appropriate messages. It also ensures that the user inputs errors are handled.

`use_supplies()` removes the supplies that have been used for harvesting fish during the quarter. The supplies are removed from the warehouses, first from the main warehouse. Once the main warehouse is empty, the auxiliary warehouse supplies gets deducted.

`apply_depreciation()` applies depreciation to the supplies in main and auxiliary warehouse. The method `deprecate()` from Warehouse class is used.

`pay_expenses()` deduces the expenses incured during the quarter from the hatchery cash available. The total expense includes the fixed cost, technician payment and warehouse storage cost. If the total expenses are more than the cash available, the hatchery is declared bankrupt.

`restock_supplies()` replenishes the warehouse supplies from a specific supplier. The supplies needed in both the warehouses is calculated along with the costs for replenishing them. The restocking cost is then deduced from the hatchery cash, if the hatchery cash is less than the restocking cost - the hatchery is declated bankrupt.

`bankrupcy()` is a method that declares when the hatchery has gone bankrupt. The bankruptcy status is checked at every step during the simulation. Once the conditions for hatchery bankruptcy are met, the method `bankrupcy()`  is called.

### 5. Main
