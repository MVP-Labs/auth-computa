
import json
from dt_asset.document.dt_helper import DTHelper
from dt_asset.document.ddo import DDO
from dt_asset.template.op_template import OpTemplate
from dt_asset.storage.ipfs_provider import IPFSProvider
from dt_asset.agreement.constraint import validate_leaf_template, validate_service_agreement, _check_params

ipfs_client = IPFSProvider()
creator_address = '0x7080b17af4b29F621A5Ef3B1802B2a778Af595d0'

#####
print('generate op template')

metadata = {'main': {'name': 'add_op', 'desc': 'test op', 'type': 'Operation'}}
with open('./tests/template/add_op.py', 'r') as f:
    operation = f.read()
with open('./tests/template/params.json', 'r') as f:
    params = f.read()

op = OpTemplate()
op.add_metadata(metadata)
op.add_template(operation, params)
op.add_creator(creator_address)
op.assign_tid(DTHelper.generate_new_dt())
op.create_proof()

op_cid = ipfs_client.add(op.to_dict())
op_dict = ipfs_client.get(op_cid)

cloned_op = OpTemplate(dictionary=op_dict)
print(cloned_op.tid)
print(cloned_op.creator)
print(cloned_op.metadata)
print(cloned_op.operation)
print(cloned_op.params)

#####
print('\ngenerate leaf ddo1')

metadata = {'main': {'type': 'Dataset', 'name': 'leaf data1'}}
service = {
    'index': 'sid_for_leaf1',
    'endpoint': 'ip:port',
    'descriptor': {
        'template': op.tid,
        'constraint': {
            'arg1': 1,
            'arg2': {}
        }
    },
    'attributes': {
        'price': 10
    }
}

leaf_ddo1 = DDO()
leaf_ddo1.add_metadata(metadata)
leaf_ddo1.add_service(service)
leaf_ddo1.add_creator(creator_address)
leaf_ddo1.assign_dt(DTHelper.generate_new_dt())
leaf_ddo1.create_proof()
print(leaf_ddo1.to_dict())

ddo_cid = ipfs_client.add(leaf_ddo1.to_dict())
ddo_dict = ipfs_client.get(ddo_cid)
cloned_ddo = DDO(dictionary=ddo_dict)

constraint = leaf_ddo1.get_service_by_index(
    'sid_for_leaf1').descriptor['constraint']
print(_check_params(json.loads(op.params), constraint))

#####
print('\ngenerate leaf ddo2')

metadata = {'main': {'type': 'Dataset', 'name': 'leaf data2'}}
service1 = {
    'index': 'sid1_for_leaf2',
    'endpoint': 'ip:port',
    'descriptor': {
        'template': op.tid,
        'constraint': {
            'arg1': {},
            'arg2': 2
        }
    },
    'attributes': {
        'price': 20
    }
}
service2 = {
    'index': 'sid2_for_leaf2',
    'endpoint': 'ip:port',
    'descriptor': {
        'template': op.tid,
        'constraint': {
            'arg1': 1,
            'arg2': 2
        }
    },
    'attributes': {
        'price': 20
    }
}

leaf_ddo2 = DDO()
leaf_ddo2.add_metadata(metadata)
leaf_ddo2.add_service(service1)
leaf_ddo2.add_service(service2)
leaf_ddo2.assign_dt(DTHelper.generate_new_dt())
print(leaf_ddo2.to_dict())

constraint = leaf_ddo2.get_service_by_index(
    'sid1_for_leaf2').descriptor['constraint']
print(_check_params(json.loads(op.params), constraint))
constraint = leaf_ddo2.get_service_by_index(
    'sid2_for_leaf2').descriptor['constraint']
print(_check_params(json.loads(op.params), constraint))

#####
print('\ngenerate composable ddo1')

metadata = {'main': {'type': 'Dataset', 'name': 'aggregated dataset'}}
child_dts = [
    leaf_ddo1.dt,
    leaf_ddo2.dt
]
service = {
    'index': 'sid_for_cdt1',
    'endpoint': 'ip:port',
    'descriptor': {
        'workflow': {
            leaf_ddo1.dt: {
                'service': 'sid_for_leaf1',
                'constraint': {
                    'arg1': 1,
                    'arg2': {}
                }
            },
            leaf_ddo2.dt: {
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

cdt_ddo1 = DDO()
cdt_ddo1.add_metadata(metadata, child_dts)
cdt_ddo1.add_service(service)
cdt_ddo1.assign_dt(DTHelper.generate_new_dt())
print(cdt_ddo1.to_dict())

print(validate_service_agreement(cdt_ddo1, leaf_ddo1))
print(validate_service_agreement(cdt_ddo1, leaf_ddo2))

#####
print('\ngenerate composable ddo2')

metadata = {'main': {'type': 'Algorithm', 'name': 'final algorithm'}}
child_dts = [
    cdt_ddo1.dt,
]
service = {
    'index': 'sid_for_cdt2',
    'endpoint': {},
    'descriptor': {
        'workflow': {
            cdt_ddo1.dt: {
                'service': 'sid_for_cdt1',
                'constraint': {
                    leaf_ddo1.dt: {
                        'arg1': 1,
                        'arg2': 3,
                    },
                    leaf_ddo2.dt: {
                        'arg1': 4,
                        'arg2': 2
                    }
                }
            }
        }
    },
    'attributes': {
        'price': 40
    }
}

cdt_ddo2 = DDO()
cdt_ddo2.add_metadata(metadata, child_dts)
cdt_ddo2.add_service(service)
cdt_ddo2.assign_dt(DTHelper.generate_new_dt())
print(cdt_ddo2.to_dict())

print(validate_service_agreement(cdt_ddo2, cdt_ddo1))
