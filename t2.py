V = int(input("Enter the number of vertices: "))

graph = []

print("Enter Adjacency Matrix:")

for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

m = int(input("Enter the number of colors: "))


def is_safe(graph, color, vertex, c):

    for i in range(V):

        if graph[vertex][i] == 1 and color[i] == c:
            return False

    return True


def graph_coloring_util(graph, m, color, vertex):

    if vertex == V:
        return True

    for c in range(1, m + 1):

        # Correct parameter order
        if is_safe(graph, color, vertex, c):

            color[vertex] = c

            if graph_coloring_util(graph, m, color, vertex + 1):
                return True

            color[vertex] = 0

    return False


def graph_coloring(graph, m):

    color = [0] * V

    if not graph_coloring_util(graph, m, color, 0):
        print("No Solution Exists")
        return

    print("Solution Exists:\n")

    for i in range(V):
        print("Vertex", i, "----->", color[i])


graph_coloring(graph, m)



# N queens

# n = int(input("Enter the number of queens: "))

# board = [[0] * n for _ in range(n)]


# def isSafe(row, col):

#     # Check same column
#     for i in range(row):
#         if board[i][col] == 1:
#             return False

#     # Check left diagonal
#     i, j = row - 1, col - 1

#     while i >= 0 and j >= 0:
#         if board[i][j] == 1:
#             return False

#         i -= 1
#         j -= 1

#     # Check right diagonal
#     i, j = row - 1, col + 1

#     while i >= 0 and j < n:
#         if board[i][j] == 1:
#             return False

#         i -= 1
#         j += 1

#     return True


# def solve(row):

#     if row == n:
#         print("Solution Exists:\n")

#         for i in board:
#             print(i)

#         return True

#     for col in range(n):

#         if isSafe(row, col):

#             board[row][col] = 1

#             if solve(row + 1):
#                 return True

#             board[row][col] = 0

#     return False


# if not solve(0):
#     print("No Solution Exists")







# n = int(input("Enter the number of nodes: "))

# graph = {}

# for i in range(n):

#     node = input(f"Enter the node {i+1}: ").strip()

#     neighbors = input(
#         f"Enter the neighbors of {node} (space separated): "
#     ).split()

#     graph[node] = neighbors

# start_node = input("Enter the start node: ").strip()
# goal_node = input("Enter the goal node: ").strip()

# def bfs(graph, start_node, goal_node):

    # visited = []
    # queue = []

    # visited.append(start_node)
    # queue.append(start_node)

    # print("BFS TRAVERSAL:")

    # while queue:

    #     m = queue.pop(0)

    #     print(m, end=" ")

    #     if m == goal_node:
    #         print("\nGOAL NODE FOUND")
    #         return

    #     for n in graph.get(m, []):

#             if n not in visited:
#                 visited.append(n)
#                 queue.append(n)

# bfs(graph, start_node, goal_node)










# arr = [64, 25, 12, 22, 11]

# n = len(arr)

# for i in range(n):

#     # Assume current index has minimum value
#     min_index = i

#     # Find smaller element in remaining array
#     for j in range(i + 1, n):

#         if arr[j] < arr[min_index]:
#             min_index = j

    # Swap
#     arr[i], arr[min_index] = arr[min_index], arr[i]

# print("Sorted array:", arr)





# import heapq

# def dijkstra(graph, start):
#     dist = {node: float('inf') for node in graph}
#     dist[start] = 0

#     pq = [(0, start)]

#     while pq:
#         current_dist, node = heapq.heappop(pq)

#         for neighbor, weight in graph[node]:
#             distance = current_dist + weight

#             if distance < dist[neighbor]:
#                 dist[neighbor] = distance
#                 heapq.heappush(pq, (distance, neighbor))

#     return dist


# n = int(input("Enter the number of nodes: "))
# graph = {}

# for i in range(n):
#     node = input(f"Enter node {i+1}: ")
#     edges = int(input(f"Enter number of neighbors for {node}: "))

#     neighbors = []

#     for j in range(edges):
#         neighbor = input("Enter neighbor node: ")
#         weight = int(input("Enter weight: "))

#         neighbors.append((neighbor, weight))

#     graph[node] = neighbors


# start_node = input("Enter the start node: ")

# result = dijkstra(graph, start_node)

# print("\nShortest distance from", start_node)

# for node in result:
#     print(node, ":", result[node])



# def triage_system():
# print("=== Hospital Expert System: Patient Triage Assistant ===")

# name = input("Enter Patient Name: ")
# age = int(input("Enter Age: "))
# print("\nSelect Symptoms (Y/N):")

# chest_pain = input("Chest Pain? ").lower() == 'y'
# short_breath = input("Shortness of Breath? ").lower() == 'y'
# bleeding = input("Heavy Bleeding? ").lower() == 'y'
# high_fever = input("High Fever? ").lower() == 'y'
# injury = input("Recent Injury? ").lower() == 'y'
# dizziness = input("Dizziness or Fainting? ").lower() == 'y'
# stomach_pain = input("Severe Stomach Pain? ").lower() == 'y'

# print("\nAnalyzing symptoms...")

# if bleeding or injury:
# department = "Emergency Room (ER)"
# advice = "Immediate attention required. Proceed to the ER."
# elif chest_pain or short_breath:
# department = "Cardiology"
# advice = "Cardiac symptoms detected. Visit Cardiology immediately."
# elif high_fever and age < 12:

# department = "Pediatrics"
# advice = "High fever in child. Visit Pediatrics urgently."
# elif high_fever:
# department = "General Medicine"
# advice = "Consult a general physician for evaluation."
# elif dizziness:
# department = "Neurology"
# advice = "Neurological symptoms present. Visit Neurology."
# elif stomach_pain:
# department = "Gastroenterology"
# advice = "Visit a gastroenterologist for further diagnosis."
# else:
# department = "Outpatient (OPD)"
# advice = "No critical symptoms. You may proceed to OPD."

# print(f"\n=== Patient Report ===")
# print(f"Name: {name}")
# print(f"Recommended Department: {department}")
# print(f"Advice: {advice}")

# if __name__ == "__main__":
# triage_system()




# def chatbot():
# print("TravelBot: Hello! I am your Travel Agent Assistant ")
# print("Type 'bye' to exit.\n")
# while True:
# user = input("You: ").lower()
# if user in ["hello", "hi", "hey"]:
# print("TravelBot: Hello! Ask me any travel-related question.")
# elif "best time goa" in user or "when visit goa" in user:
# print("TravelBot: Best time to visit Goa is from November to February.")
# elif "best time manali" in user or "when visit manali" in user:
# print("TravelBot: October to February is best for snow, March to June for sightseeing.")
# elif "best time kashmir" in user:
# print("TravelBot: April to October for greenery, December to February for snow.")
# elif "documents" in user:
# print("TravelBot: You need ID proof for domestic travel and passport + visa for international
# travel.")
# elif "cheap flights" in user or "low cost flights" in user:
# print("TravelBot: Book early, avoid weekends, and compare prices to get cheap flights.")
# elif "popular destinations" in user:
# print("TravelBot: Popular destinations include Goa, Manali, Kashmir, Jaipur, and Kerala.")
# elif "luggage" in user or "baggage" in user:
# print("TravelBot: Most airlines allow 15-25 kg check-in and 7 kg cabin baggage.")
# elif "insurance" in user:
# print("TravelBot: Travel insurance covers medical emergencies, cancellations, and lost
# baggage.")
# elif "budget trip" in user:
# print("TravelBot: Plan early, travel off-season, and use public transport to save money.")
# elif "hotel booking" in user or "book hotel" in user:
# print("TravelBot: You can book hotels based on budget, location, and ratings.")

# elif "cancel ticket" in user:
# print("TravelBot: Cancellation depends on airline or hotel policy. Charges may apply.")
# elif "time" in user:
# import datetime
# print("TravelBot: Current time is", datetime.datetime.now().strftime("%H:%M:%S"))
# elif "date" in user:
# import datetime
# print("TravelBot: Today's date is", datetime.datetime.now().date())
# elif user == "bye":
# print("TravelBot: Goodbye! Have a nice journey ")
# break
# else:
# print("TravelBot: Sorry, I don't understand. Please ask travel-related questions.")

# chatbot()



# import heapq
# def prim(graph, start):
# visited = set()
# min_heap = [(0, start)]
# total_cost = 0
# while min_heap:
# weight, node = heapq.heappop(min_heap)
# if node not in visited:
# visited.add(node)
# total_cost += weight
# print(&quot;Visited:&quot;, node, &quot;Weight:&quot;, weight)
# for neighbor, w in graph[node]:
# if neighbor not in visited:
# heapq.heappush(min_heap, (w, neighbor))
# print(&quot;Total Cost of MST:&quot;, total_cost)
# graph = {
# 'A':[('B',2),('C',1)],
# &#39;B&#39;: [(&#39;A&#39;, 2), (&#39;D&#39;, 4), (&#39;E&#39;, 2)],
# &#39;C&#39;: [(&#39;A&#39;, 1), (&#39;F&#39;, 2)],
# &#39;D&#39;: [(&#39;B&#39;, 4)],
# &#39;E&#39;: [(&#39;B&#39;, 2), (&#39;F&#39;, 3)],
# &#39;F&#39;: [(&#39;C&#39;, 2), (&#39;E&#39;, 3)]
# }
# prim(graph, 'A')





