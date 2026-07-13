class Solution:
    def isValid(self, s: str) -> bool:
        validPair = {")" : "(", "]" : "[", "}" : "{", ">": "<"}
        st = []

        for ch in s:
            if ch in validPair:
                if st and st[-1] == validPair[ch]:
                    st.pop()
                else:   
                    return False
            else:
                st.append(ch)
        
        return True if not st else False