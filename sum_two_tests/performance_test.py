from time import time
from sum_two import is_sum_two1, is_sum_two2

if __name__ == '__main__':
    large_numbers = list(range(10000))
    print(f'Testing with {len(large_numbers)} numbers')
    target_sum = 20000
    # Testing is_sum_two1
    start_time = time()
    result = is_sum_two1(large_numbers, target_sum)
    end_time =time()
    print(f'is_sum_two1 time: {end_time-start_time}, result:{result}')
    # Testing is_sum_two2
    start_time = time()
    result = is_sum_two2(large_numbers, target_sum)
    end_time = time()
    print(f'is_sum_two2 time: {end_time - start_time}, result:{result}')
