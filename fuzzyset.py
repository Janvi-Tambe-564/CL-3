A = {"x1":0.2, "x2" :0.3, "x3":0.5}
B = {"x1":0.6, "x2" :0.4, "x3":0.8}

def union_set(A,B):
    union={}
    for x in A:
        union[x]=max(A[x], B[x])
    return union

print(f"Union of Fuzzy sets : {union_set(A, B)}")

def intersection_Set(A,B):
    intersection={}
    for r in A:
        intersection[r]=min(A[r], B[r])
    return intersection

print(f"Intersection of Fuzzy sets : {intersection_Set(A, B)}")

def complement(A):
    complement={}
    for w in A:
        complement[w]=1-A[w]
    return complement

print(f"Intersection of Fuzzy sets : {complement(A)}")

def difference(A,B):
    difference={}
    for d in A:
        difference[d]=min(A[d],1-B[d])
    return difference

print(f"Differnce of fuzzy sets : {difference(A,B)}")
print(f"Differnce of fuzzy sets : {difference(B,A)}")

def cartesian_product(A,B):
    cartesian_product={}
    for a in A:
        for b in B:
            cartesian_product[(a,b)]=min(A[a],B[b])
    return cartesian_product

print(f"Cartesian product : {cartesian_product(A, B)}")

R = {
    ('x','p'): 0.2,
    ('x','q'): 0.6,
    ('y','p'): 0.5,
    ('y','q'): 0.3
}

S = {
    ('p','u'): 0.7,
    ('p','v'): 0.4,
    ('q','u'): 0.5,
    ('q','v'): 0.8
}

def max_min(R,S):
    result={}
    for (a,b1) in R:
        for (b1,c) in S:
            if b1==b1:
                key=(a,c)
                value=min(R[(a,b1)],S[(b1,c)])
            if key in result:
                result[key]=max(result[key],value)
            else:
                result[key]=value
    return result

print(f"Max-min composition: {max_min(R,S)}")
