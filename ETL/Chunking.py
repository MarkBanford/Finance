'''the DataFrame is divided into chunks using the shape attribute and a list comprehension.
Each chunk is passed as an argument to a separate thread, which multiplies all values in the chunk by 2 and stores the
result in a list. Once all threads have completed, the results are concatenated into a single DataFrame using the
concat function. This allows the row operations to be performed concurrently, improving the performance of the
program.'''

import pandas as pd
import threading


def process_chunk(chunk):
    # Multiply all values in the chunk by 2
    chunk *= 2
    return chunk


# Load the DataFrame
df = pd.read_csv('data.csv')

# Divide the DataFrame into chunks
chunks = [df[i:i + 1000] for i in range(0, df.shape[0], 1000)]

# Create a list to store the results
results = []

# Create a thread for each chunk
threads = []
for chunk in chunks:
    thread = threading.Thread(target=process_chunk, args=(chunk,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Concatenate the results into a single DataFrame
df = pd.concat(results)
