#1- Fab

def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

n = 5
print(f"The {n}th Fibonacci number is:", Fibonacci(n))


#2- print

def print_numbers(N):
    for i in range(1, N + 1):
        print(i)

N = 10  
print_numbers(N)


#3-def print_digits(N):
    if N < 10:
        
        print(N, end=" ")
    else:
        
        print_digits(N // 10)  # Integer division to remove the last digit
        print(N % 10, end=" ")  # Print the last digit

N = 12345
print_digits(N)  


#4- array 

def calculate_average(arr, n):
    if n == 0:
        return 0  
    else:
        
        return (arr[n - 1] + calculate_average(arr, n - 1) * (n - 1)) / n


N = 5
array_A = [10, 20, 30, 40, 50]
average = calculate_average(array_A, N)
print(f"The average of the numbers in array A is: {average:.6f}")


#5- 3n+1 

def collatz_sequence_length(n):
    if n == 1:
        return 1  
    elif n % 2 == 0:
        return 1 + collatz_sequence_length(n // 2)  
    else:
        return 1 + collatz_sequence_length(3 * n + 1)  


n = 3
sequence_length = collatz_sequence_length(n)
print(f"Length of the 3n+1 sequence starting with {n} is: {sequence_length}")


#6- reaoh

def can_reach_N(current_value, N):
    if current_value == N:
        return True  
    elif current_value > N:
        return False  
    else:
        
        return can_reach_N(current_value * 10, N) or can_reach_N(current_value * 20, N)


N = 2
initial_value = 1
if can_reach_N(initial_value, N):
    print(f"YES")
else:
    print(f"NO")


#7- knapsack

def knapSack(W, wt, val, n):
    
    if n == 0 or W == 0:
        return 0
    
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)
    
    return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
               knapSack(W, wt, val, n - 1))


profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50
N = len(profit)
max_value = knapSack(W, weight, profit, N)
print(f"Maximum value that can be carried in the knapsack: {max_value}")

#8- path-sum

def maximum_sum_path(matrix, i, j):
    
    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        return matrix[i][j]
    
    
    right_sum = float('-inf')
    down_sum = float('-inf')
    
    
    if j < len(matrix[0]) - 1:
        right_sum = maximum_sum_path(matrix, i, j + 1)
    
    
    if i < len(matrix) - 1:
        down_sum = maximum_sum_path(matrix, i + 1, j)
    
    
    return matrix[i][j] + max(right_sum, down_sum)


matrix = [
    [1, 2, 3],
    [9, 8, 7],
    [4, 5, 6]
]

max_sum = maximum_sum_path(matrix, 0, 0)
print({max_sum})


#9- subseq

def is_subsequence(A, B):
    i, j = 0, 0  
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            j += 1  
        i += 1  
    return j == len(B)  


A = [1, 6, 3, 7]
B = [1, 4, 7]
if is_subsequence(A, B):
    print("B is a sub-sequence of A.")
else:
    print("B is not a sub-sequence of A.")


#10- permutation

def is_permutation(A, B):
    
    freq_A = {}
    freq_B = {}

    
    for num in A:
        freq_A[num] = freq_A.get(num, 0) + 1

   
    for num in B:
        freq_B[num] = freq_B.get(num, 0) + 1

    
    return freq_A == freq_B


A = [1, 2, 3]
B = [2, 1, 3]
if is_permutation(A, B):
    print("B is a permutation of A.")
else:
    print("B is not a permutation of A.")


#11- minimize

def max_operations(A):
    # Initialize a counter for the number of operations
    operations = 0
    
    # Check if all numbers in A are even
    all_even = all(num % 2 == 0 for num in A)
    
    while all_even:
        # Divide each number in A by 2
        A = [num // 2 for num in A]
        operations += 1
        all_even = all(num % 2 == 0 for num in A)
    
    return operations

# Example usage:
N = 5
array_A = [16, 8, 4, 2, 6]
max_ops = max_operations(array_A)
print(f"Maximum possible operations: {max_ops}")


#12- minmax

def swap_min_max(arr):
    
    min_num = min(arr)
    max_num = max(arr)
    
    
    min_index = arr.index(min_num)
    max_index = arr.index(max_num)
    arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
    
    return arr


N = 5
array_A = [10, 5, 8, 3, 12]
result = swap_min_max(array_A)
print(result)


#13- max subarray

def max_in_subarrays(arr):
    n = len(arr)
    max_values = []  

    
    for i in range(n):
        max_val = float('-inf')  
        for j in range(i, n):
            max_val = max(max_val, arr[j])  
            max_values.append(max_val)  

    return max_values


N = 4
array_A = [1, 6, 3, 7]
result = max_in_subarrays(array_A)
print(*result)  


#14- smallest pair 

def smallest_sum(N, A):
    
    min_sum = float('inf')
    
   
    for i in range(N):
        for j in range(i + 1, N):
            curr_sum = A[i] + A[j] + j - i
            min_sum = min(min_sum, curr_sum)
    
    return min_sum


T = int(input().strip())

for _ in range(T):
    
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    
    
    result = smallest_sum(N, A)
    print(result)


#15-check code 

def check_code(S, A, B):
    
    if len(S) != A + B + 1:
        return "No"
    
    
    if S[A] != '-':
        return "No"
    
    
    for i in range(A + B + 1):
        if i != A and not S[i].isdigit():
            return "No"
    
    return "Yes"


A, B = map(int, input().strip().split())


S = input().strip()


result = check_code(S, A, B)
print(result)


#16- 5 in one

def get_max(arr):
    return max(arr)
def get_min(arr):
    return min(arr)
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(arr):
    return sum(1 for num in arr if is_prime(num))
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(arr):
    return sum(1 for num in arr if is_prime(num))
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def count_palindromes(arr):
    return sum(1 for num in arr if is_palindrome(num))
def count_divisors(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    return count

def max_divisor_count(arr):
    max_divisors = 0
    max_num = None
    for num in arr:
        divisors = count_divisors(num)
        if divisors > max_divisors:
            max_divisors = divisors
            max_num = num
    return max_num


#17- swapping with matrix

def swap_rows(matrix, X, Y):
    matrix[X], matrix[Y] = matrix[Y], matrix[X]

def swap_columns(matrix, X, Y):
    for row in matrix:
        row[X], row[Y] = row[Y], row[X]

def print_matrix(matrix):
    for row in matrix:
        print(*row)


N = 3  
matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

X = 0  
Y = 2  
swap_rows(matrix_A, X, Y)

X = 1  
Y = 2  
swap_columns(matrix_A, X, Y)


print_matrix(matrix_A)


#18- xor 

def calculate_value(A, B, Q):
    if Q == 1:
        return A
    elif Q == 2:
        return B
    else:
        F_Q_minus_1 = calculate_value(A, B, Q - 1)
        F_Q_minus_2 = calculate_value(A, B, Q - 2)
        return F_Q_minus_1 & F_Q_minus_2


A = 5
B = 3
Q = 2
result = calculate_value(A, B, Q)
print(result)

#19- convert to base 

def base_to_decimal(N, X):
    decimal_value = 0
    for char in N:
        if char.isdigit():
            decimal_value = decimal_value * X + int(char)
        else:
            decimal_value = decimal_value * X + ord(char) - ord('A') + 10
    return decimal_value

def decimal_to_base(N, X):
    result = ""
    while N > 0:
        digit = N % X
        if digit < 10:
            result = str(digit) + result
        else:
            result = chr(ord('A') + digit - 10) + result
        N //= X
    return result

T = int(input().strip())
N, X = input().strip().split()

if T == 1:
    decimal_value = base_to_decimal(N, int(X))
    print(decimal_value)
elif T == 2:
    decimal_number = int(N)
    base_X_value = decimal_to_base(decimal_number, int(X))
    print(base_X_value)
else:
    print("Invalid value of T. Please choose 1 or 2.")


#20- multi of matrix


RA, CA = map(int, input().split())
matrix_A = [list(map(int, input().split())) for _ in range(RA)]


RB, CB = map(int, input().split())
matrix_B = [list(map(int, input().split())) for _ in range(RB)]


result_matrix = [[0] * CB for _ in range(RA)]


for i in range(RA):
    for j in range(CB):
        for k in range(CA):
            result_matrix[i][j] += matrix_A[i][k] * matrix_B[k][j]


for row in result_matrix:
    print(*row)


#21- comination

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)


A, B = map(int, input().split())


G = gcd(A, B)
L = lcm(A, B)


print(f"GCD: {G} LCM: {L}")


 #22- ciroles

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def main():
    X1, Y1, X2, Y2 = map(int, input().split())
    X3, Y3, X4, Y4 = map(int, input().split())

    
    X_A, Y_A = (X1 + X2) / 2, (Y1 + Y2) / 2
    X_B, Y_B = (X3 + X4) / 2, (Y3 + Y4) / 2

    
    d = distance(X_A, Y_A, X_B, Y_B)

    
    r_A = d / 2
    r_B = d / 2

    
    if r_A + r_B >= d:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()

#23- common area

def compute_intersection_area(rectangles):
    
    common_area = (rectangles[0][2] - rectangles[0][0]) * (rectangles[0][3] - rectangles[0][1])

    
    for rect in rectangles[1:]:
        x1, y1, x2, y2 = rect
        common_area = max(0, min(common_area, (x2 - x1) * (y2 - y1)))

    return common_area

def main():
    T = int(input())  

    for case in range(1, T + 1):
        N = int(input())  
        rectangles = [tuple(map(int, input().split())) for _ in range(N)]

        
        area = compute_intersection_area(rectangles)

        print(f"Case #{case}: {area}")

if __name__ == "__main__":
    main()

#24 - big add and multi

def compute_intersection_area(rectangles):
    
    common_area = (rectangles[0][2] - rectangles[0][0]) * (rectangles[0][3] - rectangles[0][1])

    
    for rect in rectangles[1:]:
        x1, y1, x2, y2 = rect
        common_area = max(0, min(common_area, (x2 - x1) * (y2 - y1)))

    return common_area

def main():
    T = int(input())  

    for case in range(1, T + 1):
        N = int(input())  
        rectangles = [tuple(map(int, input().split())) for _ in range(N)]

        
        area = compute_intersection_area(rectangles)

        print(f"Case #{case}: {area}")

if __name__ == "__main__":
    main()

