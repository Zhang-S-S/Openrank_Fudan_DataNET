# Openrank_Fudan_DataNET
<img width="1199" height="676" alt="image" src="https://github.com/user-attachments/assets/fdd3fe8c-4a7b-42c6-9950-842dc19e69fc" />


## 关联开源项目（赛题）：

**EasyGraph**：https://github.com/easy-graph/Easy-Graph

**主题**：开发者协作网络的图分析与优化


## 安装步骤（Installation）

#### 1.1 克隆仓库

```bash
git clone https://github.com/Zhang-S-S/OpenRank_Fudan_DataNET.git
```

#### 1.2 拉取 pybind11（用于 C++/Python 绑定）

```bash
cd OpenRank_Fudan_DataNET/复赛/代码/EasyGraph++/cpp_easygraph
git clone --depth 1 https://github.com/pybind/pybind11.git pybind11
```

#### 1.3 安装本地 EasyGraph++ 包

回到 `EasyGraph++` 目录后安装：

```bash
cd ..
pip install .
```

#### 1.4 EasyGraph 依赖安装

```bash
pip install fastjsonschema
pip install torch==2.4.0 --index-url https://download.pytorch.org/whl/cpu
pip install torch_scatter==2.1.2 torch_sparse==0.6.18 -f https://data.pyg.org/whl/torch-2.4.0+cpu.html
pip install torch_geometric==2.7.0
```
