"""
Project Euler: Problem 14: Longest Collatz sequence
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under the given limit, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def longest_collatz_seq(limit):
    
    if int(limit) < 3:
        return 1
    else: 
        answer = 1
        lg_count = 0
        for i in range(2, int(limit)):
            number = i
            count = 1
            while i > 1:
                if i % 2 == 0:
                    i = i // 2
                else:
                    i = 3 * i + 1
            
                count += 1
            
            if count >= lg_count:
                answer = number
                lg_count = count
        
        return answer

if __name__ == '__main__':
    limit = input("The number which has the longest (Collatz) chain under: ")
    print(longest_collatz_seq(limit))

# Since `i` keeps changing, I had to contain the value of original `i` into `number` - debug



        




