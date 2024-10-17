class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources",
        "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research"
    ]

    def __init__(self, name="Unknown", job="Unemployed"):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
            self._job = "Unemployed"

    def talk(self):
        print("Hello World!")  # Ensure "World" is capitalized

    def walk(self):
        print("The person is walking.")
