from abaqusConstants import *
from .BoundaryCondition import BoundaryCondition
from ..Region.Region import Region


class TypeBC(BoundaryCondition):
    """The TypeBC object stores the data for several types of predefined boundary conditions
    that are commonly used in stress/displacement analyses. 
    The TypeBC object is derived from the BoundaryCondition object. 

    Attributes
    ----------
    name: str
        A String specifying the boundary condition repository key.
    buckleCase: SymbolicConstant
        A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
        analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and
        PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE.
    category: SymbolicConstant
        A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.
    region: Region
        A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the boundary condition is applied.
    localCsys: str
        None or a :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system of the boundary
        condition's degrees of freedom. If **localCsys=None**, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].boundaryConditions[name]

    """

    # A String specifying the boundary condition repository key. 
    name: str = ''

    # A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE 
    # analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and 
    # PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE. 
    buckleCase: SymbolicConstant = NOT_APPLICABLE

    # A SymbolicConstant specifying the category of the boundary condition. Possible values 
    # are MECHANICAL and THERMAL. 
    category: SymbolicConstant = None

    # A Region object specifying the region to which the boundary condition is applied. 
    region: Region = Region()

    # None or a DatumCsys object specifying the local coordinate system of the boundary 
    # condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
    # in the global coordinate system. The default value is None. 
    localCsys: str = None

    def EncastreBC(self, name: str, createStepName: str, region: Region,
                   buckleCase: SymbolicConstant = NOT_APPLICABLE, localCsys: str = None):
        """This method creates an encastre TypeBC object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].EncastreBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE 
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and 
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 

        Returns
        -------
            A TypeBC object.
        """
        pass

    def PinnedBC(self, name: str, createStepName: str, region: Region,
                 buckleCase: SymbolicConstant = NOT_APPLICABLE, localCsys: str = None):
        """This method creates a pinned TypeBC object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].EncastreBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE 
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and 
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 

        Returns
        -------
            A TypeBC object.
        """
        pass

    def XsymmBC(self, name: str, createStepName: str, region: Region,
                buckleCase: SymbolicConstant = NOT_APPLICABLE, localCsys: str = None):
        """This method creates a TypeBC object that specifies symmetry about the *X*-axis.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].EncastreBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE 
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and 
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 

        Returns
        -------
            A TypeBC object.
        """
        pass

    def YsymmBC(self, name: str, createStepName: str, region: Region,
                buckleCase: SymbolicConstant = NOT_APPLICABLE, localCsys: str = None):
        """This method creates a TypeBC object that specifies symmetry about the *Y*-axis.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].EncastreBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE 
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and 
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 

        Returns
        -------
            A TypeBC object.
        """
        pass

    def ZsymmBC(self, name: str, createStepName: str, region: Region,
                buckleCase: SymbolicConstant = NOT_APPLICABLE, localCsys: str = None):
        """This method creates a TypeBC object that specifies symmetry about the *Z*-axis.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].EncastreBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE 
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and 
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 

        Returns
        -------
            A TypeBC object.
        """
        pass

    def XasymmBC(self, name: str, createStepName: str, region: Region,
                 buckleCase: SymbolicConstant = NOT_APPLICABLE, localCsys: str = None):
        """This method creates a TypeBC object that specifies antisymmetry about the *X*-axis.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].EncastreBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE 
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and 
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 

        Returns
        -------
            A TypeBC object.
        """
        pass

    def YasymmBC(self, name: str, createStepName: str, region: Region,
                 buckleCase: SymbolicConstant = NOT_APPLICABLE, localCsys: str = None):
        """This method creates a TypeBC object that specifies antisymmetry about the *Y*-axis.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].EncastreBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE 
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and 
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 

        Returns
        -------
            A TypeBC object.
        """
        pass

    def ZasymmBC(self, name: str, createStepName: str, region: Region,
                 buckleCase: SymbolicConstant = NOT_APPLICABLE, localCsys: str = None):
        """This method creates a TypeBC object that specifies antisymmetry about the *Z*-axis.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].EncastreBC
        
        Parameters
        ----------
        name
            A String specifying the boundary condition repository key. 
        createStepName
            A String specifying the name of the step in which the boundary condition is created. 
        region
            A Region object specifying the region to which the boundary condition is applied. 
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE 
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and 
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 

        Returns
        -------
            A TypeBC object.
        """
        pass

    def setValues(self, region: Region = Region(), typeName: SymbolicConstant = None,
                  buckleCase: SymbolicConstant = NOT_APPLICABLE, localCsys: str = None):
        """This method modifies the data for an existing TypeBC object in the step where it is
        created.
        
        Parameters
        ----------
        region
            A Region object specifying the region to which the boundary condition is applied. 
        typeName
            A SymbolicConstant specifying the predefined boundary condition type. Possible values 
            are XSYMM, YSYMM, ZSYMM, XASYMM, YASYMM, ZASYMM, PINNED, and ENCASTRE. 
        buckleCase
            A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE 
            analysis. Possible values are NOT_APPLICABLE, STRESS_PERTURBATION, BUCKLING_MODES, and 
            PERTURBATION_AND_BUCKLING. The default value is NOT_APPLICABLE. 
        localCsys
            None or a DatumCsys object specifying the local coordinate system of the boundary 
            condition's degrees of freedom. If *localCsys*=None, the degrees of freedom are defined 
            in the global coordinate system. The default value is None. 
        """
        pass

    def setValuesInStep(self, stepName: str, typeName: SymbolicConstant = None):
        """This method always returns a value error for a TypeBC; it is inherited from the
        BoundaryCondition object.
        
        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the boundary condition is modified. 
        typeName
            A SymbolicConstant specifying the predefined boundary condition type. Possible values 
            are XSYMM, YSYMM, ZSYMM, XASYMM, YASYMM, ZASYMM, PINNED, and ENCASTRE.

        Raises
        ------
            - Value Error: 
              A Symmetry/Antisymmetry/Encastre BC cannot be edited in a propagated step. 
        """
        pass
