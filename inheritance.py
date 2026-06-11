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