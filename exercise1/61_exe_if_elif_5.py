"""write a program to findout day of week(monday/tuesday/wednesday) from given date.  
https://www.wikihow.com/Calculate-the-Day-of-the-Week"""
day=int(input("Enter day of month :"))
mon=int(input("Enter number of month :"))
lm=26-0  #Year ending digit
rf=lm//4 #Divinding by 4
lm+=rf #Adding with reminder
lm+=6 #adding 6
lis=["",0,3,3,6,1,4,6,2,5,0,3,5] #value of table according to calender
days=["Sunday","Monday","Tuesday","Wednesday","Thrsday","Friday","Sunday"] #days of week
res=lm+lis[mon]+day #Geting value from lis
res%=7  #Getting fay index
print(days[res])