import random
print("one random number between 0 and 1",random.random())
print("one random float number between 10 and 99",random.uniform(10,99))
print("one random number integer  between 10 to 99 ",random.randint(10,99))
print("one random number integer  between 10 to 100 divisible by 10 ",random.randrange(10,100,10))
books = ["Python Crash Course", "Fluent Python", "Learning Python", "Python for Data Analysis", "Automate the Boring Stuff with Python", "Effective Python", "Python Tricks", "Clean Code in Python", "Mastering Python Regular Expressions", "Python Cookbook", "Advanced Python Programming", "Test Driven Development with Python", "Two Scoops of Django", "Python for Finance", "Natural Language Processing with Python", "Machine Learning with Python", "Python Deep Learning", "The Pragmatic Programmer", "Design Patterns in Python", "Real Python"]

#pick one item randomly
print(random.choice(books))

#pick two item randomly
print(random.choices(books,k=2))

cards = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣"]
print(cards)
print(random.sample(cards,k=len(cards)))
random.shuffle(cards)
print(cards)
print(random.choices(cards,k=3))