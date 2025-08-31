class Solution:
    def intToRoman(self, num: int) -> str:
        pair=[(3000,"MMM"),(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
        List=[]
        for val,sym in pair:
            while num>=val:
                num=num-val
                List.append(sym)
        return "".join(List)