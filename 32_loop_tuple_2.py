# for loop with tuple
#write a program to display countries from north america 
countries = ("india", "usa", "canada", "mexico", "brazil", "argentina", "uk", "france", "germany", "italy", "spain", "china", "japan", "south korea", "australia", "new zealand", "south africa", "egypt", "nigeria", "russia")

north_america_countries = ["canada","usa","mexico","belize","costa rica","el salvador","guatemala","honduras","nicaragua","panama","antigua and barbuda","bahamas","barbados","cuba","dominica","dominican republic","grenada","haiti","jamaica","saint kitts and nevis","saint lucia","saint vincent and the grenadines","trinidad and tobago"]

for item in countries:
    if item in north_america_countries:
        print(item)