
year = int(input("Enter the year :"))

if (year % 400 ==0)|( year%4 ==0 & year % 100 !=0):
    print("Year is leap year")
else:
    print("Year is NOT a leap year")