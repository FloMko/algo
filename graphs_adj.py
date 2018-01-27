def main():
    graph = dict()
    graph['A'] = ['B','C']
    graph['B'] = ['E','A']
    graph['C'] = ['A','B','E','F']
    graph['E'] = ['B','C']
    graph['F'] = ['C']
    matrix_elements = sorted(graph.keys())
    edges_list = []
    for key in matrix_elements:
        for neighbor in graph[key]:
            edges_list.append((key,neighbor))
    cols = rows = len(matrix_elements)
    adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
    for edge in edges_list:
        index_of_first_vertex = matrix_elements.index(edge[0])
        index_of_second_vertex = matrix_elements.index(edge[1])
        adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1
    print(adjacency_matrix)

if __name__ == '__main__':
    main()

