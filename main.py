import pytest

def open_file(file):
	with open(file, 'r') as f:
		return [line.strip() for line in f]

def write_file(shit):
	with open("result.txt",'a') as f:
		for text in shit:
			f.write(text + '\n')

def sort_file(string):
	for k,value in enumerate(skills[string]):
		count = 0
		for i, j in enumerate(skills[string]):
			if value == j:
				count+=1
				if count == 2:
					skills[string][k] = "<u>" + skills[string][k] + "</u>"
					skills[string].pop(i)

	write_file(skills[string])




try:
	skills = {
			"hard": open_file('hard.txt'),
	 		"soft": open_file('soft.txt') 
	 		}
except Exception as e:
	print(e)
finally:
	pass




with open("result.txt",'a') as f:
	f.write("HARDSKILLS:\n")
sort_file("hard")


with open("result.txt",'a') as f:
	f.write("\nSOFTSKILLS:\n")
sort_file("soft")








#TESTS 
def test_types():
	print(f"{skills.values()}, \n\
	У НАС ТУТ ПРАВДА СЛОВАРЬ?\t{type(skills) == type(dict())}\
	\nУ НАС ТУТ ПРАВДА СПИСОК?\t{type(skills['hard']) == type(list())}")


#мы заранее знаем, что в тестовом файле hard.txt дублируется только первые 3 скилла
#Проверяем, что не задело ненужные строки из начального файла.
def test_count():
	started_file = open_file("hard.txt")
	ended_file = open_file("result.txt")
	started_file.pop(0) 
	started_file.pop(0) 
	started_file.pop(0)
	started_file.pop(-1)
	started_file.pop(-1)
	started_file.pop(-1)
	print(started_file)

	for i in started_file:
		assert i in ended_file
