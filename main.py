from flask import Flask, render_template, request, jsonify
import heapq

app = Flask(__name__)

# Алгоритм Dijkstra для поиска кратчайших путей
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dijkstra', methods=['POST'])
def run_dijkstra():
    graph = request.json.get('graph', {})
    start_vertex = request.json.get('start', '')

    # Проверка наличия начальной вершины
    if start_vertex not in graph:
        return jsonify({'error': 'Стартовая нода не в графе'}), 400

    shortest_paths = dijkstra(graph, start_vertex)

    return jsonify(shortest_paths)

if __name__ == '__main__':
    app.run(debug=True)


    
