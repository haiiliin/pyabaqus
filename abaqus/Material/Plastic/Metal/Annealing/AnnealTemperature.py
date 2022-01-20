
class AnnealTemperature:
    """The AnnealTemperature object specifies the material annealing temperature.

    Access
    ------
        - import material
        - mdb.models[name].materials[name].Plastic.annealTemperature
        - import odbMaterial
        - session.odbs[name].materials[name].Plastic.annealTemperature

    Table Data
    ----------
        - The annealing temperature, θθ.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - ANNEAL TEMPERATURE

    """

    def __init__(self, table: tuple, dependencies: int = 0):
        """This method creates an AnnealTemperature object.

        Path
        ----
            - mdb.models[name].materials[name].Plastic.AnnealTemperature
            - session.odbs[name].materials[name].Plastic.AnnealTemperature

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            An AnnealTemperature object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the AnnealTemperature object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass
