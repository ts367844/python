# for loop with dictionary
#write a program to find out list of player who have made more century then given user given value
odi_centuries = {
    "sachin tendulkar": 49,
    "virat kohli": 50,
    "rohit sharma": 31,
    "ricky ponting": 30,
    "sanath jayasuriya": 28,
    "hashim amla": 27,
    "ab de villiers": 25,
    "kumar sangakkara": 25,
    "chris gayle": 25,
    "sourav ganguly": 22,
    "tillakaratne dilshan": 22,
    "david warner": 22,
    "quinton de kock": 21,
    "saeed anwar": 20,
    "babar azam": 19,
    "brian lara": 19,
    "shikhar dhawan": 17,
    "virender sehwag": 15,
    "kane williamson": 13,
    "joe root": 12
}
n = int(input("How many Century play should have scored?"))
for player in odi_centuries:
    if odi_centuries[player]>n:
        print(player,' ',odi_centuries[player])