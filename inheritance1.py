# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
    
#     def sound(self):
#         print("Bark")

# class Cat(Animal):
#     def sound(self):
#         print("Meow")

# animals = [Dog(), Cat(), Dog()]

# for animal in animals:
#     animal.sound()

# 2. Text Information Processor (Data Handling)

text=input("paste your text here: ")

words=text.split()

print(f"total words: {len(words)}")

search_word=input("enter a word to search for: ")

if search_word in text:

    print(f"found  the word '{search_word}' appears  {text.count(search_word)} times in the text.")
else:
    
    print("word not found in the text:")