class TUF:
    @staticmethod
    def isalpha(c):
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            return True
        return False

    @staticmethod
    def isdigit(c):
        if '0' <= c <= '9':
            return True
        return False

    @staticmethod
    def isOperator(c):
        return not (TUF.isalpha(c) or TUF.isdigit(c))

    @staticmethod
    def getPriority(C):
        if C == '-' or C == '+':
            return 1
        elif C == '*' or C == '/':
            return 2
        elif C == '^':
            return 3
        return 0

    @staticmethod
    def infixToPostfix(infix1):
        print(infix1)
        infix = '(' + infix1 + ')'

        l = len(infix)
        char_stack = []
        output = ""

        for i in range(l):
            if TUF.isalpha(infix[i]) or TUF.isdigit(infix[i]):
                output += infix[i]
            elif infix[i] == '(':
                char_stack.append('(')
            elif infix[i] == ')':
                while char_stack[-1] != '(':
                    output += char_stack.pop()
                char_stack.pop()
            else:
                if TUF.isOperator(char_stack[-1]):
                    while (TUF.getPriority(infix[i]) < TUF.getPriority(char_stack[-1])) or \
                          (TUF.getPriority(infix[i]) <= TUF.getPriority(char_stack[-1]) and infix[i] == '^'):
                        output += char_stack.pop()
                    char_stack.append(infix[i])
        while char_stack:
            output += char_stack.pop()
        return output

    @staticmethod
    def infixToPrefix(infix):
        l = len(infix)
        infix1 = infix[::-1]
        infix = list(infix1)
        for i in range(l):
            if infix[i] == '(':
                infix[i] = ')'
                i += 1
            elif infix[i] == ')':
                infix[i] = '('
                i += 1
        prefix = TUF.infixToPostfix(''.join(infix))
        prefix = prefix[::-1]
        return prefix

    @staticmethod
    def main():
        s = "(p+q)*(c-d)"
        print("Infix expression: " + s)
        print("Prefix expression: " + TUF.infixToPrefix(s))

if __name__ == "__main__":
    TUF.main()
