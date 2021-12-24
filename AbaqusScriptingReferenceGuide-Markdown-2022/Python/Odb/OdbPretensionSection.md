# OdbPretensionSection object

The pretension section object is used to define an assembly load. It associates a pretension node with a pretension section.

## Access

```
import odbAccess
session.odbs[name].rootAssembly.pretensionSections[i]
```

## Members

The OdbPretensionSection object can have the following members:

- *node*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) object specifying the node set containing the pretension node.

- *element*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) object specifying the element set that defines the pretension section.

- *surface*

  An [OdbSet](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?ContextScope=all) object specifying the surface set that defines the pretension section.

- *normal*

  A tuple of Floats specifying the components of the normal to the pretension section.