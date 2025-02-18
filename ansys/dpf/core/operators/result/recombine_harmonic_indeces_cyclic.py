"""
recombine_harmonic_indeces_cyclic
=================================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "result" category
"""

class recombine_harmonic_indeces_cyclic(Operator):
    """Add the fields corresponding to different load steps with the same frequencies to compute the response.

      available inputs:
        - fields_container (FieldsContainer)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.result.recombine_harmonic_indeces_cyclic()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.result.recombine_harmonic_indeces_cyclic(fields_container=my_fields_container)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, config=None, server=None):
        super().__init__(name="recombine_harmonic_indeces_cyclic", config = config, server = server)
        self._inputs = InputsRecombineHarmonicIndecesCyclic(self)
        self._outputs = OutputsRecombineHarmonicIndecesCyclic(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)

    @staticmethod
    def _spec():
        spec = Specification(description="""Add the fields corresponding to different load steps with the same frequencies to compute the response.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "recombine_harmonic_indeces_cyclic")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRecombineHarmonicIndecesCyclic 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRecombineHarmonicIndecesCyclic 
        """
        return super().outputs


#internal name: recombine_harmonic_indeces_cyclic
#scripting name: recombine_harmonic_indeces_cyclic
class InputsRecombineHarmonicIndecesCyclic(_Inputs):
    """Intermediate class used to connect user inputs to recombine_harmonic_indeces_cyclic operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.recombine_harmonic_indeces_cyclic()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
    """
    def __init__(self, op: Operator):
        super().__init__(recombine_harmonic_indeces_cyclic._spec().inputs, op)
        self._fields_container = Input(recombine_harmonic_indeces_cyclic._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.result.recombine_harmonic_indeces_cyclic()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

class OutputsRecombineHarmonicIndecesCyclic(_Outputs):
    """Intermediate class used to get outputs from recombine_harmonic_indeces_cyclic operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.result.recombine_harmonic_indeces_cyclic()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(recombine_harmonic_indeces_cyclic._spec().outputs, op)
        self._fields_container = Output(recombine_harmonic_indeces_cyclic._spec().output_pin(0), 0, op) 
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

        >>> op = dpf.operators.result.recombine_harmonic_indeces_cyclic()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

