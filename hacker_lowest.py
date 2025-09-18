if __name__ == '__main__':
    result=[]
    grades=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a=[name,score]
        result.append(a)
        grades.append(score)
    grades=list(set(grades))
        
    grades.sort()
    second_lowest=(grades[1])
    result.sort()
    for i in result:
        if i[1]==second_lowest:
             print(i[0])
           
