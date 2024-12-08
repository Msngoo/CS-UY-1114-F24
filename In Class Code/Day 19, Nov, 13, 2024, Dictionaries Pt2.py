def readFile(file):
    inFile = open( "r")
    outerDict = {} #This is the first dictionary where each key will be an n number, with a dictionary as its value
    keyOuter = {} #Each N number will be a key in the outer dictionary, 1 of 3 total dictionaries
    studentData = {} # A dictionary that will hold all the stats of each student, this will be the value for the N number key (keyOuter)

for line in inFile:
    line = line.strip()
    lst = line.split(",")
    {keyOuter[lst[0]]: {'firstName': lst[1], 'lastName': lst[2], 'email': lst[3], 'gpa': lst[3], 'gradYr'}}