# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, M, X, Y):
    
    stops = []
    weight = 0
    start = 0
    counter = 0
    
    for indx, i in enumerate(A):
        weight += i
        
    if weight >= Y or indx % M ==0:
        stops.append(B[start:indx])
        start = indx
        weight = 0
    # else:
    #     pass
    
    stops.append(B[start:])
    stops.pop(0)
    
    for stop in stops:
        counter += len(set(stop))
    counter += len(stops)
    
    return counter