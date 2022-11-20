import json


class Content:
    question1 = {"Concert": 1, "Restaurant": 2, "Community event": 3,
                 "Activity": 4, "Surprise me!": 5}
    question2 = {"Chill": 1, "Hype": 2, "Social": 3,
                 "Just looking to have a good time": 4}
    question3 = {"Solo": 1, "Two": 2, "Three": 3, "Four or more": 4}
    question4 = {"FREE": 1, "Just a bit": 2, "A moderate amount": 3,
                 "I'm trying to splurge": 4, "Money is no object!": 5}
    answers = [0, 0, 0, 0]

    def __init__(self, answers = [0, 0, 0, 0]):
        self.answers = answers

    def add_criteria(self, question, criteria):
        if question == "question1":
            self.answers[0] = self.question1[criteria]
        elif question == "question2":
            self.answers[1]= self.question2[criteria]
        elif question == "question3":
            self.answers[2] = self.question3[criteria]
        elif question == "question4":
            self.answers[3] = self.question4[criteria]

    def isEmpty(self):
        for answer in self.answers:
            if answer != 0:
                return False
        return True

