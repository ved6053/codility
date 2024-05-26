'''
MissingInteger
This is a demo task.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
def find_missing_integer(A):
    N = max(max(A), len(A))+1
    missing_flag = [True for _ in range(N)]
    for ele in A: 
        if ele>0 and ele<=N:
            op = ele-1
            missing_flag[op] = False
    try:
        return missing_flag.index(True)+1
    except ValueError:
        return 1

if __name__=='__main__':
    print(find_missing_integer([1, 3, 6, 4, 1, 2]))
