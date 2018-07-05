"""
Program created by Evaldas Senavaitis 1402039
2016/02/26
"""

numbers = [132, 201, 141, 74, 140, 94, 141, 140, 141, 15, 31, 164, 90, 229, 201, 141, 78, 114, 241, 217, 141, 217, 140, 180, 141, 164, 51, 141, 188, 221, 31, 164, 241, 177, 141, 140, 51, 217, 141, 201, 229, 152, 141, 78, 241, 114, 78, 102, 94, 141, 74, 152, 31, 152, 141, 94, 201, 31, 164, 102, 164, 51, 90, 141, 201, 229, 164, 31, 201, 152, 152, 51, 115]
key = 84

def bits(x):
    bits = bin(numbers[x])[2:].zfill(8) # getting 8 bits representation from a number
    return [bits[:2], bits[2:4], bits[4:6], bits[6:8]] # returning part of bits for manipulation

def bitwise_xor():
    for x in range(len(numbers)): # doing xor operation for every number
        numbers[x]^= key 

def bit_seperation(): # getting seperated bits from bits(x) and changing last two nibbles places
    for x in range(len(numbers)):
        bit_s = bits(x)
        nib = ''.join([bit_s[y] for y in [0, 1, 3, 2]])
        numbers[x] = int(nib, 2)

def s_box(): # doing sbox operation as described in coursework swapping one numbers with anothers
    for x in range(len(numbers)):
        bit_s = bits(x)
        swap = {'00':'10', '01':'00', '10':'11', '11':'01'}
        for i in range(len(bit_s)):
            bit_s[i] = swap[bit_s[i]]
        numbers[x] = int(''.join(bit_s), 2)

def subtract(): # subtracting and doing modulo by 4 
    for x in range(len(numbers)):
        two_bits = ['00', '01', '10', '11'] # possible variation of bits of 2
        pos_bits = [] # new storage place for bits
        for y in bits(x):
            pos_bits.append(two_bits.index(y))
        pos_bits[0] = (pos_bits[0] - pos_bits[2])%4
        pos_bits[1] = (pos_bits[1] - pos_bits[3])%4
        numbers[x] = int(''.join([two_bits[y] for y in pos_bits]), 2)
# seq described for decryption in coursework
bitwise_xor()
bit_seperation()
s_box()
bitwise_xor()
subtract()      
bit_seperation()
s_box()
bitwise_xor()
# printing out the message in standart python form
for x in numbers:
    print(chr(x), end = "")
