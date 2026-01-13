# Openrank_Fudan_DataNET
<img width="1199" height="676" alt="image" src="https://github.com/user-attachments/assets/fdd3fe8c-4a7b-42c6-9950-842dc19e69fc" />


## 关联开源项目（赛题）：

**EasyGraph**：https://github.com/easy-graph/Easy-Graph

**主题**：开发者协作网络的图分析与优化



## 1.Installation

#### 1.1 Clone the repository

```bash
git clone https://github.com/Zhang-S-S/OpenRank_Fudan_DataNET.git
```

#### 1.2 Pull pybind11 (for C++/Python bindings)

```bash
cd OpenRank_Fudan_DataNET/复赛/代码/EasyGraph++/cpp_easygraph
git clone --depth 1 https://github.com/pybind/pybind11.git pybind11
```

#### 1.3 Install the EasyGraph++ package

After returning to the 'EasyGraph++' directory, install it:

```bash
cd ..
pip install .
```

#### 1.4 Install EasyGraph++ dependencies

```bash
pip install fastjsonschema
pip install torch==2.4.0 --index-url https://download.pytorch.org/whl/cpu
pip install torch_scatter==2.1.2 torch_sparse==0.6.18 -f https://data.pyg.org/whl/torch-2.4.0+cpu.html
pip install torch_geometric==2.7.0
```

## 2.Usage

This project provides a bench.py script to test all optimized functions of EasyGraph++, and outputs the results to a text file (txt).

#### 2.1 Navigate to the repository directory (ensure that the data files can be located via relative paths).

```bash
cd OpenRank_Fudan_DataNET
```

#### 2.2 Run bench.py

```bash
python 复赛/代码/测试代码/bench.py
```

#### 2.3 Output  
After the execution is completed, a result/ directory will be generated in the current working directory, which contains output files for various metrics (e.g., pagerank_result.txt).

> If prompted that ca-HepPh.txt is not found: check if the running directory is correct, or update file_path in bench.py to your actual path.

## 3. EasyGraph++ implementation location

The file paths for the corresponding EasyGraph++ algorithm implementations are as follows:

- Betweenness：[`OpenRank_Fudan_DataNET/复赛/代码/EasyGraph++/cpp_easygraph/functions/centrality/betweenness.cpp`](https://github.com/Zhang-S-S/OpenRank_Fudan_DataNET/blob/main/%E5%A4%8D%E8%B5%9B/%E4%BB%A3%E7%A0%81/EasyGraph%2B%2B/cpp_easygraph/functions/centrality/betweenness.cpp)
- Closeness：[`OpenRank_Fudan_DataNET/复赛/代码/EasyGraph++/cpp_easygraph/functions/centrality/closeness.cpp`](https://github.com/Zhang-S-S/OpenRank_Fudan_DataNET/blob/main/%E5%A4%8D%E8%B5%9B/%E4%BB%A3%E7%A0%81/EasyGraph%2B%2B/cpp_easygraph/functions/centrality/closeness.cpp)
- PageRank：[`OpenRank_Fudan_DataNET/复赛/代码/EasyGraph++/cpp_easygraph/functions/pagerank/pagerank.cpp`](https://github.com/Zhang-S-S/OpenRank_Fudan_DataNET/blob/main/%E5%A4%8D%E8%B5%9B/%E4%BB%A3%E7%A0%81/EasyGraph%2B%2B/cpp_easygraph/functions/pagerank/pagerank.cpp)
- Katz：[`OpenRank_Fudan_DataNET/复赛/代码/EasyGraph++/cpp_easygraph/functions/centrality/katz_centrality.cpp`](https://github.com/Zhang-S-S/OpenRank_Fudan_DataNET/blob/main/%E5%A4%8D%E8%B5%9B/%E4%BB%A3%E7%A0%81/EasyGraph%2B%2B/cpp_easygraph/functions/centrality/katz_centrality.cpp)
- Eigenvector：[`OpenRank_Fudan_DataNET/复赛/代码/EasyGraph++/cpp_easygraph/functions/centrality/eigenvector.cpp`](https://github.com/Zhang-S-S/OpenRank_Fudan_DataNET/blob/main/%E5%A4%8D%E8%B5%9B/%E4%BB%A3%E7%A0%81/EasyGraph%2B%2B/cpp_easygraph/functions/centrality/eigenvector.cpp)
- Constraint：[`OpenRank_Fudan_DataNET/复赛/代码/EasyGraph++/cpp_easygraph/functions/structural_holes/evaluation.cpp`](https://github.com/Zhang-S-S/OpenRank_Fudan_DataNET/blob/main/%E5%A4%8D%E8%B5%9B/%E4%BB%A3%E7%A0%81/EasyGraph%2B%2B/cpp_easygraph/functions/structural_holes/evaluation.cpp)
