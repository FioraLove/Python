class Solution(object):
    def numJewelsInStones(self, J, S):
        num = 0
        for i in J:
            num +=S.count(i)
        return num
def main():
    response =Solution()
    result=response.numJewelsInStones('aA','aAAbasbdagdyagaaaDHHDHHAAbu')
    print(result)
if __name__ == '__main__':
        main()
