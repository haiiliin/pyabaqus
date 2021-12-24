# BeamOrientation object

The BeamOrientation object represents the direction of the first beam section axis n1n1. Specifying the beam orientation using an additional node in the element connectivity list is not supported.

## Access

```
import odbAccess
session.odbs[name].parts[name].beamOrientations[i]
session.odbs[name].rootAssembly.instances[name].beamOrientations[i]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.beamOrientations[i]
```

## Members

The BeamOrientation object can have the following members:

- *method*

  A SymbolicConstant specifying the orientation assignment method. Possible values are N1_COSINES, CSYS, and VECT.

- *region*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) object specifying a region for which the beam orientation is defined.

- *vector*

  A tuple of Floats specifying direction cosines of the n1-direction of the beam cross-section.