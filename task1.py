import time

def sum_range(n: int) -> int:
    return (1 + n) * n // 2


if __name__ == "__main__":
    n = int(input("Enter a number: "))

    st = time.time()
    print(f"Sum from 1 to {n} is {sum_range(n)}")
    print(f"Time taken: {time.time() - st} seconds")