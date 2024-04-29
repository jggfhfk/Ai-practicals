import heapq

def a_star(n):
    def is_valid(state, nextX):
        nextY = len(state)
        for i in range(nextY):
            if state[i] == nextX or \
                state[i] - i == nextX - nextY or \
                state[i] + i == nextX + nextY:
                return False
        return True

    def priority(state):
        return len(state) - sum(abs(c - i) for i, c in enumerate(state))

    pq = []
    heapq.heappush(pq, (0, []))
    while True:
        (pri, state) = heapq.heappop(pq)
        if len(state) == n:
            return state
        for pos in range(n):
            if is_valid(state, pos):
                heapq.heappush(pq, (priority(state), state + [pos]))

def print_board(result):
    for pos in result:
        line = ""
        for i in range(len(result)):
            if i == pos:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

n = 4
result = a_star(n)
print_board(result)
