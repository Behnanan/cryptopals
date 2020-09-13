# Convert hex to base64

# The string: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

# Should produce: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t


hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
base64_string = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

hex_to_binary = { '0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', '8' : '1000'
, '9' : '1001', 'a' : '1010', 'b' : '1011', 'c' : '1100', 'd' : '1101', 'e' : '1110', 'f' : '1111' }

binary_to_base64 = {'000000' : 'A','000001' : 'B','000010' : 'C', '000011' : 'D','000100' : 'E', '000101' : 'F','000110' : 'G','000111' : 'H','001000' : 'I',
'001001' : 'J','001010' : 'K','001011' : 'L','001100' : 'M','001101' : 'N','001110' : 'O','001111' : 'P','010000' : 'Q','010001' : 'R','010010' : 'S',
'010011' : 'T','010100' : 'U','010101' : 'V','010110' :	'W','010111' : 'X','011000' : 'Y','011001' : 'Z','011010' :	'a','011011' : 'b','011100' : 'c',
'011101' : 'd','011110' : 'e','011111' : 'f','100000' : 'g','100001' : 'h','100010' : 'i','100011' : 'j','100100' :	'k','100101' : 'l','100110' : 'm',
'100111' : 'n','101000' : 'o','101001' : 'p','101010' :	'q','101011' : 'r','101100' : 's','101101' : 't','101110' :	'u','101111' : 'v','110000' : 'w',
'110001' : 'x','110010' : 'y','110011' : 'z','110100' : '0','110101' : '1','110110' : '2','110111' : '3','111000' : '4','111001' : '5','111010' : '6',
'111011' : '7','111100' : '8','111101' : '9','111110' : '+','111111' : '/'}

binary_list = []
base64_list = []

for i in hex_string:
    binary_list.append(hex_to_binary[i])

binary_list = "".join(binary_list)

binary_list = [binary_list[start:start+6] for start in range(0, len(binary_list), 6)]

for i in binary_list:
    base64_list.append(binary_to_base64[i])

base64_list = "".join(base64_list)

if(base64_list == base64_string):
    print("Succesfully converted hex to base64")