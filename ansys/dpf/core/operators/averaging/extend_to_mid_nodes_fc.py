"""
extend_to_mid_nodes_fc
======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "averaging" category
"""

class extend_to_mid_nodes_fc(Operator):
    """Extends ElementalNodal fields defined on corner nodes to ElementalNodal fields defined also on the mid nodes.

      available inputs:
        - fields_container (FieldsContainer)
        - mesh (MeshedRegion) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.extend_to_mid_nodes_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.extend_to_mid_nodes_fc(fields_container=my_fields_container,mesh=my_mesh)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, config=None, server=None):
        super().__init__(name="extend_to_mid_nodes_fc", config = config, server = server)
        self._inputs = InputsExtendToMidNodesFc(self)
        self._outputs = OutputsExtendToMidNodesFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Extends ElementalNodal fields defined on corner nodes to ElementalNodal fields defined also on the mid nodes.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "extend_to_mid_nodes_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsExtendToMidNodesFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsExtendToMidNodesFc 
        """
        return super().outputs


#internal name: extend_to_mid_nodes_fc
#scripting name: extend_to_mid_nodes_fc
class InputsExtendToMidNodesFc(_Inputs):
    """Intermediate class used to connect user inputs to extend_to_mid_nodes_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.extend_to_mid_nodes_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(extend_to_mid_nodes_fc._spec().inputs, op)
        self._fields_container = Input(extend_to_mid_nodes_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._mesh = Input(extend_to_mid_nodes_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.extend_to_mid_nodes_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: the mesh region in this pin is used to perform the averaging, if there is no field's support it is used

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.extend_to_mid_nodes_fc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsExtendToMidNodesFc(_Outputs):
    """Intermediate class used to get outputs from extend_to_mid_nodes_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.extend_to_mid_nodes_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(extend_to_mid_nodes_fc._spec().outputs, op)
        self._fields_container = Output(extend_to_mid_nodes_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.extend_to_mid_nodes_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

