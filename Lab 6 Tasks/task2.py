from collections import deque

goal = 20
start = 1
beam_width = 2

def h(n):
    return abs(goal - n)

def next_states(n):
    return [n + 2, n + 3, n * 2]

beam = [(start, [start])]
level = 0
found = False

print(f"Starting from: {start}")
print(f"Goal: {goal} | Beam Width: {beam_width}\n")

while beam:
    level += 1
    print(f"Level {level}:")

    all_candidates = []
    for current, path in beam:
        children = next_states(current)
        for child in children:
            all_candidates.append((child, path + [child]))

    seen = set()
    unique_candidates = []
    for val, path in all_candidates:
        if val not in seen:
            seen.add(val)
            unique_candidates.append((val, path))

    unique_candidates.sort(key=lambda x: h(x[0]))

    explored = [val for val, _ in unique_candidates]
    print(f"  All generated: {explored}")

    for val, path in unique_candidates:
        if val == goal:
            print(f"  Goal reached!")
            print(f"\nFinal Path: {' -> '.join(map(str, path))}")
            found = True
            break

    if found:
        break

    beam = unique_candidates[:beam_width]
    kept = [val for val, _ in beam]
    print(f"  Keeping best {beam_width}: {kept}\n")
