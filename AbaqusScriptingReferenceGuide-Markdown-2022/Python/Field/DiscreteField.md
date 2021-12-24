# DiscreteField object

The DiscreteField object defines a varying field whose values correspond to distinct points within a domain.

The DiscreteField object is derived from the [Field](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldpyc.htm?ContextScope=all) object.

## Access

```
import fields
mdb.models[name].discreteFields[name]
```

## DiscreteField(...)



This method creates a DiscreteField object.



### Path

```
mdb.models[name].DiscreteField
```

### Required arguments

- *name*

  A String specifying the repository key.

- *defaultValues*

  A sequence of Floats specifying a sequence of floats specifying the default values.

- *fieldType*

  A SymbolicConstant or an Int specifying the type of data represented by this discrete field. Possible values are SCALAR, ORIENTATION, and PRESCRIBEDCONDITION_DOF.

### Optional arguments

- *location*

  A SymbolicConstant or an Int specifying the location of the domain data. Possible values are NODES and ELEMENTS. The default value is NODES.

- *dataWidth*

  An Int specifying the width of the supplied data. The default value is 1.

- *data*

  A [DataTableArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datatablepyc.htm?ContextScope=all) object.

- *description*

  A String specifying the description of the field. The default value is an empty string.

- *orientationType*

  A SymbolicConstant specifying the type of the system being described by a discrete field used for an orientation. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL. The default value is CARTESIAN.

- *partLevelOrientation*

  A Boolean specifying whether or not the orientations are described in terms of part level coordinates. The default value is OFF.

### Return value

A DiscreteField object.

### Exceptions

AbaqusException.



## DiscreteFieldByVolumeFraction(...)



This method creates a DiscreteField object that represents the volume fraction of each element of an Eulerian Instance that is occupied by a reference instance.



### Path

mdb.models[*name*].rootAssembly.DiscreteFieldByVolumeFraction

### Required arguments

- *name*

  A String specifying the repository key.

- *eulerianInstance*

  A [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) object specifying the elements for which volume fraction values will be computed.

- *referenceInstance*

  A [PartInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?ContextScope=all) object specifying the region that either contains material or is empty of material.

### Optional arguments

- *accuracy*

  A Symbolic Constant specifying the level of accuracy that will be used in computing volume fractions. Possible values are LOW, MEDIUM, or HIGH. The default value is MEDIUM.

- *materialLocation*

  A Symbolic Constant indicating whether the material is inside or outside the *referenceInstance*. Possible values are INSIDE or OUTSIDE. The default value is INSIDE.

- *description*

  A String specifying the description of the field. The default value is an empty string.

- *scaleFactor*

  A float specifying the fraction of the volume that is occupied by the *referenceInstance.* Valid values are between 0 and 1.

### Return value

A DiscreteField object.

### Exceptions

AbaqusException.



## DiscreteFieldFromAnalytic(...)



This method creates a DiscreteField object from a [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) object.



### Path

```
mdb.models[name].DiscreteFieldFromAnalytic
```

### Required arguments

- *name*

  A String specifying the repository key.

- *location*

  A SymbolicConstant or an Int specifying the location of the domain data. Possible values are NODES and ELEMENTS. The default value is NODES.

- *analyticFieldName*

  A String specifying the name of the [AnalyticalField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?ContextScope=all) containing the source data.

- *region*

  A [Region](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-regionpyc.htm?ContextScope=all) object for the field.

### Optional arguments

None.

### Return value

A DiscreteField object.

### Exceptions

AbaqusException.



## setValues(...)



This method modifies the DiscreteField object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [DiscreteField ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all#simaker-discretefielddiscretefieldpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

None.



## Members

The DiscreteField object has members with the same names and descriptions as the arguments to the [DiscreteField ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all#simaker-discretefielddiscretefieldpyc)method.