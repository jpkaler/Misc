#!python3
# base_converter.py - Converts any number from base (2-36) to another (2-36)
import sys

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Transform number from any base to base 10
def to_base10(base, num):
    base10num = 0
    count = 0 # PASKA, EN KEKSI PAREMPAA :(((
 
    for digit in num[::-1]:
        try:
            base10num += int(digit)*(base**count)
            count += 1
        except:
            base10num += (ALPHABET.index(digit.upper())+10)*(base**count)
            count += 1
    return base10num

# Transform base 10 number to any base
def to_end_base(base, num):
    end_base_num = ''
    while num//base > 0:
        if num%base < 10:
            end_base_num += str(num%base)
        else:
            end_base_num += ALPHABET[(num%base)-10]
        num = num//base
    last_num = lambda x: str(x) if x<10 else ALPHABET[x-10]
    end_base_num += last_num(num%base)
    return end_base_num[::-1]

# Check if given num in correct base
def basecheck(base, num):
    if base<=9:
        for digit in num:
            try:
                if int(digit) > (base-1):
                    return False
            except:
                return False
    else:
        for digit in num:
            if digit in ALPHABET:
                if digit.upper() not in ALPHABET[:(base-10)]:
                    return False
    
    return True

# Raise errors for unexpected values and return final number
def converter(start, end, num):
    try:    
        if int(start)>=32 or int(end)>=32:
            return 'One or both base(s) incorrect'
    except ValueError:
        return 'One or both base(s) incorrect'

    if basecheck(int(start), num):
        return to_end_base(int(end), to_base10(int(start), num))
    else:
        return 'Given number in wrong base'

# Main program loop    
while(True):
    print()
    print('Welcome to Number Base Converter!')
    print('This program will change a number from any starting base (2-36) to any other base (2-36)')
    print()
    startbase = input('Insert starting base: ')
    endbase = input('Insert final base: ')
    number = input('Give a number in base ' + startbase + ': ')
    print()
    print('Number in base ' + endbase + ': ' + converter(startbase, endbase, number))
    print('\n')
    if input('Press any key to continue... \n(q)uit\n')=='q':
        sys.exit()

# TESTING
'''print(converter(16,8,'B8C'))
print(converter(2,22,'10220'))
print(converter(25,6,'HFK92'))
print(converter(10,2,'250'))
print(converter(14,10,'C54'))'''