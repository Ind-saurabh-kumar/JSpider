class Solution:

    def halfRev(self, str):
        stri=list(str)
        l=len(stri)

        stri[l//2]=stri[0]
        stri.pop(0)
        strs=''
        for i in stri:
            strs+=i
        print(strs)


    def halfRevStr(self, str):
        s=str

        l=len(s)
        sn=s.replace(s[l//2], s[0])
        print(sn)



s=Solution()
# s.halfRevStr("String")

s.halfRev(("string"))