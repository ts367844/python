#  write a program to find out which is cheaper approach to buy IPhone 17 pro max.  consider use is going usa should he buy iphone from usa or from india
price_usa_usd = 1199
usa_tax_percent = 8
usd_to_inr_rate = 85


price_india= 159900


usa_tax_amount= (price_usa_usd * usa_tax_percent) / 100
usa_total_price_usd = price_usa_usd + usa_tax_amount
usa_total_price_inr = usa_total_price_usd * usd_to_inr_rate


print("Total cost in USA :", usa_total_price_inr)
print("Total cost in India :", price_india)


if usa_total_price_inr < price_india:
    print("Cheaper option is  from USA")
else:
    print("Cheaper option is from India")