import time
import requests

def measure_latency(url="https://google.com"):
    start = time.perf_counter()
    try:
        requests.get(url, timeout=5)
        end = time.perf_counter()
        print(f"Latency to {url}: {(end - start) * 1000:.2f} ms")
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    measure_latency()
