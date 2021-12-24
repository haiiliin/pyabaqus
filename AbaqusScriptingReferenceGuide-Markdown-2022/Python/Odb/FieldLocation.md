# FieldLocation object

The FieldLocation object specifies locations for which data are available in the field. For example, a displacement field will have a FieldLocation object with a *position* member value of NODAL. The FieldLocation object has no constructor; it is created automatically as an element of the *location* member of a [FieldOutput](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputpyc.htm?ContextScope=all) object by the addData method of a [FieldOutput](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputpyc.htm?ContextScope=all) object.

## Access

```
import odbAccess
session.odbs[name].steps[name].frames[i].fieldOutputs[name]\
.locations[i]
```

## Members

The FieldLocation object can have the following members:

- *position*

  A SymbolicConstant specifying the position of the output in the element. Possible values are:NODAL, specifying the values calculated at the nodes.INTEGRATION_POINT, specifying the values calculated at the integration points.ELEMENT_NODAL, specifying the values obtained by extrapolating results calculated at the integration points.ELEMENT_FACE.CENTROID, specifying the value at the centroid obtained by extrapolating results calculated at the integration points.

- *sectionPoints*

  A [SectionPointArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpointpyc.htm?ContextScope=all) object.