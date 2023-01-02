'''the DataFrame is divided into chunks using the shape attribute and a list comprehension.
Each chunk is passed as an argument to a separate thread, which multiplies all values in the chunk by 2 and stores the
result in a list. Once all threads have completed, the results are concatenated into a single DataFrame using the
concat function. This allows the row operations to be performed concurrently, improving the performance of the
program.'''

import pandas as pd
import threading
import time as t

# Read the CSV file into a dataframe
df = pd.read_csv("matrix.csv")

start = t.time()
print(start)

# Split the dataframe into chunks
chunks = [df[i:i + 100] for i in range(0, df.shape[0], 100)]


# Define a function to process a chunk
def process_chunk(chunk):
    processed_chunk = chunk * 2
    # Add the processed chunk to the list
    processed_chunks.append(processed_chunk)


# Initialize a list to store the processed chunks
processed_chunks = []

# Process the chunks in parallel using multithreading
threads = []
for chunk in chunks:
    thread = threading.Thread(target=process_chunk, args=(chunk,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Concatenate the processed chunks back into a single dataframe
result_df = pd.concat(processed_chunks)

end = t.time()

print(end - start)

# # Save the resulting dataframe to a CSV file
# result_df.to_csv("updated.csv", index=False)


##########################################################################################


df1 = pd.read_csv("matrix.csv")
start = t.time()
df1 = df1.multiply(2)
end = t.time()
print(end - start)


print(help(pd))