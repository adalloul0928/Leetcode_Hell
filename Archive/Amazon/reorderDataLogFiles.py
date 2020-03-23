class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        A, B, G = [], [], [i.split() for i in logs]
        for wordString in G:
            if wordString[1].isdigit():
                A.append(wordString)
            else:
                B.append(wordString)
        return [" ".join(i) for i in sorted(B, key=lambda x: x[1:] + [x[0]]) + A]



