class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei",
        "Beagle", "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Unknown", breed="Mutt"):
        self.name = name  # This will trigger the name setter
        self.breed = breed  # This will trigger the breed setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"  # Default to "Unknown" if invalid

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in self.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Mutt"  # Default to "Mutt" if invalid

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")
