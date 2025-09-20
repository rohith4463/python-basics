def count_substring(string, sub_string):
    l=list(string)
    n=len(l)
    l1=[]
    count=0
    for i in range(n):
        for j in range(i+1,n+1):
            a=l[i:j]
            b="".join(a)
            
            l1.append(b)
            
        
    for i in l1:
        if i==sub_string:
            count+=1   
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
