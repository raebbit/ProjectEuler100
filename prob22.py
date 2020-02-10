"""
Project Euler: Problem 22: Names scores

Using names.txt, an array containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
def names_scores(arr):
    alphabets = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    nth_name = 0 
    total_score = 0
    arr.sort()
    for name in arr:
        nth_name += 1
        alphabet_score = 0
        for letter in name:
            alphabet_score += alphabets[letter]
        
        total_score += nth_name * alphabet_score
    
    return total_score

if __name__ == '__main__':
    # Get the list of names from txt file
    names = []
    file = open('p022_names.txt', 'r')
    data = file.read().split(',')
    for n in data:
        names.append(n[1:-1]) # remove ""
    print(names_scores(names))
