from abaqusConstants import *
from .ConnectorBehaviorOption import ConnectorBehaviorOption
from .ConnectorOptions import ConnectorOptions

from __init__ import *
from __future__ import annotations


class ConnectorDamping(ConnectorBehaviorOption):
    """The ConnectorDamping object defines damping behavior for one or more components of a
    connector's relative motion. 
    The ConnectorDamping object is derived from the ConnectorBehaviorOption object. 

    Attributes
    ----------
    options: ConnectorOptions
        A :py:class:`~abaqus.Connector.ConnectorOptions.ConnectorOptions` object specifying the :py:class:`~abaqus.Connector.ConnectorOptions.ConnectorOptions` used to define tabular options
        for this ConnectorBehaviorOption.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        mdb.models[name].sections[name].behaviorOptions[i]
        import odbSection
        session.odbs[name].sections[name].behaviorOptions[i]

        The table data for this object are:
        If *behavior*=LINEAR and *coupling*=UNCOUPLED, then each sequence of the table data specifies the following:
            - Damping coefficient (force or moment per relative velocity).
            - Frequency (cycles/time), if the data depend on frequency.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        If *behavior*=NONLINEAR and *coupling*=UNCOUPLED, then each sequence of the table data specifies the following:
            - Force or moment.
            - Relative displacement or rotation.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        If *behavior*=LINEAR and *coupling*=COUPLED, the table data specify the symmetric portion of the damping matrix
        for the specified components followed by any temperature data and then any field data. For example, if
        components 2, 3, and 5 are specified, the table portion of the command is as follows:
        table=( (C22C22, C23C23, C25C25, C33C33, C35C35, C55C55,), )
        The following items should then be specified as comma-separated data:
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        If *behavior*=NONLINEAR and *coupling*=COUPLED_POSITION or COUPLED_MOTION, each sequence of the table data
        specifies the following:
            - Force or moment for the directions in the *components* list.
            - Relative velocity for the directions in the *components* list.
            - Relative position or angle for the first *independentComponents* direction if *coupling*=COUPLED_POSITION.
          Relative displacement or rotation for the first *independentComponents* direction if *coupling*=COUPLED_MOTION.
            - Relative position or angle for the second *independentComponents* direction if *coupling*=COUPLED_POSITION.
          Relative displacement or rotation for the second *independentComponents* direction if *coupling*=COUPLED_MOTION.
            - Etc. up to the Nth *independentComponents* direction.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

    The corresponding analysis keywords are:
        - CONNECTOR DAMPING

    """

    # A ConnectorOptions object specifying the ConnectorOptions used to define tabular options
    # for this ConnectorBehaviorOption.
    options: ConnectorOptions = ConnectorOptions()

    def __init__(self,
                 behavior: SymbolicConstant = LINEAR,
                 coupling: SymbolicConstant = UNCOUPLED,
                 dependencies: int = 0,
                 temperatureDependency: Boolean = OFF,
                 frequencyDependency: Boolean = OFF,
                 table: Tuple = (),
                 independentComponents: Tuple = (),
                 components: Tuple = ()):
        """This method creates a connector damping behavior option for a ConnectorSection object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      import connectorBehavior
                      connectorBehavior.ConnectorDamping
                      import odbConnectorBehavior
                      odbConnectorBehavior.ConnectorDamping
        
        Parameters
        ----------
        behavior
            A SymbolicConstant specifying if the damping behavior is linear or nonlinear. Possible 
            values are LINEAR and NONLINEAR. The default value is LINEAR. 
        coupling
            A SymbolicConstant specifying whether the damping behavior is coupled between the 
            connector's components of relative motion. If *behavior*=LINEAR, then possible values 
            are UNCOUPLED and COUPLED. If *behavior*=NONLINEAR, then possible values are UNCOUPLED, 
            COUPLED_POSITION, and COUPLED_MOTION. Possible values are UNCOUPLED, COUPLED, 
            COUPLED_POSITION, and COUPLED_MOTION. The default value is UNCOUPLED. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        temperatureDependency
            A Boolean specifying whether the behavior data depend on temperature. The default value 
            is OFF. 
        frequencyDependency
            A Boolean specifying whether the behavior data depend on frequency. This value is 
            applicable only if *behavior*= LINEAR and *coupling*=UNCOUPLED. The default value is 
            OFF. 
        table
            A sequence of sequences of Floats specifying damping properties. Items in the table data 
            are described below. The default value is an empty sequence. 
        independentComponents
            A sequence of Ints specifying the list of independent components that are included in 
            the definition of the connector damping data. This argument is applicable only if 
            *behavior*=NONLINEAR and *coupling*=COUPLED_POSITION or COUPLED_MOTION. When this 
            argument is applicable, at least one value must be specified. Only available components 
            can be specified. The default value is an empty sequence. 
        components
            A sequence of Ints specifying the components of relative motion for which the behavior 
            is defined. Possible values are 1 ≤≤ *components* ≤≤ 6. Only available components can be 
            specified. The default value is an empty sequence. 

        Returns
        -------
            A ConnectorDamping object. 

        Raises
        ------
            ValueError and TextError. 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the ConnectorDamping object.

        Raises
        ------
            ValueError. 
        """
        pass
