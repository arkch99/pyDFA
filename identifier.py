import keywords
import string


class ID(keywords.Matcher):
    qf = 1
    alpha_list = list(string.ascii_lowercase + string.ascii_uppercase + "_")  # alphabet list + "_"
    alnum_list = list(string.digits + string.ascii_lowercase + string.ascii_uppercase + "_")  # alphabet list +
    # number list + "_"

    stateTable = [
        {x: 1 for x in alpha_list},  # q0
        {y: 1 for y in alnum_list}  # q1
    ]

    def match(self, currentState, char):
        return super().nextState(currentState, char, self.stateTable)

class GenericIDMatcher:
    def IDMatch(self, word):
        matchObj = ID()
        state = 0

        for ch in word:
            state = matchObj.match(state, ch)  # go to new state
        if state == matchObj.qf:
            return True  # valid ID
        else:
            return False