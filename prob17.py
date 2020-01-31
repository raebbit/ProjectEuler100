"""
Project Euler: Problem 17: Number letter counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to given limit inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def under_999(number):
    word_list = []
    if number == 1000: # exception
        return 'OneThousand'

    under_20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen',
    'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    hundred = number // 100
    under_99 = number % 100
    one = number % 10
    if hundred > 0:
        word_list.append(under_20[hundred])
        word_list.append('hundred')

        if under_99 > 0:
            word_list.append('And')

    if under_99 < 20:
        word_list.append(under_20[under_99])
    else:
        ten = under_99 // 10
        word_list.append(tens[ten])
        if one > 0:
            word_list.append(under_20[one])
    
    
    return ''.join(word_list)


def numbers_letter_counts(limit):
    count = 0
    for i in range(1, int(limit)+1):
        letters = under_999(i)
        count += len(letters) 

    return count


if __name__ == '__main__':
    limit = input("Set the limit (1 <= limit <= 1000): ")
    print(numbers_letter_counts(limit))