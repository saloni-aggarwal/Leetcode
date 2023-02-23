class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                res += 'G'
            elif command[i] == '(':
                temp = 0
                while command[i] != ')':
                    temp += 1
                    i += 1
                if temp ==  1:
                    res += 'o'
                else:
                    res += "al"
            i += 1
        return res
            
        