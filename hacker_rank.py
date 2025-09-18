if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    rank1=0
    rank2=0
    for i in arr:
        if i>rank1:
            rank2=rank1
            rank1=i
        elif i>rank2 and i<rank1:
            rank2=i
    print(rank2)
        

    
