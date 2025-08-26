# Comparative operators -> Always return true/false
# <, <=, >, >=, ==, ===, !=
value1 = 2
value2 = 5
print(value1 == value2)
print(value1 <= value2)


# Logical operators -> Work with comparative operators
# and, or
value3 = 5
value4 = 10
value5 = 15
print(value3 < value4 and value5 < value4)
print(value3 < value4 or value5 < value4)


# Conditional statement
nama = "zauvik"
tahun_masuk = 2016
tahun_lulus = 2019
spending_time = tahun_lulus - tahun_masuk # 6

if(spending_time > 3 and spending_time <= 6):
    # statement if true
    print("Punya potensi lulus")
    
else:
    print("Waduh jangan sampai Keluar / DO")
    # give default statement here if the conditions above all-false
