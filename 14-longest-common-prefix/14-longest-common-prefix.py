class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        ans= ""
        i = 0
        while i<200:   #gievn maximum characters in each string is 200 so iterating upto 200
            j = 0
            while j<n:  #for each ith character iterating over all the n strings
                try:
                    if strs[j][i] == strs[0][i]:  #if equal move onto next string and compare
                        j+=1
                        continue
                    else:                           #if not equal curretn ans will be returned
                        return ans
                except:                          #if any of the string ends at any point ans can be returned as                                                    #prefix can be of legth atmost the length of min size string
                    return ans
                j+=1
            ans+=strs[0][i]                     #if iterates over all strings and comes out then we can add ith charactyer to ans
            i+=1
        return ans