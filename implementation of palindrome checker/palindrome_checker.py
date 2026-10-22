from collections import deque

# Stack implementation (LIFO)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


# Queue implementation (FIFO)
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()


# Function to check palindrome
def is_palindrome(text):
    stack = Stack()
    queue = Queue()

    # Convert to lowercase and remove spaces and symbols
    text = "".join(
        ch.lower() for ch in text if ch.isalnum()
    )

    if not text:
        return None

    # Store each character in both data structures
    for ch in text:
        stack.push(ch)
        queue.enqueue(ch)

    # Compare reverse order with original order
    while stack.items and queue.items:
        if stack.pop() != queue.dequeue():
            return False

    return True


# Main program
def main():
    print("=" * 40)
    print(" PALINDROME CHECKER USING STACK & QUEUE")
    print("=" * 40)

    while True:
        text = input("\nEnter a word, phrase, or number: ")

        result = is_palindrome(text)

        if result is None:
            print("Invalid input! Enter letters or numbers.")
        elif result:
            print(f"'{text}' is a PALINDROME.")
        else:
            print(f"'{text}' is NOT a PALINDROME.")

        choice = input("\nCheck another input? (y/n): ").lower()

        if choice != 'y':
            print("\nProgram terminated successfully.")
            break


if __name__ == "__main__":
    main()
