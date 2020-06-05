class ckey:
	stateTable = [
		#qf = 999
		{"o": 1, "h": 8}, #q0
		{"n": 2}, #q1
		{"s": 3, "t": 4}, #q2
		{"t": 999}, #q3
		{"i": 5}, #q4
		{"n": 6}, #q5
		{"u": 7}, #q6
		{"e": 999}, #q7
		{"a": 9}, #q8
		{"r": 999} #q9
	]
	def nextState(self, currentState, char):
		try:
			state = self.stateTable[currentState][char]
		except(KeyError):
			state = currentState
		return state

def match(word):
	#TODO: extend this to be a general function
	if word[0] == "c":
		matcher = ckey()
	else:
		print("Whoa there, don't rush!")
	state = 0
	prevState = 0
	for ch in word[1:]: #program already knows what it starts with
		if state == 999:
			return False
		prevState = state
		state = matcher.nextState(state, ch)
		if state == prevState:
			return False
	if state == 999:
		return True

word = input()

if match(word):
	print("Keyword detected!")
else:
	print("Not a keyword.")