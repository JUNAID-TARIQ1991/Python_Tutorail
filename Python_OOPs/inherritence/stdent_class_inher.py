class ScoreModificationError(Exception):
    pass


class GradeActivity:
    def __init__(self, score):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        raise ScoreModificationError("You can't modify score")

    def grade(self, score):
        if score > 80:
            return "A"
        elif score > 70:
            return "B"
        elif score > 60:
            return "C"
        elif score > 50:
            return "D"
        else:
            return "Fail"


class FinalExam(GradeActivity):
    def __init__(self, num_qs, missed_qs):
        self.__num_qs = num_qs
        self.__missed_qs = missed_qs

    @property
    def finalscore(self):
        moeqs = 100/self.__num_qs
        finalscore = 100-(moeqs*self.__missed_qs)
        return finalscore


junaid = FinalExam(10, 1)
print(junaid.grade(junaid.finalscore))

zohaib = GradeActivity(100)
print(zohaib.score)
