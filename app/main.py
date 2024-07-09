import sys

def scanner(data):
    res=""
    error_code=0
    lines=1
    for i,ch in enumerate(data):
        if ch=='(':
            res+="LEFT_PAREN ( null\n"
        elif ch==')':
            res+="RIGHT_PAREN ) null\n"
        elif ch=='{':
            res+="LEFT_BRACE { null\n"
        elif ch=='}':
            res+="RIGHT_BRACE } null\n"
        elif ch==',':
            res+="COMMA , null\n"
        elif ch=='.':
            res+="DOT . null\n"
        elif ch=='*':
            res+="STAR * null\n"
        elif ch=='+':
            res+="PLUS + null\n"
        elif ch=='-':
            res+="MINUS - null\n"
        elif ch==';':
            res+="SEMICOLON ; null\n"
        elif ch=='/':
            res+="FORWARD_SLASH / null\n"
        elif ch=='\n':
            lines+=1
        else:
            error_code=65
            
            print(f"[line {lines}] Error: Unexpected character: {ch}", file=sys.stderr)
            

    print(res+"EOF  null")
    exit(error_code)
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    if file_contents:
        scanner(file_contents)
    else:
        print("EOF  null") 


if __name__ == "__main__":
    main()
