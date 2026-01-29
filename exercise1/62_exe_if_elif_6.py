"""
    write a program display marriage compatibility for male female using birth dates as per below link,
  accept birth day and birth month from user as separate input for both male & female.
   decide zodiac sign as per previous example and then use zodiac sign to decide  marriage compatibility
 https://miro.medium.com/v2/resize:fit:1100/format:webp/1*f58HMTVzfN2XvCPR23wXgA.jpeg
"""
mz=""
i=1
run=True
while i<3:
    if i==1:
        print("Enter birthdate  of male")
    else:
        print("Enter birthdate  of female")
    d=int(input("Enter day of birth : "))
    m=int(input("Enter birth month : "))

    if (m == 1 and d > 31) or (m == 2 and d > 28) or (m == 3 and d > 31) or (m == 4 and d > 30) or \
    (m == 5 and d > 31) or (m == 6 and d > 30) or (m == 7 and d > 31) or (m == 8 and d > 31) or \
    (m == 9 and d > 30) or (m == 10 and d > 31) or (m == 11 and d > 30) or (m == 12 and d > 31) or\
    (m<0 or m>12) or d<1 :
        print("Invalid information entered")
        run=False
    else:
        if(d>=21 and m==3) or (d<=19 and m==4):
            mz="Aries"
        elif(d>=20 and m==4) or (d<=20 and m==5):
            mz="Taurus"
        elif(d>=21 and m==5) or (d<=20 and m==6):
            mz="Gemini"
        elif(d>=21 and m==6) or (d<=22 and m==7):
            mz="Cancer"
        elif(d>=23 and m==7) or (d<=22 and m==8):
            mz="Leo"
        elif(d>=23 and m==8) or (d<=22 and m==9):
            mz="Virgo"
        elif(d>=23 and m==9) or (d<=22 and m==10):
            mz="Libra"
        elif(d>=23 and m==10) or (d<=21 and m==11):
            mz="Scorpio"
        elif(d>=22 and m==11) or (d<=21 and m==12):
            mz="Sagittarius"
        elif(d>=22 and m==12) or (d<=19 and m==1):
            mz="Capricorn"
        elif(d>=20 and m==1) or (d<=18 and m==2):
            mz="Aquarius" 
        elif(d>=19 and m==2) or (d<=20 and m==3):
            mz="Pisces"
        else:
            print("Invalid while assigniment of sign")
    if i==1:
          male=mz
    else:
        female=mz
    i+=1

if run==False:
    print("There was an error while data enterning")
else:
    if male == "Aries":
        if female in ["Taurus", "Capricorn", "Cancer", "Scorpio"]:
            print("Marriage Compatibility : Not Favorable")
        elif female in ["Virgo", "Pisces"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male == "Leo":
        if female in ["Virgo", "Capricorn"]:
            print("Marriage Compatibility : Not Favorable")
        elif female in ["Taurus", "Aquarius", "Cancer", "Scorpio", "Pisces"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male == "Sagittarius":
        if female in ["Taurus", "Virgo", "Capricorn"]:
            print("Marriage Compatibility : Not Favorable")
        elif female in ["Cancer", "Scorpio", "Pisces"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male == "Taurus":
        if female in ["Aries", "Sagittarius", "Gemini", "Aquarius"]:
            print("Marriage Compatibility : Not Favorable")
        elif female in ["Leo", "Libra"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male == "Virgo":
        if female in ["Aries", "Sagittarius", "Gemini", "Libra", "Pisces"]:
            print("Marriage Compatibility : Not Favorable")
        elif female in ["Leo", "Aquarius"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male == "Capricorn":
        if female in ["Aries", "Sagittarius", "Gemini", "Aquarius"]:
            print("Marriage Compatibility : Not Favorable")
        elif female in ["Leo", "Libra"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male == "Gemini":
        if female in ["Taurus", "Cancer", "Scorpio", "Pisces"]:
            print("Marriage Compatibility : Not Favorable")
        elif female in ["Sagittarius", "Virgo", "Capricorn"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male == "Libra":
        if female in ["Virgo", "Capricorn", "Cancer", "Scorpio"]:
            print("Marriage Compatibility : Not Favorable")
        elif female in ["Aries", "Taurus", "Pisces"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male == "Aquarius":
        if female in ["Taurus", "Virgo", "Capricorn", "Cancer"]:
            print("Marriage Compatibility : Not Favorable")
        elif female in ["Scorpio", "Pisces"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male == "Cancer":
        if female in ["Aries", "Gemini", "Libra", "Aquarius"]:
            print("Marriage Compatibility : Not Favorable")
        elif female in ["Leo", "Sagittarius"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male == "Scorpio":
        if female in ["Gemini", "Libra", "Aquarius"]:
            print("Marriage Compatibility : Not Favorable")
        elif female in ["Aries", "Leo"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    elif male == "Pisces":
        if female in ["Gemini", "Libra", "Aquarius"]:
            print("Marriage Compatibility : Not Favorable")
        elif female in ["Aries", "Leo", "Sagittarius", "Virgo"]:
            print("Marriage Compatibility : Favorable Match")
        else:
            print("Marriage Compatibility : Great Match")

    else:
        print("Invalid info givem")