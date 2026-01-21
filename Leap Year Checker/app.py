def leap_year(n):
    return (n%400==0 or (n%4==0 and n%100!=0))

year=int(input("Enter year: "))
if leap_year(year):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")