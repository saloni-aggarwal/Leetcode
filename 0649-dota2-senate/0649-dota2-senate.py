class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        # print("\n\nSTARTING NEW")
        rCnt, dCnt = 0, 0
        
        for s in senate:
            if s == 'R':
                rCnt += 1
            else:
                dCnt += 1
                
        def banOpponent(toBan, startFrom):
            while True:
                if not banned[startFrom] and senate[startFrom] == toBan:
                    banned[startFrom] = True
                    break
                startFrom = (startFrom + 1) % len(senate)
        
        banned = [False] * len(senate)
        i = 0
        while rCnt > 0 and dCnt > 0:
            if not banned[i]:
                if senate[i] == 'R':
                    banOpponent('D', i)
                    dCnt -= 1
                else:
                    banOpponent('R', i)
                    rCnt -= 1
            i = (i + 1) % len(senate)
            
        return "Radiant" if rCnt != 0 else "Dire"
                    
            
                
            