size = int(input("Enter the size of the pattern: "))
row = 1
while row <= size:
  for rows in range(1, size):
    print ("*", end="")
  print ()
  row += 1
