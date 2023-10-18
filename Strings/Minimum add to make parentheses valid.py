class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for it in s:
            if it == '(':
                st.append(it)
            else:
                if (len(st) and st[-1] == '('):
                    st.pop()
                else:
                    st.append(it)
        return len(st)
