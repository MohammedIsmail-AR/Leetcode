class Solution(object):
    def maxProfit(self, prices):
        min_pro = prices[0]
        max_pro = 0

        for price in prices :
            if price < min_pro :
                min_pro = price
            if price - min_pro > max_pro :
                max_pro = price - min_pro
        return max_pro








        

                
            



                


        





            


        






        



        