import random

def test_print():
	print("hello")

def test_get_array():
	A = []
	for i in range(100):
		A.append(int(random.random()*100))
	return A

def test_get_sorted_array():
	A = []
	for i in range(100):
		A.append(int(random.random()*100))
	return insertion_sort2(A)

def test_get_sorted_array_unique():
	A = []
	for i in range(100):
		A.append(int(random.random()*100))
	A = insertion_sort2(A)
	A = unique_array(A)
	return A

def unique_array(A):
	newA = []
	for i in A:
		if i not in newA:
			newA.append(i)
	return newA


def insertion_sort2(A):
    B = A.copy()
    for i in range(1,len(B)):
        temp = B[i]
        end = False
        for j in range(i-1,-1,-1):
            if B[j] > temp:
                B[j+1] = B[j]
            else:
                B[j+1] = temp
                end = True
                break
        if not end:
            B[1] = B[0]
            B[0] = temp
    return B

def __init__():
	pass