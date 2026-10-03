class Solution(object):
    def frequencySort(self, s):
       result = ""
       count = {}

       for ch in s:
        count[ch] = count.get(ch,0) + 1

       chars = sorted(count, key=count.get, reverse = True)

       for ch in chars:
            result += ch * count[ch]

       return result


    
        