import os
import psutil

def check_memory():
    process = psutil.Process(os.getpid())
    print(f"Current Memory Usage: {process.memory_info().rss / 1024**2:.2f} MB")

if __name__ == "__main__":
    check_memory()
