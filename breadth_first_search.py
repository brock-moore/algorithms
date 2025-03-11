from collections import deque

def bfs(graph, start, check):
    search_queue = deque()
    search_queue += graph[start]
    searched = set()

    while search_queue:
        token = search_queue.popleft()
        if token not in searched:
            if check(token):
                print(token)
                return True
            else:
                search_queue += graph[token]
                searched.add(token)

    return False

graph = {}
graph["a"] = ["ab", "ac"]
graph["ab"] = ["abc", "abd", "abe", "abf"]
graph["ac"] = ["abc", "abcd"]
graph["abc"] = ["abg"]
graph["abd"] = ["abde"]
graph["abe"] = []
graph["abf"] = []
graph["abg"] = []
graph["abcde"] = []
graph["abcd"] = ["abcde"]

def is_four(token):
    return len(token) == 4

bfs(graph, "a", is_four)