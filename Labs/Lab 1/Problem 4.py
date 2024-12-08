A = True
B = True
C = False
D = “”
E = 0
F = not C

(A or B) and (not C and A) True
(C and B) or (A or C) True
(C and B) or (A or C) True
(A and D) or (E == 5 - 5) True
not (F and B and E or A) False

(64 == 2**6) and (E or F) True

D = "a" True
six = (D and B) and (F = E) False

E += 1  True
seven = (7 % 2 == 0) or (E and F) True

(not D) or (not F) False