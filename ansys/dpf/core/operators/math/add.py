"""
add
===
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class add(Operator):
    """Computes the sum of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field. if one of the input field is empty, the remaining is forwarded to the output.

      available inputs:
        - fieldA (Field, FieldsContainer)
        - fieldB (Field, FieldsContainer)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.add()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.add(fieldA=my_fieldA,fieldB=my_fieldB)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, fieldA=None, fieldB=None, config=None, server=None):
        super().__init__(name="add", config = config, server = server)
        self._inputs = InputsAdd(self)
        self._outputs = OutputsAdd(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)

    @staticmethod
    def _spec():
        spec = Specification(description="""Computes the sum of two fields. If one field's scoping has 'overall' location, then these field's values are applied on the entire other field. if one of the input field is empty, the remaining is forwarded to the output.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "add")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAdd 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsAdd 
        """
        return super().outputs


#internal name: add
#scripting name: add
class InputsAdd(_Inputs):
    """Intermediate class used to connect user inputs to add operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.add()
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
    """
    def __init__(self, op: Operator):
        super().__init__(add._spec().inputs, op)
        self._fieldA = Input(add._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fieldA)
        self._fieldB = Input(add._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._fieldB)

    @property
    def fieldA(self):
        """Allows to connect fieldA input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_fieldA : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.add()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> #or
        >>> op.inputs.fieldA(my_fieldA)

        """
        return self._fieldA

    @property
    def fieldB(self):
        """Allows to connect fieldB input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_fieldB : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.add()
        >>> op.inputs.fieldB.connect(my_fieldB)
        >>> #or
        >>> op.inputs.fieldB(my_fieldB)

        """
        return self._fieldB

class OutputsAdd(_Outputs):
    """Intermediate class used to get outputs from add operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.add()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(add._spec().outputs, op)
        self._field = Output(add._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.add()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field

