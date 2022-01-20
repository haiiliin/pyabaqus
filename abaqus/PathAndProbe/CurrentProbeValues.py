
class CurrentProbeValues:
    """The CurrentProbeValues object has no constructor. The CurrentProbeValues object is
    created when you import the Visualization module. 

    Access
    ------
        - import visualization
        - session.currentProbeValues

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A tuple of Floats specifying the values obtained while probing. These values are updated 
    # constantly as the user moves the mouse over the object being probed. 
    values: tuple[float] = None
