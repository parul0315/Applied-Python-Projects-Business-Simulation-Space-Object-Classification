# uv24946_EMATM0048

# Fish Hatchery Management Simulation

## Description
The Fish Hatchery Management Simulation is a python based project that aims at creating a simulation for managing a fish hatchery. It involves various aspects that an owner of the hatchery has to look after while running the business such as the resources, fish types, labour, storage and financial management. It interacts with the user, asking for the input and running the management simulation accordingly.
The project consists of several classes that are interconnected, each representing a different aspect of the hatchery. Below are the classes created and the function that each of the class performs:

## Classes and their functions

### 1. Fish Class
The fish class represents the core product of the hatchery i.e., the fish specied being harvestd and sold. Each fish type is defined by its attributes which are the supplies required by each type and maintenance time. The class also keeps track of the financial properties of the fish which are its price and demand. All these attributes are encapsulated in the fish class, providing a foundation which ensures that each fish's characteristics are applied consistently throughout the simulation.

Methods:<br/>
`__init__` intialized the fish attributes

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
`__init__` initialized a technician in the hatchery. Each technician had its own attributes like the weekly pay, number of working weeks and any specialization. 

`pay_perquarter` is used to calculate the pay of each technician per quarter. The technicians are paid for 12 weeks in each quarter. Therefore, the total amount is calculated accordingly.

`maintain_fish` is a method that is used in the extension of the project. Each technician specializes in one fish which reduced the maintainance time for that specific fish type to 2/3rd of its original time. Therefore, this method is used to calculate the new maintenance time for the fish type given that the technician specialises in that fish type.

### 3. Warehouse
The warehouse class represents the supplies that are stored in the warehouses, namely main and auxiliary warehouse. The supplies that are stored are fertilizer, feed and salt respectively. This class ensures encapsulation of all the supplies and their maximum limit in each warehouse, accounts for the depreciation of the supplies and calculates the warehouse storage costs. All these factors offers a more realistic approach to the management of the hatchery, prompting the user to manage the resources and plan accordingly.

Attributes:<br/>
`supply` - the type of supply (i.e. fertilizer, feed, salt)<br/>
`main` - the amount of supply stored in the main warehouse<br/>
`auxiliary` - the amount of supply stored in the auxiliary warehouse<br/>
`depreciation` - the depreciation per quarter for the supply<br/>
`costs` - cost of the storage space per unit for the supply<br/>

Methods:<br/>
`__init__` initialized a supply type in the warehouses, its depreciation rate and cost for the warehouse storage per unit.

`deprecate` applies the depreciation to the unused supplies by the end of the quarter. It subtracts the depreciated amount from the supplies amount that is in the warehouse. 

`warehouse_cost` calculates the cost incured through the storage space taken up by the supplies in the warehouses. This method calculates the total cost for each supply from both the main and the auxiliary warehouses. 

### 4. Supplier
The supplier class represents the supplier from which the hatchery restocks its supplies. Each supplier has different rates for each of the supplies, and the user is prompted to make the decision based on the cost efficiency for the hatchery. This class serves as a place to store all the pricing information of the supplies.

Methods:<br/>
`__init__` initialized a supplier with the required attributes, which are their name and rates provided for each supply.

Attributes:<br/>
`name` - the name of the supplier<br/>
`fertilizer_rate` - the rate for the fertilizer by the supplier<br/>
`feed_rate` - the rate for the feed by the supplier<br/>
`salt_rate` - the rate for the salt by the supplier<br/>









The flow of the simulation can be described through the following flowchart:
Start simulation -> Set number of quarters -> Add/remove technician -> Sell fish -> Pay expenses -> Restock supplies -> End of quarter status -> Check for bankrupcy -> End simulation

From this flowchart, we get a better understanding of all the classes and the methods we need to create in them respectively.

I created the 5 separate files for each of the classes I created.
fish.py
I started by creating the fish class - in which I initialized the class with the required attributes. The information provided regarding the fish was the name, fertilizer, feed, salt, time and in a different table we were provided with the demand and price of the fish quarterly. Since there are all static values and are related to the fish, I decided to add them in the __init__ function and initialize them. By doing so, this class made it easier to call all the fish related attributes since they are all contained in one class.

technician.py
The next class created is Technician. This particular class defines the technicians that work in the hatchery. The technicians have names, the rate of their labour per week which is £500 per week. The labour weeks provided by the technician is 9 weeks. The point to note is that even tho the technicians work for 9 weeks, the pay is given for the entire quarter which is 12 weeks. Once we initialized the main attributes of the technicians, I created 2 methods namely 'pay_perquarter()' and 'maintain_fish'. The 'pay_perquarter()' is a method used to calculate the total pay of the technician in each quarter. The 'maintain_fish' is a method created for calculating the maintainance time taken by the technician in a fish that they specialize in. Since the maintainance time is reduced by 2/3rd of its original value if a technician specialise in that specific fish, this method is important for extending the code at a later stage.

supplier.py
The supplier class contained the 
