from hatchery import Hatchery

def main():
    """
    The number of quarters is taken as an input from the user. The input takes an int value, and prompts the user
    to enter an int value and gives an error when the user gives an negative value or an invalid data type value.
    Param: str (prompt)
    return: int
    """

    # initializing the hatchery 
    hatchery = Hatchery()
    
    while True:
        try:
            quarter = int(input(">>> Enter the number of quarters for the simulation: "))
            if quarter > 0:
                break
            print("Number of quarters must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    """
    The for loop starts the simulation for the quarters given by the user. 
    """

    for q in range(1, quarter + 1):
        print("\n================================")
        print(f"====== SIMULATING quarter {q} ======")
        print("================================")

    
        """
        Once we have started the simulation for the first quarter, the next input taken by the user is the number of technicians to hire.
        The input takes an int value and shows error if the value given is invalid.
        """
        while True:
            try:
                no_technician = int(input("To add enter positive, to remove enter negative, no change enter 0.\n>>> Enter number of technicians: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        """
        The following loop is to add/remove the technician.
        The if statement here checks for the number of technician used and the for loop calls the methods 'add_technician' 
        and 'remove_technician' from the class Hatchery.
        Params for 'add_technician': name (str), quarter (int)
        """
        while True:
            try:
                if no_technician > 0:
                    for i in range(no_technician):
                        name = str(input(">>> Enter technician name: "))
                        if name.isnumeric() or not name:
                            raise ValueError 
                        if hatchery.add_technician(name, q):
                            continue
                        else:
                            print(f"{name} is already hired. Please enter a different name")
                    break
                elif no_technician < 0:
                    for i in range(abs(no_technician)):
                        hatchery.remove_technician()
                    break
                else:
                    print("\nNo new technicians are added.")
                    break
            except ValueError:
                print("Invalid input. Please enter a string value.")


        # initially the time_left will be the total labour time
        time_left = float(hatchery.calculate_labour())
        """
        The next for loop is used to sell the fishes from the hatchery. The method created for selling fish in Hatchery i.e. 'sell_fish is called here.
        """

        for fish_name, fish in hatchery.fish_types.items():
            sell = 0
            fish_time = hatchery.calculate_required_labour(fish.time, fish.demand)
            if time_left >= fish_time:
                sell = hatchery.sell_fish(fish_name, fish.demand, time_left)
                print(f"{fish.name}, demand {fish.demand}, sell {fish.demand}: {sell}")
                time_left -= fish_time
            else:
                time_left = 0
                print(f"{fish.name}, demand {fish.demand}, sell {fish.demand}: 0")
    

        # Pay expenses
        print(hatchery.pay_expenses())
        print(hatchery.apply_depreciation())

        # Restock supplies
        print("\nList of suppliers:")
        for s, supplier in enumerate(hatchery.suppliers, start=1):
            print(f" {s}. {supplier.name}")
        while True:
            try:
                vendor = int(input(">>> Enter number of vendor to purchase from: ")) - 1
                if 0 <= vendor < len(hatchery.suppliers):
                    vendor_select = hatchery.suppliers[vendor]
                    print(f"The supplier selected for restocking is: {vendor_select.name}")
                    print(hatchery.restock(vendor_select.name))
                    break
                print("Invalid vendor number. Please enter a valid number.")
            except ValueError:
                print("Invalid vendor input. Please enter a valid number.")
        
        # Display end-of-quarter state
        print(f"\nHatchery Cash Available: {hatchery.cash}")
        for warehouse in hatchery.warehouse:
            print(f" {warehouse.supply}, {warehouse.main} (capacity={warehouse.main_max_capacity})")
            print(f" {warehouse.supply}, {warehouse.auxiliary} (capacity={warehouse.aux_max_capacity})")
        print(" Technicians")
        for tech in hatchery.technicians:
            print(f" Technician {tech.name}, weekly rate={tech.ratepw}")
        
        # Check for bankruptcy
        bankruptcy_status = hatchery.bankrupt
        if bankruptcy_status:
            print(bankruptcy_status)
            break

        print(f"END OF QUARTER {q}")

    # Final state
    print("\n=== FINAL STATE ===")
    print(f"Cash: {hatchery.cash}")
    for warehouse in hatchery.warehouse:
        print(f" {warehouse.supply}, {warehouse.main} (capacity={warehouse.main_max_capacity})")
        print(f" {warehouse.supply}, {warehouse.auxiliary} (capacity={warehouse.aux_max_capacity})")
    print(" Technicians")
    for tech in hatchery.technicians:
        print(f" Technician {tech.name}, weekly rate={tech.ratepw}")

if __name__ == "__main__":
    main()
