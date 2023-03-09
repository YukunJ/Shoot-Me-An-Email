"""
    Data structure for holding a lease listing
"""

class Lease:

    """
    combination of apartment name and unit is used as primary key
    """
    def __init__(self, apt_name: str, apt_unit: str, size: str="", price: str="", start_date: str=""):
        assert len(apt_name) > 0, "apartment name cannot be null"
        assert len(apt_unit) > 0, "apartment unit cannot be null"
        self.apt_name = apt_name
        self.apt_unit = apt_unit
        self.size = size
        self.price = price
        self.start_date = start_date

    def to_key(self) -> str:
        # generate the key in mem_tabale
        return self.apt_name + "@" + self.apt_unit

    def __str__(self) -> str:
        return f"Apartment {self.apt_name} Unit {self.apt_unit} of size {self.size} sq feet at price ${self.price} " \
               f"with lease start date {self.start_date}"