"Evaldas Senavaitis 1402039 2nd Computer security assignment "
file = open("flower.bmp","rb")
data = bytearray(file.read())
file.close()
#p is 7 and q is 15
p = 25
q = 25
header_len = 54
m_value = 0
result = (0, 0)
for x in range(1, p):
        
        for y in range(1, q):
                
                text_as_bits = bytearray((len(data) - header_len - x) // y)
                
                for i in range(0, len(text_as_bits)):
                        
                        text_as_bits[i] = data[header_len + x + i * y] & 0b00000001
                        
                text = bytearray(len(text_as_bits)//8)
                
                count = 0
                
                for i in range(0, len(text)):
                        
                        text[i] = 0
                        
                        for j in range(0,8):
                                if text_as_bits[i*8+j]==1:
                                        count+=1
                                
                                text[i] = text[i] | (text_as_bits[i * 8 + j] << j)
                                
                value = abs(1 - count / ((len(text) * 8 ) - count ))
                if (value>m_value):
                        m_value = value
                        result = (x, y)

print(result)           

	
