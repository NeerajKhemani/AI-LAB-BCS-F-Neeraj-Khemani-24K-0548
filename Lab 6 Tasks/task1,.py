import random

def f(x):
    return -x**2 + 6*x

current = random.randint(0, 6)
print(f"Starting at x = {current}, f(x) = {f(current)}\n")

step = 0
while True:
    step += 1
    left = current - 1
    right = current + 1

    best_neighbor = current
    best_val = f(current)

    if 0 <= left <= 6 and f(left) > best_val:
        best_neighbor = left
        best_val = f(left)

    if 0 <= right <= 6 and f(right) > best_val:
        best_neighbor = right
        best_val = f(right)

    if best_neighbor == current:
        print(f"No better neighbor found. Stopping here.")
        break

    current = best_neighbor
    print(f"Step {step}: moved to x = {current}, f(x) = {f(current)}")

print(f"\nBest x found: {current}")
print(f"Best f(x) found: {f(current)}")
