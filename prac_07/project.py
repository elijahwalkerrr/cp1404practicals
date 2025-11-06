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

    def __lt__(self,other):
        """ Determines if project is older or younger than another """
        return self.start_date < other.start_date


    def update(self):
        """ Changes update status to new float and priority to new int"""
        print(f"Updating project: {self.name}")
        new_completion = input("New Percentage: ")
        new_priority = input("New Priority: ")

        if new_completion.strip():
            self.completion = float(new_completion)
        if new_priority.strip():
            self.priority = int(new_priority)


