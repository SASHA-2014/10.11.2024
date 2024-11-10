try:
  print(10 / 5)
  print(12 / 2)
  #print(10 / 0)
  print(value_1)
  print("End of the try block")
except ZeroDivisionError:
    print("division by zero")
except NameError:
    print("Такої зміної не існуе")

print("Next code")
