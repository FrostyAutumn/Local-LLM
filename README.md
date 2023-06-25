# Local-LLM

## 第一步：环境的搭建

1. 在开始你的本地大语言模型之旅前，请确保你的计算机上已正确安装较新版本的 CUDA 和 cuDNN 工具，否则无法保证程序能够正常运行。
2. 选择你需要部署的模型，例如，chinese-alpaca-plus 模型。
3. 在下表中检查推荐使用的 Python 编译器版本，例如，chinese-alpaca-plus 模型推荐使用 3.10 版本的 Python 编译器。使用其他版本的编译器无法保证程序能够正常运行。

<table>
    <tr>
        <td>模型类别</td> 
        <td>Python 编译器版本</td>
    </tr>
    <tr>
        <td rowspan="2">
            <a href="https://github.com/ymcui/Chinese-LLaMA-Alpaca">chinese-alpaca-plus</a>
        </td>
        <td rowspan="2">3.10</td>
    </tr>
</table>

4. 检查选择的模型目录下的 requirements.txt 文件，例如，chinese-alpaca-plus/requirements.txt 文件。通过 pip 等工具安装指定的依赖。使用其他版本的依赖无法保证程序能够正常运行。

## 第二步：获取适配的模型权重文件

1. 由于版权原因，本项目不会直接提供一部分模型的权重文件。下表给出了对各模型验证过的能够直接使用的权重文件和对应的SHA256值。

<table>
    <tr>
        <td>模型类别</td> 
        <td>适用的权重类型</td> 
        <td>获取方式</td> 
        <td>文件名</td> 
        <td>SHA256值</td> 
    </tr>
    <tr>
        <td rowspan="2">
            <a href="https://github.com/ymcui/Chinese-LLaMA-Alpaca">chinese-alpaca-plus</a>
        </td>
        <td rowspan="2">7B</td> 
        <td rowspan="2">
            <a href="https://github.com/ymcui/Chinese-LLaMA-Alpaca/wiki/%E5%9C%A8%E7%BA%BF%E6%A8%A1%E5%9E%8B%E5%90%88%E5%B9%B6%E4%B8%8E%E8%BD%AC%E6%8D%A2">合并权重</a>
            及
            <a href="https://github.com/ymcui/Chinese-LLaMA-Alpaca/wiki/%E6%89%8B%E5%8A%A8%E6%A8%A1%E5%9E%8B%E5%90%88%E5%B9%B6%E4%B8%8E%E8%BD%AC%E6%8D%A2">格式转换</a>
        </td>
        <td>pytorch_model-00001-of-00002.bin</td> 
        <td>75ddade0a97a9592daff2fe764d03000cf7561a7798c1fc054e6f3789fded45a</td> 
    </tr>
    <tr>
        <td>pytorch_model-00001-of-00002.bin</td> 
        <td>d1e32eade4c61c029f24e921380812fb698d8faf651944dc11b1ef61efdeffff</td> 
    </tr>
</table>

2. 将模型权重文件放在选择的模型的 /model 目录下（一个典型的HF格式模型权重应当包含.bin, .json和.model文件）。

## 第三步：运行程序

1. 运行选择的模型目录下的 run_* 程序，例如，chinese-alpaca-plus/run_with_cmd.py 程序。
