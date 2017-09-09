def solution(S):
    
    longest = 0
    prefixes = []
    suffixes = []
    length = len(S)
    
    for i in range(1, length):
        prefixes.append(S[0:i])
        suffixes.append(S[i:length])
        
    for p in prefixes:
        if p in suffixes and len(p) > longest:
            longest = len(p)
            
    return longest
