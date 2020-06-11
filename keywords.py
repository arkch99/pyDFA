class Matcher:  # mainly reduces code size. Looks cool too
    qd = 999  # dead state

    def nextState(self, currentState, char, table):
        try:
            state = table[currentState][char]
        except(KeyError, IndexError):
            state = self.qd
        return state


class CKey(Matcher):
    qf = 12  # final state
    stateTable = [  # hash-table of states indexed by state number
        {"o": 1, "h": 8, "a": 10},  # q0
        {"n": 2},  # q1
        {"s": 3, "t": 4},  # q2
        {"t": qf},  # q3
        {"i": 5},  # q4
        {"n": 6},  # q5
        {"u": 7},  # q6
        {"e": qf},  # q7
        {"a": 9},  # q8
        {"r": qf},  # q9
        {"s": 11},  # q10
        {"e": qf}  # q11
    ]

    def match(self, currentState, char):  # NOTE: every class should have this exact function
        return super().nextState(currentState, char, self.stateTable)


class RKey(Matcher):
    qf = 10  # final state
    stateTable = [  # hash-table of states indexed by state number
        {"e": 1},  # q0
        {"t": 2, "g": 5},  # q1
        {"u": 3},  # q2
        {"r": 4},  # q3
        {"n": qf},  # q4
        {"i": 6},  # q5
        {"s": 7},  # q6
        {"t": 8},  # q7
        {"e": 9},  # q8
        {"r": qf},  # q9
    ]

    def match(self, currentState, char):
        return super().nextState(currentState, char, self.stateTable)


class DKey(Matcher):
    qf = 4  # final state
    stateTable = [  # hash table
        {"o": qf},  # q0
        {"b": 2},  # q1
        {"l": 3},  # q2
        {"e": qf},  # q3
        {"u": 1},  # qf
    ]

    def match(self, currentState, char):
        return super().nextState(currentState, char, self.stateTable)


class IKey(Matcher):
    qf = 2  # final state
    stateTable = [  # hash-table of states indexed by state number
        {"f":qf, "n":1}, #q0
        {"t":qf}, #q1
    ]

    def match(self, currentState, char):
        return super().nextState(currentState, char, self.stateTable)


class KeywordMatcher:
    def keyMatch(self, word):
        # TODO: extend this to be a general function

        if word[0] == "c":  # for other starting chars, create object of the corresponding class
            matchObj = CKey()
        elif word[0] == "r":
            matchObj = RKey()
        elif word[0] == "d":
            matchObj = DKey()
        elif word[0] == "i":
            matchObj = IKey()
        else:  # otherwise not a keyword
            return False

        # this portion remains unchanged

        state = 0

        for ch in word[1:]:  # program already knows what it starts with
            state = matchObj.match(state, ch)  # get new state
        if state == matchObj.qf:  # if the DFA has reached its final state and has no more characters to read
            return True  # keyword found!
        else:
            return False

