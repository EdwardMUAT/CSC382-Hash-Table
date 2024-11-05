import sys
import time
import random
import string

class HashTable:
    def __init__(self, num_buckets):
        self.table = [[] for _ in range(num_buckets)]
        self.num_buckets = num_buckets
    
    def _hash(self, state):
        return hash(state) % self.num_buckets

    def insert(self, registration):
        index = self._hash(registration['state'])
        self.table[index].append(registration)

    def retrieve(self, registration_id):
        for bucket in self.table:
            for reg in bucket:
                if reg['registration_id'] == registration_id:
                    return reg
        return None

    def print_all(self):
        for bucket in self.table:
            for reg in sorted(bucket, key=lambda x: x['name']):
                print(reg)

# Generate sample registrations
def generate_dataset(num_entries=1000):
    dataset = []
    states = ["CA", "TX", "NY", "FL", "IL"]
    for i in range(num_entries):
        entry = {
            "registration_id": i + 1,
            "name": ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5)),
            "state": random.choice(states),
            "email": f"user{i}@example.com"
        }
        dataset.append(entry)
    return dataset

# Measure insertion time
def measure_time(num_buckets, dataset):
    hash_table = HashTable(num_buckets)
    start_time = time.time()
    for data in dataset:
        hash_table.insert(data)
    end_time = time.time()
    print(f"Time taken for {num_buckets} buckets: {end_time - start_time:.4f} seconds")

# Main program function
def main():
    # Check if a specific number of buckets is provided as a command-line argument
    if len(sys.argv) > 1:
        try:
            num_buckets = int(sys.argv[1])
            if num_buckets <= 0:
                raise ValueError
            print(f"\n--- Hash Table with {num_buckets} Buckets ---")
            dataset = generate_dataset()
            measure_time(num_buckets, dataset)
        except ValueError:
            print("Please provide a valid positive integer for <num_buckets>.")
    else:
        # Run with 10, 100, and 1000 buckets by default if no argument is given
        dataset = generate_dataset()
        for num_buckets in [10, 100, 1000]:
            print(f"\n--- Hash Table with {num_buckets} Buckets ---")
            measure_time(num_buckets, dataset)

# Run the main function
if __name__ == "__main__":
    main()
