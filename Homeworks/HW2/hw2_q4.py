"""
Author: Christian Auguste
Assignment / Part: HW#2 - Q4
Date due: September 26, 2024 11:59pm
I pledge that I have completed this assignment without collaborating with 
anyone else, in conference with the NYU Tandon School of Engineering Policies 
and Procedures on Academic Misconduct.
"""

dayV = int(input("Enter the number of days Vamshi has worked: "))
hourV = int(input("Enter the number of hours Vamshi has worked: "))
minV = int(input("Enter the number of minutes Vamshi has worked: "))
dayN = int(input("Enter the number of days Nishat has worked: "))
hourN = int(input("Enter the number of hours Nishat has worked: "))
minN = int(input("Enter the number of minutes Nishat has worked: "))


if minV + minN >= 60:
    minSum = minV + minN
    minToHr = minSum // 60
    minCombined = minSum % 60
else:
    minCombined = minV + minN
    minToHr = 0

if hourV + hourN >= 24:
    hrSum = hourV + hourN
    hrToDay = hrSum // 60
    hourCombined = hrSum % 24
    hourCombined += minToHr
else:
    hourCombined = hourV + hourN
    hrToDay = 0

dayCombined = hrToDay + dayV + dayN

print("The total time both CAs worked together is:",dayCombined, "days," , hourCombined, "hours and" , minCombined , "minutes"  )
    
daySum = dayV + dayN
hourSum = hourV + hourN