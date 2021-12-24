from .OdbDatumCsys import OdbDatumCsys
from .OdbSet import OdbSet
from abaqusConstants import *

class RebarOrientation:

    """The RebarOrientation object represents the orientation of the rebar reference. 

    Access
    ------
        - import odbAccess
        - session.odbs[name].parts[name].rebarOrientations[i]
        - session.odbs[name].rootAssembly.instances[name].rebarOrientations[i]
        - session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.rebarOrientations[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate 
    # system about which an additional rotation is applied. Possible values are AXIS_1, 
    # AXIS_2, and AXIS_3. 
    axis: SymbolicConstant = None

    # A Float specifying the angle of the additional rotation. 
    angle: float = None

    # An OdbSet object specifying a region for which the rebar orientation is defined. 
    region: OdbSet = None

    # An OdbDatumCsys object specifying a datum coordinates system. 
    csys: OdbDatumCsys = None

