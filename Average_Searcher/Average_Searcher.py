num = []

NumInput = ""
stop = int (input ("How much numbers do want to add:"))

for i in range (stop):
    NumInput = int (input ("Enter a number here (press n to stop):"))
    num.append (NumInput)

Sum = sum (num)
print ("your total is",Sum)

print ("The average of the numbers are",Sum/stop)



