# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    A.sort()
    left_index = len(A) // 3 - 1
    right_index = - len(A) // 3
    left_shift_count = 1
    right_shift_count = 1
    while K > 0:
        if left_index == 0:
            return A[right_index] - A[left_index] + K // left_shift_count
        if right_index == -1:
            return A[right_index] - A[left_index] + K // right_shift_count

        shift = min(K // left_shift_count, (A[left_index] - A[left_index - 1]) * left_shift_count)
        A[left_index] -= shift
        if K <= A[left_index] - A[left_index - 1]:
            if K == 0:
                return A[right_index] - A[left_index]
            else:
                K -= shift * left_shift_count
        else:
            left_index -= 1
            K -= shift * left_shift_count
            left_shift_count += 1

        shift = min(K // right_shift_count, (A[right_index + 1] - A[right_index]) * right_shift_count)
        A[right_index] += shift
        if K <= A[right_index + 1] - A[right_index]:
            if K == 0:
                return A[right_index] - A[left_index]
            else:
                K -= shift * right_shift_count
        else:
            right_index += 1
            K -= shift * right_shift_count
            right_shift_count += 1

    return A[right_index] - A[left_index]

A = [7,6,3,2,2,2,2,2,2,2,2,1]
K = 5

print(solution(A, K))