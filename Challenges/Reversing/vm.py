import sys

def execute(code, sp, stack):
    eq_flag = True
    skip = False
    skip_times = 0
    for ip in range(0, len(code)):
        if skip and skip_times == 0:
            skip = False
        elif skip_times > 0:
            skip_times -= 1
        else:
            if code[ip] == 88:
                ip += 1
                stack.append(code[ip])
                skip = True
            elif code[ip] == 21:
                stack[sp] += 1
            elif code[ip] == 1:
                stack[sp] -= 1
            elif code[ip] == 200:
                ip +=1
                sp += code[ip]
                skip = True
            elif code[ip] == 173:
                ip += 1
                sp -= code[ip]
            elif code[ip] == 15:
                tmp = ""
                for x in stack[sp:]:
                   if x == 0:
                       break
                   else:
                       sp += 1
                       tmp += chr(x)
                sys.stdout.write(tmp)
            elif code[ip] == 16:
                rin = raw_input()
                for x in rin:
                    stack.append(ord(x))
                stack.append(0)
            elif code[ip] == 118:
                ip += 1
                stack[sp] ^= code[ip]
                skip = True
            elif code[ip] == 57:
                sp = len(stack)-1
            elif code[ip] == 69:
                ip += 1
                if stack[sp] == stack[code[ip]]:
                    eq_flag = eq_flag and True
                else:
                    eq_flag = eq_flag and False
                skip = True
            elif code[ip] == 70:
                if not eq_flag:
                    skip_times += code[ip+1]
                skip = True
            elif code[ip] == 20:
                sys.exit(0)

code = [88, 73, 88, 110, 88, 115, 88, 101, 88, 114, 88, 116, 88, 32, 88, 112, 88, 119, 88, 58, 88, 20, 88, 0, 15,
        16, 88, 198, 88, 221, 88, 226, 88, 229, 88, 163, 88, 252, 88, 234, 88, 0, 200, 1, 57, 173, 7, 118, 144,
        200, 1, 118, 144, 200, 1, 118, 144, 200, 1, 118, 144, 200, 1, 118, 144, 200, 1, 118, 144, 200, 1, 118, 144,
        173, 6, 69, 12, 200, 1, 69, 13, 200, 1, 69, 14, 200, 1, 69, 15, 200, 1, 69, 16, 200, 1, 69, 17, 200, 1, 69,
        18, 200, 1, 69, 19, 70, 22, 200, 1, 88, 67, 88, 111, 88, 110, 88, 103, 88, 114, 88, 97, 88, 116, 88, 122, 88,
        33, 15, 20, 200, 1, 88, 66, 88, 97, 88, 100, 88, 32, 88, 80, 88, 97, 88, 115, 88, 115, 88, 33, 15, 20]

execute(code, 0, [])
