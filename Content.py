class Content:
    def __init__(self):
        self.criteria1 = None
        self.criteria2 = None
        self.criteria3 = None
        self.criteria4 = None

    def add_criteria(self, question, criteria):
        if question == "question1":
            self.criteria1 = criteria
        elif question == "question2":
            self.criteria2 = criteria
        elif question == "question3":
            self.criteria3 = criteria
        elif question == "question4":
            self.criteria4 = criteria
