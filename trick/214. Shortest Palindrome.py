class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sps = s+"#"+s[-1::-1] # s[-1::-1]+"#"+s
        tbl = self.getTable(sps)
        return s[tbl[-1]:][-1::-1] + s

    def getTable(self, s):
        tbl = [0]*len(s)
        idx = 0
        for i in range(1,len(s)):
            if s[idx] == s[i]:
                tbl[i] = tbl[i-1] + 1
                idx += 1
            else:
#                       idx          i
#                a   b   x   a   b   c
#                0   0   0   1   2   0
#
                idx = tbl[i-1]

#                        idx           i
#                abcd abcx ... abcd abcd ...
#                   idx                i
#                01234123              idx=4

                while idx>0 and not s[idx] == s[i]:
                    idx = tbl[idx-1]
                if s[idx] == s[i]:
                    idx += 1
                tbl[i] = idx
        print (tbl)
        return tbl

'''
// java KMP
public String shortestPalindrome(String s) {
    String temp = s + "#" + new StringBuilder(s).reverse().toString();
    int[] table = getTable(temp);

    //get the maximum palin part in s starts from 0
    return new StringBuilder(s.substring(table[table.length - 1])).reverse().toString() + s;
}

public int[] getTable(String s){
    //get lookup table
    int[] table = new int[s.length()];

    //pointer that points to matched char in prefix part

    int index = 0;
    //skip index 0, we will not match a string with itself
    for(int i = 1; i < s.length(); i++){
        if(s.charAt(index) == s.charAt(i)){
            //we can extend match in prefix and postfix
            table[i] = table[i-1] + 1;
            index ++;
        }else{
            //match failed, we try to match a shorter substring

            //by assigning index to table[i-1], we will shorten the match string length, and jump to the
            //prefix part that we used to match postfix ended at i - 1
            index = table[i-1];

            while(index > 0 && s.charAt(index) != s.charAt(i)){
                //we will try to shorten the match string length until we revert to the beginning of match (index 1)
                index = table[index-1];
            }

            //when we are here may either found a match char or we reach the boundary and still no luck
            //so we need check char match
            if(s.charAt(index) == s.charAt(i)){
                //if match, then extend one char
                index ++ ;
            }

            table[i] = index;
        }

    }

    return table;
}
'''
