class Project:

    def __init__(self, name ="", start_date="", priority = 0, cost_est = 0.0, completion = 0.0):
        """Initialises name (string), start date (string), priority (int), cost estimation
        and completion (floats) """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_est = cost_est
        self.completion = completion

    def __str__(self):
        """ Returns The name, start date, priority, cost estimate and completion status"""
        return (f"{self.name} starts {self.start_date} at priority {self.priority}, the cost estimate "
                f"is {self.cost_est} and is {self.completion}% completed")