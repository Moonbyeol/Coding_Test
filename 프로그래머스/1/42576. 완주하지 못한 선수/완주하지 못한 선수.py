def solution(participant, completion):
    H={}
    s=0
    for p in participant:
        H[hash(p)]= p
        s+=hash(p)
    for c in completion:
        s-=hash(c)
    return H[s]