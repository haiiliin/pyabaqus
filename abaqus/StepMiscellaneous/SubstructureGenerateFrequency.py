class SubstructureGenerateFrequency:
    """A SubstructureGenerateFrequency object is used to define the modes to be used in a modal
    dynamic analysis. These modes are selected from the specified frequency range including 
    the frequency boundary. 

    Access
    ------
        - import step
        - mdb.models[name].steps[name].frequencyRange[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A Float specifying the lower limit of the frequency range, in cycles/time. 
    lower: float = None

    # A Float specifying the upper limit of the frequency range, in cycles/time. 
    upper: float = None
