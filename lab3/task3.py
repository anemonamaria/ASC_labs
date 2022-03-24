from random import choice, seed
from concurrent.futures import ThreadPoolExecutor

def find_seq(data):
    index = data[0]
    sample = data[1]
    seq = data[2]

    if not sample.find(seq) == -1:
        return "DNA sequence found in sample " + str(index)

    return ""

if __name__ == "__main__":
    samples = []
    for i in range(100):
        seed(i)
        samples.append("".join([choice("ACGT") for i in range(10000)]))

    seq = "ACGTACG"
    data = [(index, samples[index], seq) for index in range(100)]

    with ThreadPoolExecutor(max_workers=30) as executor:
        results = executor.map(find_seq, data)

    for result in results:
        if not result == "":
            print(result)
