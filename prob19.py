"""
Project Euler: Problem 19: Counting Sundays
You are given the following information, but you may prefer to do some research for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September, April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def counting_sundays(firstyear, lastyear):
    first_of_month = [1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30] # February has 28 days

    # Counting days for the first year
    days_counts = 0
    for i in range (1900, int(firstyear)):
        if i % 4 == 0 and i != 1900:
            days_counts += 366
        else:
            days_counts += 365
    
    sunday_counts = 0
    for year in range(int(firstyear), int(lastyear)+1):
        if year % 4 == 0:
            first_of_month[2] = 29 # Leap year
        else:
            first_of_month[2] = 28

        for j in first_of_month:
            days_counts += j 
            if days_counts % 7 == 0: # (Since the days_counts for 1 Jan 1900(Monday) is 1) If the days_counts is 7, it's Sunday.
                sunday_counts += 1

        days_counts += 30 # 31 days in December 

    return sunday_counts

if __name__ == '__main__':
    firstyear = input("First Year: ")
    lastyear = input("Last Year: ")
    print(counting_sundays(firstyear, lastyear))
            

    
    


    