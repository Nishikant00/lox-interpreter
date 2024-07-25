import sys

def parse(file_contents):
    lexemes = {
        'true':'true',
        'false':'false',
        'nil':'nil',
    }
    res=""
    i=0
    data=file_contents.split(' ')
    while i<len(data):
        if data[i] in lexemes:
            res=f"{data[i]}"
        elif data[i].isnumeric() :
            res=f"{float(data[i])}"
        elif data[i]=='0' or data[i]=='0.0':
            res="0.0"
        elif data[i].replace('.', '', 1).isnumeric():
            res=f"{data[i]}"

        i+=1
    print(res)
        
def equality(eql):
    num=eql//2
    rem=eql%2
    ee_arr=""
    e_arr=""

    for i in range(rem):
        e_arr+="EQUAL = null\n"
    for i in range(num):
        ee_arr+="EQUAL_EQUAL == null\n"
    return (ee_arr,e_arr)

def scanner(data):
    tokens = {
        '(': "LEFT_PAREN ( null\n",
        ')': "RIGHT_PAREN ) null\n",
        '{': "LEFT_BRACE { null\n",
        '}': "RIGHT_BRACE } null\n",
        ',': "COMMA , null\n",
        '.': "DOT . null\n",
        '*': "STAR * null\n",
        '+': "PLUS + null\n",
        '-': "MINUS - null\n",
        ';': "SEMICOLON ; null\n",
        ' ':'',
        '\t':'',
    }
    operators=['+',' ','-',',','/','*','\n',')','(']
    keywords={'class','print','or','for','if','nil','while','return','and','super','else','false','true','this','var','fun'}
    res = ""
    error_code = 0
    lines = 1
    eql=0
    bang_eq=0
    l_eq=0
    g_eq=0
    skip=0
    string_skip=0
    strs=""
    num=""
    alpha=""
    dot_done=0
    alpha_e=0
    
    for i,ch in enumerate(data):

        if skip==1:
            if ch!='\n':
                continue
            else:
                skip=0   
        if string_skip==1:
            if ch!='"':
                if i==len(data)-1:
                    error_code = 65
                    print(f"[line {lines}] Error: Unterminated string.",file=sys.stderr)
                    string_skip=0
                    strs=""
                strs+=ch
                continue
            
            elif ch=='"' and len(strs)!=0:
                res+=f'STRING "{strs}" {strs}\n' 
                strs=""
                string_skip=0
                continue
        if ch.isalpha() or ch=='_' or (ch.isnumeric() and alpha_e==1):
            alpha+=ch
            alpha_e=1
            if alpha in keywords:
                res+=f"{alpha.upper()} {alpha} null\n"
                alpha_e=0
                alpha=""

            elif i==len(data)-1:
                res+=f"IDENTIFIER {alpha} null\n"
                alpha_e=0
                alpha=""
            elif i+1<len(data) and data[i+1] in operators:    
                res+=f"IDENTIFIER {alpha} null\n"
                alpha_e=0
                alpha=""
        elif ch.isnumeric() or ch=='.' and data[i-1].isnumeric() and i+1<len(data) and data[i+1].isnumeric():
            num+=str(ch)
            if ch=='.':
                dot_done+=1
            
            if dot_done==2:
                res+=f"NUMBER {num[:-1]} {num[:-1]}\n"
                res+='DOT . null\n'
                dot_done=0
                num=""
            elif i+1<len(data) and data[i+1] in operators:
                if dot_done==0:
                    res+=f"NUMBER {num} {num}.0\n"
                else:
                    if '.' in num and num.endswith('0'):
                        cut=0
                        for i in range(len(num)-1,-1,-1):
                            if num[i]=='0' and num[i-1]=='0':
                                cut+=1
                            else:
                                res+=f"NUMBER {num} {num[:-cut]}\n"
                                break
                    else:   
                        res+=f"NUMBER {num} {num}\n"
                num=""
                dot_done=0
            elif i+1<len(data) and data[i+1].isalpha():
                if dot_done==0:
                    res+=f"NUMBER {num} {num}.0\n"
                else:
                    if '.' in num and num.endswith('0'):
                        cut=0
                        for i in range(len(num)-1,-1,-1):
                            if num[i]=='0' and num[i-1]=='0':
                                cut+=1
                            else:
                                res+=f"NUMBER {num} {num[:-cut]}\n"
                                break
                    else:   
                        res+=f"NUMBER {num} {num}\n"
                num=""
                dot_done=0
            elif i==len(data)-1:
                if dot_done==0:
                    res+=f"NUMBER {num} {num}.0\n"
                else:
                    if '.' in num and num.endswith('0'):
                        cut=0
                        for i in range(len(num)-1,-1,-1):
                            if num[i]=='0' and num[i-1]=='0':
                                cut+=1
                            else:
                                res+=f"NUMBER {num} {num[:-cut]}\n"
                                break
                    else:   
                        res+=f"NUMBER {num} {num}\n"
                num=""
                dot_done=0
            continue
        elif ch=='.' and len(num)>0:
            res+=f"NUMBER {num} {num}.0\n"
            num=""
            res+='DOT . null\n'
            continue
        
        
        elif ch=='"':
            string_skip=1
            continue       
        elif ch in tokens:
            res +=tokens[ch]
        elif ch == '\n':
            lines += 1
        elif ch=='/':
            if i+1<len(data) and data[i+1]=='/':
                skip=1
                continue
            else:
                res+="SLASH / null\n"
        elif ch =='!':
            if i+1<len(data) and data[i+1]=='=':
                bang_eq+=1
                res+="BANG_EQUAL != null\n"
            else:   
                res+="BANG ! null\n"
        elif ch =='<':
            
            if i+1<len(data) and data[i+1]=='=':
                bang_eq+=1
                res+="LESS_EQUAL <= null\n"
            else:   
                res+="LESS < null\n"
        elif ch =='>':
            if i+1<len(data) and data[i+1]=='=':
                bang_eq+=1
                res+="GREATER_EQUAL >= null\n"
            else:   
                res+="GREATER > null\n"
        elif ch=='=':
            if bang_eq==1:
                bang_eq=0
                continue
            if l_eq==1:
                l_eq=0
                continue
            if g_eq==1:
                g_eq=0
                continue
            if i+1<len(data) and data[i+1]=='=':
                eql+=1
            else:
                eql+=1
                ee_arr,e_arr=equality(eql)
                eql=0
                res+=f"{ee_arr}{e_arr}"
        else:
            error_code = 65
            print(f"[line {lines}] Error: Unexpected character: {ch}", file=sys.stderr)

    print(res + "EOF  null")
    exit(error_code)
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]
    commands={"tokenize","parse"}
    if command not in commands:
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    if file_contents:
        if command=='tokenize':
            scanner(file_contents)
        elif command=='parse':
            parse(file_contents)
    else:
        print("EOF  null") 


if __name__ == "__main__":
    main()
