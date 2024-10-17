class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei",
        "Beagle", "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Unknown", breed="Mutt"):
        # Validate name first
        self.name = name  # Use the setter to validate name
        # Only set breed if name is valid
        if isinstance(self._name, str) and 1 <= len(self._name) <= 25:
            self.breed = breed  # Use the setter to validate breed
        else:
            self.breed = "Mutt"  # Default value if name is invalid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"  # Default value if invalid

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in self.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Mutt"  # Default value if invalid

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")


