import streamlit as st
st.image("LabReport_BSD2513_#1.jpg", caption="Breadth-First Search Graph", use_column_width=True)

graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['F','G']
}

def bfs(graph, start_node):
    visited = []
    queue = []
    visited.append(start_node)
    queue.append(start_node)
    traversal_order = []

    while queue:
        s = queue.pop(0)
        traversal_order.append(s)

        for neighbour in sorted(graph[s]):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return traversal_order

st.title("Breadth-First Search (BFS) Traversal")
st.write("This app performs BFS on the graph shown above.")

start_node = st.text_input("Enter start node (default = 'A'):", "A")

if st.button("Run BFS"):
    if start_node in graph:
        order = bfs(graph, start_node)
        st.success("Following is the Breadth-First Search traversal order:")
        st.write(" → ".join(order))
    else:
        st.error("Start node not found in graph.")

st.caption("Lab Report 1 BSD2513 | BFS Traversal Demonstration")
