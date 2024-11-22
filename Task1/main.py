from hatchery import Hatchery

def main():
    # initializing the hatchery
    hatchery = Hatchery()
    
    # Get the number of quarters
    while True:
        try:
            quarter = int(input(">>> Please enter number of quarters: "))
            if quarter > 0:
                break
            print("Number of quarters must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    for q in range(1, quarter + 1):
        print("================================")
        print(f"====== SIMULATING quarter {q} ======")
        print("================================")

        # Add/remove technicians
        while True:
            try:
                no_technician = int(input("To add enter positive, to remove enter negative, no change enter 0.\n>>> Enter number of technicians: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        if no_technician > 0:
            for _ in range(no_technician):
                name = input(">>> Enter technician name: ")
                hatchery.add_technician(name, quarter)
        elif no_technician < 0:
            for _ in range(abs(no_technician)):
                hatchery.remove_technician()

        # Fish sales
        for fish_name, fish in hatchery.fish_types.items():
            sell = hatchery.sell_fish(fish_name, fish.demand)
            print(f"{fish.name}, demand {fish.demand}, sell {fish.demand}: {sell}")

        # Pay expenses
        print(hatchery.pay_expenses())

        # Restock supplies
        print("List of suppliers:")
        for s, supplier in enumerate(hatchery.suppliers, start=1):
            print(f" {s}. {supplier.name}")
        while True:
            try:
                vendor = int(input(">>> Enter number of vendor to purchase from: ")) - 1
                if 0 <= vendor < len(hatchery.suppliers):
                    print(hatchery.restock(hatchery.suppliers[vendor].name))
                    break
                print("Invalid vendor number. Please enter a valid number.")
            except ValueError:
                print("Invalid vendor input. Please enter a valid number.")
        
        # Display end-of-quarter state
        print(f"Hatchery Cash Available: {hatchery.cash}")
        for warehouse in hatchery.warehouse:
            print(f" {warehouse.supply}, {warehouse.main} (capacity={warehouse.main_max_capacity})")
            print(f" {warehouse.supply}, {warehouse.auxiliary} (capacity={warehouse.aux_max_capacity})")
        print(" Technicians")
        for tech in hatchery.technicians:
            print(f" Technician {tech.name}, weekly rate={tech.ratepw}")
        
        # Check for bankruptcy
        bankruptcy_status = hatchery.bankrupcy()
        if bankruptcy_status:
            print(bankruptcy_status)
            break

        print(f"END OF QUARTER {quarter}")

    # Final state
    print("=== FINAL STATE ===")
    print(f"Cash: {hatchery.cash}")
    for warehouse in hatchery.warehouse:
        print(f" {warehouse.supply}, {warehouse.main} (capacity={warehouse.main_max_capacity})")
        print(f" {warehouse.supply}, {warehouse.auxiliary} (capacity={warehouse.aux_max_capacity})")
    print(" Technicians")
    for tech in hatchery.technicians:
        print(f" Technician {tech.name}, weekly rate={tech.ratepw}")

if __name__ == "__main__":
    main()
