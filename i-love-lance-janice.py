# Problem for Stage 1
def solution(A):
    opx=""
    for i in range(len(A)):
        if(A[i].islower()):
            n=123-ord(A[i])
            opx+=chr(n+96)
        else: opx+=A[i]
    return opx

if __name__ == "__main__":
    print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
    print(solution("vmxibkgrlm"))
    print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
    print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
    print(solution("abcdefghijklmnopqrstuvwxyz1234567890-=[];',./`"))