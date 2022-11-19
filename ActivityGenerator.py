import collections
import random


class ActivityGenerator:
    activityTypeId = 0
    vibeId = 1
    groupSizeId = 2
    costId = 3

    def __init__(self, dbUtil):
        self.dbUtil = dbUtil
        self.activities = []

    def generate_activity(self, criteriaModel):
        results = self.dbUtil.executeQuery(
            "SELECT activityTypeId, vibeId, groupSizeId, "
            "costId, longName, link, activityDescription, "
            "eventDate FROM Activities")

        events = []

        criteria = [criteriaModel.criteria1, criteriaModel.criteria2,
                    criteriaModel.criteria3, criteriaModel.criteria4]
        if criteriaModel.isEmpty():
            randomNums = set()
            while len(randomNums) < min(len(results) - 1, 10):
                randomNums.add(random.randint(0, len(results) - 1))
            for num in randomNums:
                self.activities.append(results[num])
            print(randomNums)
            print(self.activities)
        else:
            weightDict = collections.defaultdict(list)
            weights = set()
            for event in results:
                tempWeight = 0
                for i in range(0, 4):
                    if criteria[i] and event[i]:
                        tempWeight += abs(criteria[i] - event[i])
                weightDict[tempWeight].append(event)
                weights.add(tempWeight)

            weights = list(weights)
            weights.sort()
            i = 0
            while len(events) < 10 and i < len(weights):
                events += weightDict[weights[i]]
                i += 1

            self.activities = events
