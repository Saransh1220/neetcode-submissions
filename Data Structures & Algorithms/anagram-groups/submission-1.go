func groupAnagrams(strs []string) [][]string {
    group:=make(map[string][]string)
    for i:=0;i<len(strs);i++{
       
        ch:= sortStrings(strs[i])
        group[ch]=append(group[ch],strs[i])

    }
    res := [][]string{}

    for _, val:= range group{
        res = append(res,val)
    }
    return res
}


func sortStrings(s string) string{
    b:=[]byte(s)
    for i :=0;i<len(b)-1;i++{
        for j:=0;j<len(b)-1;j++{
            if b[j]>b[j+1]{
                b[j],b[j+1]=b[j+1],b[j]
            }
        }
    }
    return string(b)
}