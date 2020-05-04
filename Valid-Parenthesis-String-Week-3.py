class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftnwild = 0

        for i in s:

            if(i == ')'):

                if(leftnwild == 0):
                    return False

                else:
                    leftnwild -= 1

            else:
                leftnwild += 1

        s = reversed(s)
        rightnwild = 0

        for i in s:

            if(i == '('):

                if(rightnwild == 0):
                    return False

                else:
                    rightnwild -= 1

            else:
                rightnwild += 1


        return True