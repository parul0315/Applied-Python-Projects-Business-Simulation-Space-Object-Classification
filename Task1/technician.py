class Technician:
    """ 
    Class to define the technician that work in the hatchery
    Represents the technicians that maintains the fish and sells them. The attributes of the technician
    includes their labour weeks, weekly pay and the speciality(if any).
    """
    def __init__(self, name, specialty, ratepw = 500, labour_weeks = 9):
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