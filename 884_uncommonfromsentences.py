class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        set1 = set()
        set2 = set()
        new = []

        slist = s1.split(" ")
        slist1 = s2.split(" ")

        for i in slist: 
            set1.add(i)

        for j in slist1:
            set2.add(j)

        for j in slist1: 
            if j not in set1: 
                if slist1.count(j) == 1: 
                    new.append(j)

        for j in slist: 
            if j not in set2: 
                if slist.count(j) == 1: 
                    new.append(j)      
        return new