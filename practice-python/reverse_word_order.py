def solution():
	w = input("Gimme the sentence: ")
	# sentence = input("Gimme your sentence: ")
	return ' '.join(w.split()[::-1])

# print (solution())