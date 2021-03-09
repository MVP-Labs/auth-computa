# dt-asset

[中文版](./README_CN.md)

This project implements a new service schema for defining off-chain assets, including: 1) datatoken helper; 2) asset ddo generator; 3) templated operator; 4) service descriptor; 5) cross-domain workflow; 6) agreement and fulfillment; 7) decentralized storage provider.

## Highlights

Our goal is to allow data owners to quickly define data services with trusted on-chain operators (e.g., download, mpc_add, encrypt). The associated metadata is stored in the decentralized storage networks (e.g., Filecoin), which is trusted and immutable. The outputs of each data service can be chained hierarchically, formalizing all related operators as a traceable workflow. When these components are combined, off-chain trusted computation becomes a reality. You can consider the decentralized storage as the tape of Turing machine and the on-chain operators as the instruction set.

We are building more on-chain operators with privacy-preserving capabilities ([Compute-to-Data](https://github.com/ownership-labs/Compute-to-Data) provides an example). Then it becomes trusted private computation. When you define services of sensitive data assets, you don't need to worry about the privacy leakage. This is because the computation will never be triggered by undefined or privacy-leaking operators. Ultimatelly, the data assets can be defined once but sold mutiple times.

## Play With It

```
$ git clone https://github.com/ownership-labs/dt-asset
$ cd dt-asset
$ export PYTHONPATH=$PYTHONPATH:"../dt-asset"
$ pip install -r requirements.txt
$ python tests/test.py
```

## Trusted Workflow

Our system enables hierarchical composable assets, with cross-domain distributed workflows built-in. The high-level asset is required to fulfill service terms and constraints of the lower ones, such as selected operators and parameters. Partial constraint satisfaction is also permitted, which means any middle-level CDT/DDO or leaf DT/DDO do not need to satisfy all constraints. Only the top-level algorithm CDT/DDO should fulfill all requirements, since it triggers the actual computation. With such a design, we hope to attract more traders/scientists to find the optimal parameters based on the historical information of data marketplaces, thus enabling Autonomous Economic Agents (AEAs).

### trusted operator and constraint：

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
Trusted operators are published on the blockchain, and then can be used to define services of data assets. In the later work, we will consider tensor-level operators.

### example of leaf DDO

A leaf asset can be defined by incorporating the template id of operators.
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

### example of composable DDO

Leaf data assets can be aggregated as a data union. You need to use the workflow structure and satisfy the constraints of leaf assets.
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
