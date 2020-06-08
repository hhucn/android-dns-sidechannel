import time
from timeit import default_timer as timer

import numpy as np
from dns.resolver import query
from dns.reversename import from_address

SAMPLE_SIZE = 100


def process_request():
    start_time = timer()
    try:
        response = query(from_address("8.8.8.8"), "PTR")
        for data in response:
            print(data)
    except Exception as e:
        print(e)

    end_time = timer()
    return (end_time - start_time) * 1000.0


def main():
    sample_list = np.ndarray(SAMPLE_SIZE)
    for i in range(SAMPLE_SIZE):
        sample_list[i] = process_request()
        time.sleep(0.1)

    print(f"Average request time: {sample_list.mean()} ms")
    print(f"Standart deviation: {sample_list.std()} ms")
    print("Samples:")
    for sample in sample_list:
        print(str(sample))


if __name__ == "__main__":
    main()
