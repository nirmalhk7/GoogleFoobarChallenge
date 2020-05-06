import operator

def solution(A):
    VListForm=[]
    for i in range(len(A)):
        minilist=(list(map(int,A[i].split('.'))))
        if(len(minilist)==2):
            minilist.append(-1)
        elif(len(minilist)==1):
            minilist.append(-1)
            minilist.append(-1)
        VListForm.append(minilist)
    VListForm=sorted(VListForm,key=operator.itemgetter(0,1,2))
  #  print(VListForm)
    VStrArrayForm=[]
    for i in range(len(VListForm)):
        stx=str(VListForm[i][0])
        if(VListForm[i][1]!=-1):
            stx+="."+str(VListForm[i][1])
        if(VListForm[i][2]!=-1):
            stx+="."+str(VListForm[i][2])
        VStrArrayForm.append(stx)
    return VStrArrayForm

if __name__ == "__main__":
    print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
    print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))