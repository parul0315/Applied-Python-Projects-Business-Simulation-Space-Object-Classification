# uv24946_EMATM0048

# Fish Hatchery Management Simulation

## Description
The Fish Hatchery Management Simulation is a python based project that aims at creating a simulation for managing a fish hatchery. It involves various aspects that an owner of the hatchery has to look after while running the business such as the resources, fish types, labour, storage and financial management. It interacts with the user, asking for the input and running the management simulation accordingly.
The project consists of several classes that are interconnected, each representing a different aspect of the hatchery. Below are the classes created and the function that each of the class performs:

## Classes and their functions

### 1. Fish Class
The fish class represents the different types of fish in the hatchery. Each fish type has its attributes, its demand and the price.

Methods:
`__init__` intialized the fish attributes

Attributes:
`name` - name of the fish
`fertilizer` - the amount of fertilizer needed for the fish
`feed` - the amount of feed needed for the fish
`salt` - the amount of salt needed for the fish
`time` - the time required to maintain each fish type
`price` - the price of each fish type
`demand` - the demand of each fish type

### 2. Technician
The technician class represents the workers that work in the hatchery. This class is used to manage the labour availability and the cost incured in each quarter.

Methods:
__init__

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
