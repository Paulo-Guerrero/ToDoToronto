class Content:
    question1 = {"Concert": 1, "Restaurant": 2, "Community event": 3, "Activity": 4, "Suprise me!": 5}
    question2 = {"Chill": 1, "Hype": 2, "Social": 3, "Just looking to have a good time": 4}
    question3 = {"Solo": 1, "Two": 2, "Three": 3, "Four or more": 4}
    question4 = {"FREE": 1, "Just a bit": 2, "A moderate amount": 3, "I'm trying to splurge": 4, "Money is no object!": 5}

    def __init__(self):
        self.criteria1 = None
        self.criteria2 = None
        self.criteria3 = None
        self.criteria4 = None

    def add_criteria(self, question, criteria):
        if question == "question1":
            self.criteria1 = self.question1[criteria]
        elif question == "question2":
            self.criteria2 = self.question2[criteria]
        elif question == "question3":
            self.criteria3 = self.question3[criteria]
        elif question == "question4":
            self.criteria4 = self.question4[criteria]

    def isEmpty(self):
        if self.criteria1 or self.criteria2 or self.criteria3 or self.criteria4:
            return False
        return True