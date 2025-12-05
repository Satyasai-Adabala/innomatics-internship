# import calendar as c
# def is_leap(n):
#     if c.isleap(n):
#         return True
#     else:
#         return False
def is_leap(n):
    if ((n%4==0 and n%100!=0)or n%400==0):
        return True
    else:
        return False


