from lcg.api.controllers import validate_params
from lcg.generators import ConfigGenerator
from lcg.schemas import IOSNodeSchema, NetplanSchema
from lcg.api.controllers import ControllerResult
from lcg.maps import MAP_TEMPLATE_TYPES


def _process(template_type, params) -> ConfigGenerator:
    _schema = MAP_TEMPLATE_TYPES.get(template_type).get('schema')

    res = validate_params(_schema, params)
    if res.status != 200:
        return res

    cg = ConfigGenerator()

    cg.generate(params)

    return cg


def controller_ios_base_config(params):
    cg = _process("ios_base_node", params)

    return ControllerResult(data=cg.results, result=True, msg=f"Success", status=200)


def controller_linux_netplan_base(params):
    cg = _process("linux_netplan_base", params)

    return ControllerResult(data=cg.results, result=True, msg=f"Success", status=200)


def controller_cumulux_vx_base_config(params):
    pass
