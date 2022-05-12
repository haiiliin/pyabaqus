from abaqusConstants import *

from __init__ import *
from __future__ import annotations


class OdbAuxiliaryData:
    """The OdbAuxiliaryData object stores auxiliary data related to the steps in the analysis.

    Attributes
    ----------
    elementInstanceNames: Tuple
        A Tuple consisting of element instance names. This attribute is read-only.
    elementLabels: Tuple
        A Tuple consisting of element label names. This attribute is read-only.
    hasValues: Boolean
        A boolean specifying whether the :py:class:`~abaqus.PlotOptions.OdbAuxiliaryData.OdbAuxiliaryData` object has values in it. This
        attribute is read-only.
    nodeInstanceNames: Tuple
        A Tuple consisting of node instance names. This attribute is read-only.
    nodeLables: Tuple
        A Tuple consisting of node label names. This attribute is read-only.

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import visualization
            session.odbData[name].diagnosticData.analysisErrors[i].data[i]
            session.odbData[name].diagnosticData.analysisWarnings[i].data[i]
            session.odbData[name].diagnosticData.steps[i].contactDiagnostics[i].data[i]

    """

    # A Tuple consisting of element instance names. This attribute is read-only.
    elementInstanceNames: Tuple = ()

    # A Tuple consisting of element label names. This attribute is read-only.
    elementLabels: Tuple = ()

    # A boolean specifying whether the OdbAuxiliaryData object has values in it. This
    # attribute is read-only.
    hasValues: Boolean = OFF

    # A Tuple consisting of node instance names. This attribute is read-only.
    nodeInstanceNames: Tuple = ()

    # A Tuple consisting of node label names. This attribute is read-only.
    nodeLables: Tuple = ()
