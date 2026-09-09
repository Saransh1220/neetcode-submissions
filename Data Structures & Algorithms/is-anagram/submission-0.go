func isAnagram(s string, t string) bool {
    count:= make(map[byte]int)
    if len(s)!=len(t){
        return false
    }
    for i:=0;i<len(s);i++{
        ch :=s[i]
        count[ch]++
    }

    for i:=0;i<len(t);i++{
        count[t[i]]--
        if count[t[i]]<0{
            return false
        }
    }
    return true
}
