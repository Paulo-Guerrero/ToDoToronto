class Content:
    def __init__(self):
        self.criteria1 = None
        self.criteria2 = None
        self.criteria3 = None
        self.criteriaMapping = {"question1": self.criteria1,
                                "question2": self.criteria2,
                                "question3": self.criteria3}

    def add_criteria(self, question, criteria):
        if question == "question1":
            self.criteria1 = criteria
        elif question == "question2":
            self.criteria2 = criteria
        elif question == "question3":
            self.criteria3 = criteria