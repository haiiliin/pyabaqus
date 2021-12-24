# SectionCategory object

The SectionCategory object is used to group regions of the model with like sections. Section definitions that contain the same number of section points or integration points are grouped together.

To access data for a particular section definition, use the individual [Section](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpyc.htm?ContextScope=all) objects in the output database. For more information, see [Beam Section profile commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-BpfPyc-sb.htm?ContextScope=all) and [Section commands](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-SctPyc-sb.htm?ContextScope=all).

## Access

```
import
odbAccess
session.odbs[name].parts[name].elements[i].sectionCategory
session.odbs[name].parts[name].elementSets[name].elements[i]\
.sectionCategory
session.odbs[name].parts[name].nodeSets[name].elements[i]\
.sectionCategory
session.odbs[name].parts[name].surfaces[name].elements[i]\
.sectionCategory
session.odbs[name].rootAssembly.elements[i].sectionCategory
session.odbs[name].rootAssembly.elementSets[name].elements[i]\
.sectionCategory
session.odbs[name].rootAssembly.instances[name].elements[i]\
.sectionCategory
session.odbs[name].rootAssembly.instances[name].elementSets[name]\
.elements[i].sectionCategory
session.odbs[name].rootAssembly.instances[name].nodeSets[name]\
.elements[i].sectionCategory
session.odbs[name].rootAssembly.instances[name].surfaces[name]\
.elements[i].sectionCategory
session.odbs[name].rootAssembly.nodeSets[name].elements[i]\
.sectionCategory
session.odbs[name].rootAssembly.surfaces[name].elements[i]\
.sectionCategory
session.odbs[name].sectionCategories[name]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.elements[i].sectionCategory
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.elementSets[name].elements[i].sectionCategory
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.nodeSets[name].elements[i].sectionCategory
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.surfaces[name].elements[i].sectionCategory
```

## SectionCategory(...)



This method creates a SectionCategory object.



### Path

session.odbs[*name*].SectionCategory

### Required arguments

- *name*

  A String specifying the name of the category.

- *description*

  A String specifying the description of the category.

### Optional arguments

None.

### Return value

A SectionCategory object.

### Exceptions

None.



## Members

The SectionCategory object has members with the same names and descriptions as the arguments to the [SectionCategory ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectioncategorypyc.htm?ContextScope=all#simaker-sectioncategorysectioncategorypyc)method.

In addition, the SectionCategory object can have the following member:

- *sectionPoints*

  A [SectionPointArray](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpointpyc.htm?ContextScope=all) object.