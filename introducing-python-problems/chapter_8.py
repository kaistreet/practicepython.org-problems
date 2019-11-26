#Problem 8.1: Assign the string 'This is a test of the emergency text system' to the variable test1, and write test1 to a file called test.txt
test1 = 'This is a test of the emergency text system'
fileout = open('test.txt','w')
fileout.write(test1)
fileout.close()
