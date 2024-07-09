import sys

def scanner(data):
    res=""
    for i in data:
        if i=='(':
            res+="LEFT_PAREN ( null\n"
        elif i==')':
            res+="RIGHT_PAREN ) null\n"
        if i=='{':
            res+="LEFT_BRACE { null\n"
        elif i=='}':
            res+="RIGHT_BRACE } null\n"
        elif i==',':
            res+="COMMA , null\n"
        elif i=='.':
            res+="DOT . null\n"
        elif i=='*':
            res+="STAR * null\n"
        elif i=='+':
            res+="PLUS + null\n"
        elif i=='-':
            res+="MINUS - null\n"
        elif i==';':
            res+="SEMICOLON ; null\n"
        elif i=='/':
            res+="FORWARD_SLASH / null\n"
    print(res+"EOF  null")
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

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
