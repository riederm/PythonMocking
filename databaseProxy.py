import random

import random

class Part:
    """
    A class representing a part with its attributes.
    """

    def __init__(self, part_id, name, weight, price):
        self.id = part_id
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"Part(id={self.id}, name='{self.name}', weight={self.weight}, price={self.price})"

class DatabaseProxy:
    """
    A proxy class for a database.
    This class generates random part information by ID.
    """
    def read_part_information(self, part_id):
        """
        Generates random part information.

        Args:
            part_id (int): The ID of the part to retrieve.

        Returns:
            dict: An object containing part information (id, name, weight, price).
        """
        # Generate random part information
        part_info = Part(
            part_id,
            f"Part-{random.randint(1000, 9999)}",
            round(random.uniform(0.5, 10.0), 2),
            round(random.uniform(5.0, 100.0), 2));
        
        return part_info