import pandas as pd
import easygraph as eg
import os
import time
import numpy as np

def setup():
    """ca-HepPh (无向)"""
    file_path = '复赛/代码/测试代码/ca-HepPh.txt'
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")

    print(f"[Setup] Loading {file_path}...")
    df = pd.read_csv(
        file_path,
        sep=r'\s+',
        header=None,
        names=["source", "target"],
        comment='#',
        dtype=int,
    )

    # 排序以保证ID映射确定性
    all_nodes_list = sorted(list(set(df["source"].tolist() + df["target"].tolist())))
    node_to_idx = {node: idx for idx, node in enumerate(all_nodes_list)}

    mapped_sources = df["source"].map(node_to_idx).to_numpy()
    mapped_targets = df["target"].map(node_to_idx).to_numpy()
    edges_array = np.vstack([mapped_sources, mapped_targets]).T

    G = eg.GraphC()
    G.add_nodes_from(range(len(all_nodes_list)))
    G.add_edges_from(edges_array)

    print(f"Graph setup complete. {G.number_of_nodes()} nodes, {G.number_of_edges()} edges.")
    
    # 返回 G 和 ID映射列表
    return G, all_nodes_list


def save_txt(name, result, idx_to_node):
    # 创建结果目录
    output_dir = "result"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    path = os.path.join(output_dir, f"{name}_result.txt")
    lines = []

    # 兼容 ndarray 和 dict 输出形式
    if isinstance(result, (np.ndarray, list)):
        iterator = enumerate(result)
    elif isinstance(result, dict):
        iterator = result.items()
    else:
        print(f"Error: Unknown result type {type(result)}")
        return

    for internal_id, val in iterator:
        original_id = idx_to_node[internal_id]
        lines.append(f"{original_id}\t{val}\n")
    
    lines.sort()

    with open(path, 'w') as f:
        f.writelines(lines)
        
    print(f"Results saved to {path}")


def main():

    st = time.time()
    G, idx_to_node = setup()
    print(f"Setup time: {time.time() - st:.4f}s\n")

    # 1. Betweenness
    print("Running Betweenness...")
    st = time.time()
    res = eg.betweenness_centrality(G)
    print(f"Betweenness time: {time.time() - st:.4f}s")
    save_txt("betweenness", res, idx_to_node)
    print("-" * 20)

    # 2. Closeness
    print("Running Closeness...")
    st = time.time()
    res = eg.closeness_centrality(G)
    print(f"Closeness time: {time.time() - st:.4f}s")
    save_txt("closeness", res, idx_to_node)
    print("-" * 20)

    # 3. PageRank
    print("Running PageRank...")
    st = time.time()
    res = eg.pagerank(G)
    print(f"PageRank time: {time.time() - st:.4f}s")
    save_txt("pagerank", res, idx_to_node)
    print("-" * 20)

    # 4. Katz
    print("Running Katz...")
    st = time.time()
    res = eg.katz_centrality(G)
    print(f"Katz time: {time.time() - st:.4f}s")
    save_txt("katz", res, idx_to_node)
    print("-" * 20)

    # 5. Eigenvector
    print("Running Eigenvector...")
    st = time.time()
    res = eg.eigenvector_centrality(G)
    print(f"Eigenvector time: {time.time() - st:.4f}s")
    save_txt("eigenvector", res, idx_to_node)
    print("-" * 20)

    # 6. Constraint
    print("Running Constraint...")
    st = time.time()
    res = eg.constraint(G)
    print(f"Constraint time: {time.time() - st:.4f}s")
    save_txt("constraint", res, idx_to_node)
    print("-" * 20)

    print("All tasks finished.")

if __name__ == "__main__":
    main()