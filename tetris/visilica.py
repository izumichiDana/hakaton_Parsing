from random import choice


HANGMAN = [
	'''
	  +---+
	  |   |
	      |
	      |
	      |
	      |
	=========
	''', 
	'''
	  +---+
	  |   |
	  O   |
	      |
	      |
	      |
	=========
	''', 
	'''
	  +---+
	  |   |
	  O   |
	  |   |
	      |
	      |
	=========
	''', 
	'''
	  +---+
	  |   |
	  O   |
	 /|   |
	      |
	      |
	=========
	''', 
	'''
	  +---+
	  |   |
	  O   |
	 /|\  |
	      |
	      |
	=========
	''',
	'''
	  +---+
	  |   |
	  O   |
	 /|\  |
	 /    |
	      |
	=========
	''',
	'''
	  +---+
	  |   |
	  O   |
	 /|\  |
	 / \  |
	      |
	=========
	'''
]



max_wrong = len(HANGMAN)
WORDS = ('game', 'python', 'grammy', 'pop', 'java', 'friends', 'love','git')


word = choice(WORDS)
so_far = '_' * len(word)
wrong = 0
used = []
correct = []
print(word)




while wrong < max_wrong and so_far != word:
	print(wrong)
	
	print(f'Вы использовали следующие буквы: {used}')
	print(f'На данный момент слово выглядит вот так: {so_far}')

	quess = input('Введите предположение: ')
		
	while quess in used:
		print(f'Вы уже угодали букву, {quess}')
		quess = input('Ведите предполодение: ')
	
	used.append(quess)

	res = ''.join(used)

	if res != word:
		print(f'Тебя повесили!,загаданнное слово было, {word}')
	else:
		print('Ура! Вы угодали ')
	
	if quess in word:
		print(f'Да {quess} есть в слове')
		correct.append(quess)
		new = ''
		for i in word:
			if i in correct:
				new += i
			else:
				new += "_"
		so_far = new
	else: 
		print(f'Извините буквы  {quess}  нет в слове.')

		wrong += 1


