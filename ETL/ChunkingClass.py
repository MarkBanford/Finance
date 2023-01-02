import pandas as pd
import threading


class DataFrameProcessor:
    def __init__(self, df, chunk_size=1000):
        self.df = df
        self.chunk_size = chunk_size

    def process(self):
        # Divide the DataFrame into chunks
        chunks = [self.df[i:i + self.chunk_size] for i in range(0, self.df.shape[0], self.chunk_size)]

        # Create a list to store the results
        results = []

        # Create a thread for each chunk
        threads = []
        for chunk in chunks:
            thread = threading.Thread(target=self.process_chunk, args=(chunk,))
            thread.start()
            threads.append(thread)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Concatenate the results into a single DataFrame
        self.df = pd.concat(results)

    def process_chunk(self, chunk):
        # Multiply all values in the chunk by 2
        chunk *= 2
        return chunk


# Load the DataFrame
df = pd.read_csv('matrix.csv')

df[0, 0] = 100

print(df)

# Create an instance of the DataFrameProcessor class
processor = DataFrameProcessor(df)

# Process the DataFrame
processor.process()

# The processed DataFrame is now stored in the 'df' attribute of the processor instance
df = processor.df
print(df)
