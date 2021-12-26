from .Section import Section
from .TransverseShearShell import TransverseShearShell

class ShellSection(Section):

    """The ShellSection object defines the properties of a shell section. The ShellSection 
    object is derived from the Section object. The ShellSection object has no explicit 
    constructor and no methods or members. 
    The ShellSection object is derived from the Section object. 

    Access
    ------
        - import section
        - mdb.models[name].sections[name]
        - import odbSection
        - session.odbs[name].sections[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the repository key. 
    name: str = ''

    # A TransverseShearShell object specifying the transverse shear stiffness properties. 
    transverseShear: TransverseShearShell = TransverseShearShell()

