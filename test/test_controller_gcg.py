import json

from gcg.api.controllers.controller_gcg import controller_gcg_v2, ControllerResult


def test_controller_gcg_v2_1():
    with open('data/r1.json', 'r') as json_file:
        data = json.load(json_file)
        result = controller_gcg_v2(data=data, template_type='ios_base_node')
        assert isinstance(result, ControllerResult)
