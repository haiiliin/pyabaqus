from abaqus.Calibration.Calibration import Calibration
from abaqus.Model.ModelBase import ModelBase


class CalibrationModel(ModelBase):

    def Calibration(self, name: str) -> Calibration:
        """This method creates a Calibration object.

        Path
        ----
            -           mdb.models[name].Calibration

        Parameters
        ----------
        name
            A String specifying the name of the new calibration.

        Returns
        -------
            A Calibration object.

        Exceptions
        ----------
            InvalidNameError.
        """
        self.calibrations[name] = calibration = Calibration(name)
        return calibration
