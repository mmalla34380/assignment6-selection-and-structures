import time
import random
import matplotlib.pyplot as plt
from deterministic_select import deterministic_select
from randomized_select import randomized_select

def test_selection_algorithms():
    input_sizes = [100, 500, 1000, 2000, 5000, 10000]
    rand_times, det_times = [], []

    for size in input_sizes:
        arr1 = [random.randint(1, size) for _ in range(size)]
        arr2 = arr1.copy()
        k = size // 2

        start = time.time()
        randomized_select(arr1, 0, len(arr1) - 1, k)
        rand_times.append(time.time() - start)

        start = time.time()
        deterministic_select(arr2, k)
        det_times.append(time.time() - start)

        print(f"n={size} | Randomized: {rand_times[-1]:.5f}s | Deterministic: {det_times[-1]:.5f}s")

    plt.plot(input_sizes, rand_times, label="Randomized Quickselect", marker='o')
    plt.plot(input_sizes, det_times, label="Deterministic Select", marker='x')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (s)")
    plt.title("Selection Algorithm Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    test_selection_algorithms()
