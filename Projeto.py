#Construct the De Bruijn Graph of a Collection of k-mers solved by 1117


def de_bruijn(kmers):
    from collections import defaultdict
    
    adj_list = defaultdict(list)
    
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        adj_list[prefix].append(suffix)
    
    # Converte o defaultdict para um dicionário padrão para o retorno
    return {node: adj_list[node] for node in adj_list}

def read_kmers_from_file(file_path):
    with open(file_path, 'r') as file:
        kmers = [line.strip() for line in file if line.strip()]
    return kmers

def write_de_bruijn_to_file(graph, output_file):
    with open(output_file, 'w') as file:
        for node in sorted(graph):
            file.write(f"{node} -> {','.join(graph[node])}\n")

# Nome do arquivo de entrada
input_file = 'rosalind_ba3e.txt'
# Nome do arquivo de saída
output_file = 'de_bruijn_output.txt'

# Ler k-mers do arquivo
kmers = read_kmers_from_file(input_file)

# Construir o gráfico de De Bruijn
de_bruijn_graph = de_bruijn(kmers)

# Escrever o gráfico de De Bruijn no arquivo de saída
write_de_bruijn_to_file(de_bruijn_graph, output_file)

print(f"O gráfico de De Bruijn foi escrito em {output_file}")
