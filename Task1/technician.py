class Technician:
    """ 
    Class to define the technician that work in the hatchery
    Represents the technicians that maintains the fish and sells them. The attributes of the technician
    includes their labour weeks, weekly pay and the speciality(if any).
    """
    def __init__(self, name, ratepw = 500, specialty = None, labour_weeks = 9):
        """
        initializes a technician in the hatchery.

        Parameters:
        name (str) - the name of the technician
        ratepw (int) - the weekly pay of the technician which is £500
        specialty (str) - the fish type in which the technician specializes in (by default it is none)
        labour_weeks (int) - the number of weeks that the technician works for (by default it is 9)
        """
        self.name = name    #the name of each technician
        self.ratepw = ratepw  # weekly pay for the quarter
        self.specialty = specialty  # technician specialises in fish type (if any)
        self.labour_weeks = labour_weeks    #number of weeks that the technician works for

    def pay_perquarter(self):
        """
        calculates the total pay of the technician per quarter.

        Parameters: None
        Returns:
        int - the total amount of pay the technician get in one quarter
        """
        return self.ratepw * 12  #total pay of the technician per quarter 

    def maintain_fish(self, fish_type, quantity):
        """
        calculates the adjusted maintenance time required by the technician for the fish type they specialises in.

        Parameters:
        fish_type (Fish) - the number of weeks required to maintain a fish
        quantity (int) - the number of fishes of the type to be maintained
        Returns:
        maintenance_time (float) - the maintenance time returned is adjusted and is now reduced to 2/3rd of its original time
        """
        maintenance_time = quantity * fish_type.time    #base time it takes to maintain a fish
        if self.specialty == fish_type.name:
            #the base time is reduced to 2/3 of the original time required if the technician specialised in that fish
            maintenance_time *= 2/3     
        return maintenance_time     #the adjusted maintenance time for the fish