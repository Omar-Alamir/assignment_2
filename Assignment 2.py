##################
#   Question 1   #
##################
def count_digits(n):
 if n < 10:
  return 1
 else:
  return 1 + count_digits(n // 10)


def main():
 while True:
  print("1. Count Digits\n2. Find Max\n3.1. Count Tags\n3.2. Count Normalized Columns\n4. Exit")
  print("- - - - - - - - - - - - - - -")
  choice = input("Enter a choice: ")

  if choice == "1":
   try:
    num = int(input("Enter an integer: "))
    print("Output:", count_digits(abs(num)))
   except ValueError:
    print("Please enter a valid integer.")
  elif choice == "2":
   # Add the code for option 2 here
   pass
  elif choice == "3.1":
   # Add the code for option 3.1 here
   pass
  elif choice == "3.2":
   # Add the code for option 3.2 here
   pass
  elif choice == "4":
   print("Exiting the program. Goodbye!")
   break
  else:
   print("Invalid choice. Please try again.")


main()

