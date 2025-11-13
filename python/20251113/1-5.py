# from ascii 32 to ascii 126

max_length = 2

passwds = []

for str_length in range(1, max_length + 1):
    chars = [32] * str_length
    while chars[0] < 126:
        gen_str = ""
        for c in chars:
            gen_str += chr(c)
            
        # print(gen_str)
        passwds.append(gen_str)

        chars[-1] += 1
        
        for i in range(str_length-1, 0, -1):
            if chars[i] > 126:
                chars[i-1] += 1
                chars[i] = 32
                

print(passwds)