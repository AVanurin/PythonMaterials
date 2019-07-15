import sys
import time


db = []


def print_menu():
	msg = '''
	1. Register new student
	2. Search by id
	3. Search by name
	4. Delete student with id
	5. Show all students
	6. Exit
	'''
	print(msg)


def add_new_student():
	name = input("Enter name:")

	biggest = 0
	for student in db:
		if student['id'] > biggest:
			biggest = student['id']

	temp = {"name": name, "id": biggest + 1}

	db.append(temp)
	print("Student successfully has been added!")


def search_by_id():
	s_id = int(input("Enter id to seak:"))
	for student in db:
		if s_id == student["id"]:
			print("Student:id " + str(student["id"]) + " named " + student["name"])
			return
	print("Not found")


def search_by_name():
	name = input("Enter name to seak:")
	count = 0
	for student in db:
		if student["name"].lower().find(name.lower()) != -1:
			print("Student:id " + str(student["id"]) + " named " + student["name"])
			count += 1
	if count == 0:
		print("Not founded!")
	else:
		print("Founded " + str(count) + " students")


def delete_student():
	s_id = int(input("Enter id to delete:"))
	for student in db:
		if s_id == student['id']:
			db.remove(student)
			print("Student has been successfully removed")
			return
	print("No such student. Pls try again")


def show_all():
	for student in db:
		print("Student:id " + str(student["id"]) + " named " + student["name"])


def exit():
	sys.exit()


def main():
	while True:
		print_menu()
		choice = str(input(":"))
		if choice.startswith("1") or choice.endswith("1"):
			add_new_student()
		elif choice.startswith("2") or choice.endswith("2"):
			search_by_id()
		elif choice.startswith("3") or choice.endswith("3"):
			search_by_name()
		elif choice.startswith("4") or choice.endswith("4"):
			delete_student()
		elif choice.startswith("5") or choice.endswith("5"):
			show_all()
		elif choice.startswith("6") or choice.endswith("6"):
			exit()
		else:
			print("Please enter valid data!")
        time.sleep(3)


if __name__ == "__main__":
	main()
