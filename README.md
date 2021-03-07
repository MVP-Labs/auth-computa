# dt-asset

## 概览

本仓库提供了对链下资产进行服务描述的工具集，包括资产数据通证的生成、资产分布式文档的存储和解析、可信算子和跨域分布式工作流服务的创建、以及层次化的服务约束满足和校验。

## 核心目标

dt-asset这项工作让资产拥有者可以通过可信的链上代码指令来快速定义其链下资产服务，相关元数据存储在可信且可追溯的分布式存储网络中(例如Filecoin)，以充当链下可信计算的图灵机纸带。我们希望尽可能多地提供具有隐私保护能力的链上指令([Compute-to-Data](https://github.com/ownership-labs/Compute-to-Data)提供了一个示例)，从而实现对链下世界的可信隐私计算，确保资产方的敏感信息不会被未定义或隐私泄漏的指令触发运算，最终让(数据)资产可以被一次定义、多次出售。

## 运行流程

```
$ git clone https://github.com/ownership-labs/dt-asset
$ cd dt-asset
$ export PYTHONPATH=$PYTHONPATH:"../dt-asset"
$ pip install -r requirements.txt
$ python tests/test.py
```

## 分布式可信工作流

我们的系统考虑了部分满足关系，除了触发实际计算的顶层算法CDT外，任一下层组合CDT或叶子DT都无需满足所有的约束条款。通过这样的设计，我们希望在未来有交易对手方根据历史信息来自动寻找最优参数，从而实现自主经济代理。

### 可信算子及参数约束：

add operator:
```
import json
import argparse

if __name__ == '__main__':
    print('hello world, data token')

    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, required=True)

    args = parser.parse_args()
    op_args = json.load(open(args.config))

    print(op_args['arg1'] + op_args['arg2'])
```

params.json:
```
{
    "arg1": {},
    "arg2": {}
}
```
可信算子都发布在公开区块链上，以形成链下资产的计算规范。在之后的工作中，我们将考虑tensor级别的算子。

### Leaf DDO的示意

叶子资产可通过可信算子模版来定义其资产服务：
```
metadata = {'main': {'type': 'Dataset', 'name': 'leaf data1'}}
service = {
    'index': 'sid_for_leaf1',
    'endpoint': 'ip:port',
    'descriptor': {
        'template': 'dt:ownership:xxx...' # tid for add-op,
        'constraint': {
            'arg1': 1,
            'arg2': {}
        }
    },
    'attributes': {
        'price': 10
    }
}
```

### Composable DDO的示意

组合资产可通过分布式工作流来定义，逐步满足子资产的约束条件：
```
metadata = {'main': {'type': 'Dataset', 'name': 'aggregated dataset'}}
child_dts = [
    'dt:ownership:xxx...dt1',  # for leaf_ddo1.dt
    'dt:ownership:xxx...dt2'   # for leaf_ddo2.dt
]
service = {
    'index': 'sid_for_cdt1',
    'endpoint': 'ip:port',
    'descriptor': {
        'workflow': {
            'dt:ownership:xxx...dt1': {
                'service': 'sid_for_leaf1',
                'constraint': {
                    'arg1': 1,
                    'arg2': {}
                }
            },
            'dt:ownership:xxx...dt2': {
                'service': 'sid1_for_leaf2',
                'constraint': {
                    'arg1': {},
                    'arg2': 2
                }
            }
        }
    },
    'attributes': {
        'price': 30
    }
}
```
