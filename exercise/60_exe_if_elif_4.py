"""
     write a program to accept birth d and birth mon from user as separate input. decide zodiac sign from below table 
    Aries: March 21-April 19
    Taurus: April 20-May 20
    Gemini: May 21-June 21
    Cancer: June 22-July 22
    Leo: July 23-August 22
    Virgo: August 23-September 22
    Libra: September 23-October 22
    Scorpio: October 24-November 21
    Sagittarius: November 22-December 21
    Capricorn: December 22-January 19
    Aquarius: January 20-February 18

    Pisces: February 19-March 20
"""
d = int(input("Enter your birth day: "))
mon = int(input("Enter your birth mon (1-12): "))

if (mon == 3 and d >= 21) or (mon == 4 and d <= 19):
    print("Zodiac Sign: Aries")
elif (mon == 4 and d >= 20) or (mon == 5 and d <= 20):
    print("Zodiac Sign: Taurus")
elif (mon == 5 and d >= 21) or (mon == 6 and d <= 21):
    print("Zodiac Sign: Gemini")
elif (mon == 6 and d >= 22) or (mon == 7 and d <= 22):
    print("Zodiac Sign: Cancer")
elif (mon == 7 and d >= 23) or (mon == 8 and d <= 22):
    print("Zodiac Sign: Leo")
elif (mon == 8 and d >= 23) or (mon == 9 and d <= 22):
    print("Zodiac Sign: Virgo")
elif (mon == 9 and d >= 23) or (mon == 10 and d <= 22):
    print("Zodiac Sign: Libra")
elif (mon == 10 and d >= 23) or (mon == 11 and d <= 21):
    print("Zodiac Sign: Scorpio")
elif (mon == 11 and d >= 22) or (mon == 12 and d <= 21):
    print("Zodiac Sign: Sagittarius")
elif (mon == 12 and d >= 22) or (mon == 1 and d <= 19):
    print("Zodiac Sign: Capricorn")
elif (mon == 1 and d >= 20) or (mon == 2 and d <= 18):
    print("Zodiac Sign: Aquarius")
elif (mon == 2 and d >= 19) or (mon == 3 and d <= 20):
    print("Zodiac Sign: Pisces")
else:
    print("Invalid date entered")
