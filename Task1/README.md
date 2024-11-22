# uv24946_EMATM0048

The purpose of this readme is to explain all the files I created throughout the project and the working of each of the classes within the files.
In task1, we are required to write a text-based Python program using object-oriented programming to simulate the quarterly actions of the shop owner. The program is made to interact with the user, asking for the input and running the simulation accordingly.

The flow of the simulation can be described through the following flowchart:
Start simulation -> Set number of quarters -> Add/remove technician -> Sell fish -> Pay expenses -> Restock supplies -> End of quarter status -> Check for bankrupcy -> End simulation

From this flowchart, we get a better understanding of all the classes and the methods we need to create in them respectively.

I created the 5 separate files for each of the classes I created. 
fish.py
I started by creating the fish class - in which I initialized the class with the required attributes. The information provided regarding the fish was the name, fertilizer, feed, salt, time and in a different table we were provided with the demand and price of the fish quarterly. Since there are all static values and are related to the fish, I decided to add them in the __init__ function and initialize them. By doing so, this class made it easier to call all the fish related attributes since they are all contained in one class.

technician.py
The next class created is Technician. This particular class defines the technicians that work in the hatchery. The technicians have names, the rate of their labour per week which is £500 per week. The labour weeks provided by the technician is 9 weeks. The point to note is that even tho the technicians work for 9 weeks, the pay is given for the entire quarter which is 12 weeks. Once we initialized the main attributes of the technicians, I created 2 methods namely 'pay_perquarter()' and 'maintain_fish'. The 'pay_perquarter()' is a method used to calculate the total pay of the technician in each quarter. The 'maintain_fish' is a method created for calculating the maintainance time taken by the technician in a fish that they specialize in. Since the maintainance time is reduced by 2/3rd of its original value if a technician specialise in that specific fish, this method is important for extending the code at a later stage.

supplier.py
