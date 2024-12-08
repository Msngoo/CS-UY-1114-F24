# # Problem # 1
# import random

# lst = [[0] * 5 for i in range(5)]
# for row in range(len(lst)):
#     for col in range(len(lst)):
#         lst[row][col] = round(random.uniform(0.0, 10.0), 1) 
# print(lst)

# sum = 0
# for row in range(len(lst)):
#     for col in range(len(lst)):
#        sum += lst[row][col]
# avg = sum / 25
# print('Average of all elements:', avg)

# Problem # 1: DePasquale Solution
import random

def make_2d(num_rows, num_cols, min_val=2.3, max_val=12.4):
    result = []
    
    for row in range(num_rows):
        row_data = []   #Temporary list to store the sublist before adding to result, after loop has 5 values and is reset upon next iteration
        for col in range(num_cols):
            val = round(random.uniform(min_val, max_val), 2)
            row_data.append(val)

        result.append(row_data)

    return result


def get_avg(result):
    total_vals = 0
    for row in range(len(result)):
        for col in range(len(result[0])):
            total_vals += result[row][col]
    return total_vals / (len(result) * len(result[0]))

def main():
    two_dee = make_2d(8, 8, 2.3, 12.4)

main()

# Problem 2: get_nucleotide_frequency
dna = "ACGTTTTCCCCCA"

def get_nucleotide_frequency(sequence):
    lst = []
    for i in sequence: 
        numA = sequence.count("A")
        tup_A = ("A", num_A)
        numC = sequence.count("C")
        tup_C = ("C", numC)
        numT = sequence.count("T")
        tup_T = ("T", numT)
        numG = sequence.count("G")
        tup_G = ("G", numG)
    lst.append(tup_A)
    lst.append(tup_C)
    lst.append(tup_T)
    lst.append(tup_G)
    return lst

# Problem 2: DePasquele Solution

def get_nucleotide_frequency(seqence):
    nucleous = "ACTG"
    result = []

    for nuc in nucleous:
        counter = sequence.count(nuc)
        nuc_tup = (nuc, counter)
        result.append(nuc_tup)
    return result

def main():
    dna = "ACGTTTTCCCCCA"
    print(get_nucleotide_frequency(dna))

main()
