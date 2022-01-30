class MpcConstraint:
    """The MpcConstraint object.

    Notes
    -----
        This object can be accessed by:
        - import visualization
        - session.odbData[name].multiPointConstraints[i]

    """

    # A String specifying the multipoint constraint name. This attribute is read-only. 
    name: str = ''

    def constraintData(self):
        """This method returns constraint data if any are associated with the object.

        Parameters
        ----------

        Returns
        -------
            A tuple containing coordinates of the nodes pertaining to the constraint. . 
        """
        pass
