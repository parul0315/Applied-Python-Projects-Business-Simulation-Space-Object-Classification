class Technician:
    """ 
    Class to define the technician that work in the hatchery
    """
    def __init__(self, name, ratepw = 500, specialty = None, labour_weeks = 9):
        self.name = name
        self.ratepw = ratepw  # weekly pay
        self.specialty = specialty  # technician specialises in fish type (if any)
        self.labour_weeks = labour_weeks

    def pay_perquarter(self):
        return self.ratepw * 12  # total pay of the technician per quarter 
