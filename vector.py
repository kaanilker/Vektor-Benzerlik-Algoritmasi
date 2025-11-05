import numpy

def arrange(item, dim,min,max):

    item_count,i = len(item),0

    for i in range(dim):
        if(i <= item_count):
            item[i] = item[i] / ((max - min) / 100)
        else:
            item[i] = 50 / ((max - min) /100)
    return item 

def kokal(x):
    return x**(1/2)

def usal(x,level):
    return x**level

kirmizi = [255,0,0]
koyuKirmizi = [181,25,25]
kahverengi = [48,34,15]
siyah = [0,0,0]
beyaz = [255,255,255]
gri = [82,82,82]

def normalize(renk):
    renk_normalized = arrange(renk, 3,0,255)
    return renk_normalized

print(normalize(gri))

def vectorSimilarty(A,B):
    if len(A) != len(B):
        return -1
    else:
        len_ = len(A)
        total = 0
        for i in range (len_):
            total += usal(B[i] - (A[i]), 2)
        distance = kokal(total)

    max_dist = 0
    for i in range(len_):
        max_dist += usal(100,2)
    max_dist = kokal(max_dist)

    return 1- (distance / max_dist)

benzerlik_orani = vectorSimilarty(normalize(kirmizi),normalize(koyuKirmizi))
benzerlik_yuzdesi = benzerlik_orani * 100
print("%",benzerlik_yuzdesi)
