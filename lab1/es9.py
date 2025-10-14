"""
Write a function magic(start, end) that takes two integers representing
two and returns a tuple of tuples, representing all the magic dates 
between start and end.
"""

def daysInMonth(month: int, year: int) -> int:
    match month:
        case 1:
            return 31
        case 2:
            if year % 4 == 0 and year % 100 != 0:
                return 29
            return 28
        case 3:
            return 31
        case 4:
            return 30
        case 5:
            return 31
        case 6:
            return 30
        case 7:
            return 31
        case 8:
            return 31
        case 9:
            return 30
        case 10:
            return 31
        case 11:
            return 31
        case 12:
            return 31


def magic(start: int, end: int) -> tuple:
    if start <= end:
        l = []

        digits = 0
        for year in range(start, end + 1):
            digits = year % 100
            for month in range(1, 12 + 1):
                days = daysInMonth(month, year)
                for day in range(1, days + 1):
                    product = month * day

                    if product == digits:
                        magic = (day, month, year)
                        l.append(magic)
        return tuple(l)

    return ()

print(magic(1990, 2000))