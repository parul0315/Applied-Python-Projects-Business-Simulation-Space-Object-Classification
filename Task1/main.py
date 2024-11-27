#Name - Parul Nagar
#Section - Data Science MSc
#Description - The program defines the main function, that is the entry point of the hatchery simulation. It allows users to
#manage the different operations in the hatchery throughout the number of quarters that the function is running for.

from hatchery import Hatchery

def main():
    """
    The main function performs the simulation of the hatchery management. 
    It handles all the aspects of running the business such as hiring/removing technicians, 
    selling fish, restocking supplies, and checking for bankruptcy etc. 

    The main function performs the following steps:
    1. Initializes the hatchery using the Hatchery() class
    2. Prompts the user to enter the number of quarters for the simulation
    3. The function manages the these operations for each of the quarter:
        - prompts user to add/remove the technicians
        - selling fish based on the demand and availability of the labour and supplies
        - paying the expenses incured throughout the quarter
        - prompts the user to choose a supplier and restocking supplies 
        - checking for bankruptcy
    4. Displays the final state of the hatchery at the end of the simulation

    Parameters: None
    Raises:
    ValueError - for invalid inputs such as null value, invalid integer values, non-string names

    Returns: None
    """

    # initializing the hatchery 
    hatchery = Hatchery()
    
    while True:
        # get the number of quarters from the user
        try:
            quarter = int(input(">>> Enter the number of quarters for the simulation: "))
            if quarter > 0:
                break
            print("Number of quarters must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # loop for starting the simulation and iterating over each quarter 
    for q in range(1, quarter + 1):
        print("\n================================")
        print(f"====== SIMULATING quarter {q} ======")
        print("================================")
        
        while True:
            # getting the number of technicians to add/remove
            try:
                no_technician = int(input("\nTo add enter positive, to remove enter negative, no change enter 0.\
                                          \n>>> Enter number of technicians: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        
        while True:
            try:
                if no_technician > 0:
                    if len(hatchery.technicians) + no_technician > 5:
                        raise ValueError("Cannot hire more than 5 technicians in total.")
                    #adding the technicians
                    for i in range(no_technician):
                        name = str(input("\n>>> Enter technician name: "))
                        if name.isnumeric() or not name:
                            raise ValueError("Invalid input. Please enter a string value.")    #ValueError for non string values
                        
                        specialty = hatchery.prompt_specialty()

                        if hatchery.add_technician(name, q, specialty=specialty):
                            continue
                        else:
                            print(f"\n{name} is already hired. Please enter a different name")
                    break

                elif no_technician < 0:
                    #removing the technicians
                    for i in range(abs(no_technician)):
                        hatchery.remove_technician()
                    break
                else:
                    # no change in the number of technicians
                    print("\nNo new technicians are added.")
                    break
            except ValueError as ve:
                print(ve)


        # initially the time_left will be the total labour time
        time_left = float(hatchery.calculate_labour())
       
        # selling the fish
        for fish_name, fish in hatchery.fish_types.items():
            sell = 0
            fish_time = hatchery.calculate_required_labour(fish.time, fish.demand)

            is_specialized = any(t.specialty ==  fish.name for t in hatchery.technicians)

            if is_specialized:
                fish_time *= 2/3

            #checking if the labour weeks available 
            if time_left >= fish_time:  
                sell = hatchery.sell_fish(fish_name, fish.demand, time_left)
                print(f"\n{fish.name}, demand {fish.demand}, sell {fish.demand}: {sell}")
                #the labour weeks used for the fish type is deduced from the time left once the fish is sold
                time_left -= fish_time

            # if the labour is insufficient, no more fish is sold
            else:
                time_left = 0
                print(f"\n{fish.name}, demand {fish.demand}, sell {fish.demand}: 0")
    

        # Pay expenses for the quarter
        print(hatchery.pay_expenses())

        #apply depreciation to the supplies
        print(hatchery.apply_depreciation())

        # Restock supplies from a specific supplier
        print("\nList of suppliers:")
        for s, supplier in enumerate(hatchery.suppliers, start=1):
            print(f" {s}. {supplier.name}")
        while True:
            try:
                vendor = int(input("\n>>> Enter number of vendor to purchase from: ")) - 1
                if 0 <= vendor < len(hatchery.suppliers):
                    vendor_select = hatchery.suppliers[vendor]
                    print(f"\nThe supplier selected for restocking is: {vendor_select.name}")
                    print(hatchery.restock(vendor_select.name))
                    break
                print("Invalid vendor number. Please enter a valid number.")
            except ValueError:
                print("Invalid vendor input. Please enter a valid number.")
        
        # display the end of quarter state 
        print(f"\nFin-tastic Hatchery, Cash Available: {hatchery.cash}")
        for warehouse in hatchery.warehouse:
            print(f" {warehouse.supply}, {warehouse.main} (capacity={warehouse.main_max_capacity})")
            print(f" {warehouse.supply}, {warehouse.auxiliary} (capacity={warehouse.aux_max_capacity})")
        print(" Technicians")
        for tech in hatchery.technicians:
            print(f" Technician {tech.name}, weekly rate={tech.ratepw}")
        
        # Check for bankruptcy 
        bankruptcy_status = hatchery.bankrupt

        #if bankruptcy is true, the hatchery is declared bankrupt and the simulation stops after that quarter
        if bankruptcy_status:
            print(bankruptcy_status)
            break

        print(f"END OF QUARTER {q}")

    # final state of the hatchery
    print("\n=== FINAL STATE ===")
    print(f"\nFin-Tastic Hatchery, Cash: {hatchery.cash}")     #the cash left at the end of the simulation
    for warehouse in hatchery.warehouse:
        print(f" {warehouse.supply}, {warehouse.main} (capacity={warehouse.main_max_capacity})")
        print(f" {warehouse.supply}, {warehouse.auxiliary} (capacity={warehouse.aux_max_capacity})")
    print("Technicians")
    for tech in hatchery.technicians:
        print(f" Technician {tech.name}, weekly rate={tech.ratepw}")

#running the function for the simulation
if __name__ == "__main__":
    main()
