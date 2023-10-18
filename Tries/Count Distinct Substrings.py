def countDistinctSubstrings(s):
    st=set()
    for i in range(len(s)):
        ss=""
        st.add('')
        for j in range(i,len(s)):
            ss=ss+s[j]
            st.add(ss)
    return len(st)
