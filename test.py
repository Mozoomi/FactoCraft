import signal
import threading
import time

def cleanup():
    print("Cleaning up...")

def main():
    print("Main function running")
    while True:
        time.sleep(1)  # Simulate some ongoing work
        print("Working...")

def signal_handler(sig, frame):
    print('Exiting...')
    cleanup()
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, signal_handler)
    thread = threading.Thread(target=main)
    thread.start()
