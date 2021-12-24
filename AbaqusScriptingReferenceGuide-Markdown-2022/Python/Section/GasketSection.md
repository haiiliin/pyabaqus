# GasketSection object

The GasketSection object defines the properties of a gasket section.

The GasketSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## GasketSection(...)



This method creates a GasketSection object.



### Path

```
mdb.models[name].GasketSection
session.odbs[name].GasketSection
```

### Required arguments

- *name*

  A String specifying the repository key.

- *material*

  A String specifying the name of the material of which the gasket is made or material that defines gasket behavior.

### Optional arguments

- *crossSection*

  A Float specifying the cross-sectional area, width, or out-of-plane thickness, if applicable, depending on the gasket element type. The default value is 1.0.

- *initialGap*

  A Float specifying the initial gap. The default value is 0.0.

- *initialThickness*

  The SymbolicConstant DEFAULT or a Float specifying the initial gasket thickness. If DEFAULT is specified, the initial thickness is determined using nodal coordinates. The default value is DEFAULT.

- *initialVoid*

  A Float specifying the initial void. The default value is 0.0.

- *stabilizationStiffness*

  The SymbolicConstant DEFAULT or a Float specifying the default stabilization stiffness used in all but link elements to stabilize gasket elements that are not supported at all nodes, such as those that extend outside neighboring components. If DEFAULT is specified, a value is used equal to 10–9 times the initial compressive stiffness in the thickness direction. The default value is DEFAULT.

### Return value

A GasketSection object.

### Exceptions

InvalidNameError and ValueError.



## setValues(...)



This method modifies the GasketSection object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [GasketSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gasketsectionpyc.htm?ContextScope=all#simaker-gasketsectiongasketsectionpyc)method, except for the *name* argument.

### Return value

None.

### Exceptions

ValueError.



## Members

The GasketSection object has members with the same names and descriptions as the arguments to the [GasketSection ](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gasketsectionpyc.htm?ContextScope=all#simaker-gasketsectiongasketsectionpyc)method.



## Corresponding analysis keywords

- [GASKET SECTION](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-gasketsection.htm?ContextScope=all#simakey-r-gasketsection)