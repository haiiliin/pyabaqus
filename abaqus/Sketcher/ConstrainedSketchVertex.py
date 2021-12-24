

class ConstrainedSketchVertex:

    """The ConstrainedSketchVertex object stores the vertex position. 

    Access
    ------
        - import sketch
        - mdb.models[name].sketches[name].vertices[i]
        - mdb.models[name].sketches[name].vertices[i][i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A tuple of Floats specifying the*X*-, *Y*-, and *Z*-coordinates of the sketch vertex. 
    coords: float = None

    def Spot(self, point: tuple[float]):
        """This method creates a spot (construction point) located at the specified coordinates.

        Path
        ----
            - mdb.models[name].sketches[name].Spot

        Parameters
        ----------
        point
            A pair of Floats specifying the coordinates of the construction point. 

        Returns
        -------
            A ConstrainedSketchVertex object (None if the spot cannot be created). 

        Exceptions
        ----------
            None. 
        """
        pass

