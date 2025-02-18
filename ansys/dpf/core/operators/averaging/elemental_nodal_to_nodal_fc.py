"""
elemental_nodal_to_nodal_fc
===========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "averaging" category
"""

class elemental_nodal_to_nodal_fc(Operator):
    """Transform ElementalNodal fields into Nodal fields using an averaging process, result is computed on a given node scoping. If the input fields are mixed shell/solid, then the fields are splitted by element shape and the output fields container has elshape label.

      available inputs:
        - fields_container (FieldsContainer)
        - mesh (MeshedRegion, MeshesContainer) (optional)
        - should_average (bool) (optional)
        - scoping (Scoping, ScopingsContainer) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_should_average = bool()
      >>> op.inputs.should_average.connect(my_should_average)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_fc(fields_container=my_fields_container,mesh=my_mesh,should_average=my_should_average,scoping=my_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, should_average=None, scoping=None, config=None, server=None):
        super().__init__(name="elemental_nodal_To_nodal_fc", config = config, server = server)
        self._inputs = InputsElementalNodalToNodalFc(self)
        self._outputs = OutputsElementalNodalToNodalFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if should_average !=None:
            self.inputs.should_average.connect(should_average)
        if scoping !=None:
            self.inputs.scoping.connect(scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal fields into Nodal fields using an averaging process, result is computed on a given node scoping. If the input fields are mixed shell/solid, then the fields are splitted by element shape and the output fields container has elshape label.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""the mesh region in this pin is used to perform the averaging, if there is no field's support it is used"""), 
                                 2 : PinSpecification(name = "should_average", type_names=["bool"], optional=True, document="""each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities)"""), 
                                 3 : PinSpecification(name = "scoping", type_names=["scoping","scopings_container"], optional=True, document="""average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "elemental_nodal_To_nodal_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsElementalNodalToNodalFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsElementalNodalToNodalFc 
        """
        return super().outputs


#internal name: elemental_nodal_To_nodal_fc
#scripting name: elemental_nodal_to_nodal_fc
class InputsElementalNodalToNodalFc(_Inputs):
    """Intermediate class used to connect user inputs to elemental_nodal_to_nodal_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_should_average = bool()
      >>> op.inputs.should_average.connect(my_should_average)
      >>> my_scoping = dpf.Scoping()
      >>> op.inputs.scoping.connect(my_scoping)
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal_fc._spec().inputs, op)
        self._fields_container = Input(elemental_nodal_to_nodal_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._mesh = Input(elemental_nodal_to_nodal_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh)
        self._should_average = Input(elemental_nodal_to_nodal_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._should_average)
        self._scoping = Input(elemental_nodal_to_nodal_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._scoping)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
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
        my_mesh : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def should_average(self):
        """Allows to connect should_average input to the operator

        - pindoc: each nodal value is divided by the number of elements linked to this node (default is true for discrete quantities)

        Parameters
        ----------
        my_should_average : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
        >>> op.inputs.should_average.connect(my_should_average)
        >>> #or
        >>> op.inputs.should_average(my_should_average)

        """
        return self._should_average

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator

        - pindoc: average only on these nodes, if it is scoping container, the label must correspond to the one of the fields container

        Parameters
        ----------
        my_scoping : Scoping, ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> #or
        >>> op.inputs.scoping(my_scoping)

        """
        return self._scoping

class OutputsElementalNodalToNodalFc(_Outputs):
    """Intermediate class used to get outputs from elemental_nodal_to_nodal_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_nodal_to_nodal_fc._spec().outputs, op)
        self._fields_container = Output(elemental_nodal_to_nodal_fc._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.averaging.elemental_nodal_to_nodal_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

