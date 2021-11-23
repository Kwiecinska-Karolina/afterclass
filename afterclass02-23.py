""" 23% VAT was paid from the amount of PLN 15.84.
Calculate and display VAT. 
Apply formatting with decimal places. Sample result:

Amount : 15.84 zł VAT 23% : 3.64 zł"""
kwota = float(input())
stawka_VAT = 0.23
kwota_VAT = kwota * stawka_VAT

print("Kwota: ", kwota , " zł VAT 23%: ",(round(kwota_VAT, 2))," zł")
