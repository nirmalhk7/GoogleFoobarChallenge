
def solution(x, y):
    ptrX,ptrY=1,1
    expoIncr=1
    incr=2
    shiftCountX=1
    while shiftCountX<x:
        ptrX+=incr
        incr+=1
        shiftCountX+=1
   # print("X",ptrX,shiftCountX)
    incr=shiftCountX
    expoIncr=1
    shiftCountY=1
    ptrY=ptrX
    while shiftCountY<y:
        ptrY+=incr
        incr+=1
        shiftCountY+=1
  #      print("Y",ptrY,shiftCountY)

    

# | 11
# | 7 12
# | 4 8 13
# | 2 5 9 14
# | 1 3 6 10 15 


if __name__ == "__main__":
    print(solution(2,3))
    print(solution(3,3))
    print(solution(3,2))
    print(solution(4,5))
    print(solution(2,4))
    print(solution(5,10))