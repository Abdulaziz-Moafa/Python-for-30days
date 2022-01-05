try :
    value = int(input("enter a numebber "))
    print(value)
    result = 10 / 0
except ZeroDivisionError as err:
    print(err)

except ValueError as err1:
    print(err1)