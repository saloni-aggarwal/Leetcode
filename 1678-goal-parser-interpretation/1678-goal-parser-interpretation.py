class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        i = 0
        while i < len(command):
            # print("i =", i, "command[i] =", command[i])
            if command[i] == 'G':
                res += 'G'
            elif command[i] == '(':
                temp = 0
                while command[i] != ')':
                    temp += 1
                    i += 1
                # print("temp =", temp)
                if temp ==  1:
                    # print("in if")
                    res += 'o'
                else:
                    # print("in else")
                    res += "al"
            i += 1
        return res
            
        