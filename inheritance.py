class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass


d = Dog()
d.speak()

# # Parent Class
class Person:
    def introduce(self):
        print("I am a Person")

# Child Class
class Student(Person):
    pass

# Create a list of students
students = [Student(), Student(), Student()]

# Use loop
for s in students:
    s.introduce()
    

# 3. Text Information Processor (Data Handling)
text=input("paste your text here: ")

words=text.split()

print(f"total words: {len(words)}")

search_word=input("enter a word to search for: ")

if search_word in text:

    print(f"found  the word '{search_word}' appears  {text.count(search_word)} times in the text.")
else:
    
    print("word not found in the text:")

# 3. Smart Task Checklist (Basic Automation)    
todo_list=[]
while True:
    action=input("\nchoose [add] task,[view] tasks, or [exit] to quit: ").lower()
    if action=="add":
        task=input("enter a task to add: ")
        todo_list.append(task)
        print(f"task '{task}' added to the list.")
    elif action=="view":
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")
    elif action=="exit":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please choose [add], [view], or [exit].")