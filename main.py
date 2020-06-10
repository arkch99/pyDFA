import identifier
import keywords

word = input("Please enter the string you wish to evaluate: ")

genericIDObj = identifier.GenericIDMatcher()
keywordObj = keywords.KeywordMatcher()

if genericIDObj.IDMatch(word) and not keywordObj.keyMatch(word):
	print("'{}' is a valid C identifier.".format(word))
else:
	print("'{}' is not a valid C identifier.".format(word))


