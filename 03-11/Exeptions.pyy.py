try:
    print("Start of try block")
    print(10 / 5)
    print(12 / 2)
    #print(10 / 0)
    #print(value_1)
    print(int("123fsas.123"))
    print("End of try block")
except ZeroDivisionError:
    print("division by zero")
except NameError:
    print("Такої змінної не існує")
except ValueError:
    print("ERROR / помилка to interge")

print("Next code")
