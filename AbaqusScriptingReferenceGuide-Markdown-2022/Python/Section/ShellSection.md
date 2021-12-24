# ShellSection object

The ShellSection object defines the properties of a shell section. The ShellSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object. The ShellSection object has no explicit constructor and no methods or members.

The ShellSection object is derived from the [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name]
import odbSection
session.odbs[name].sections[name]
```

## Members

The ShellSection object can have the following members:

- *name*

  A String specifying the repository key.

- *transverseShear*

  A [TransverseShearShell](https://help.3ds.com/2022/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-transverseshearshellpyc.htm?ContextScope=all) object specifying the transverse shear stiffness properties.