#write a program to findout coutries whose area is greater given area. 


country_area = {
    "Russia": 17098242,
    "Canada": 9984670,
    "China": 9596961,
    "United States": 9833517,
    "Brazil": 8515767,
    "Australia": 7692024,
    "India": 3287263,
    "Argentina": 2780400,
    "Kazakhstan": 2724900,
    "Algeria": 2381741
}

area=int(input("Enter area of country  : "))
for no in country_area:
    if country_area[no]>area:
        print(no," ",country_area[no])