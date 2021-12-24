# SectionPoint object

The SectionPoint object describes the location of a section point within a section category.

## Access

```
import
odbAccess
session.odbs[name].parts[name].elements[i].sectionCategory\
.sectionPoints[i]
session.odbs[name].parts[name].elementSets[name].elements[i]\
.sectionCategory.sectionPoints[i]
session.odbs[name].parts[name].nodeSets[name].elements[i]\
.sectionCategory.sectionPoints[i]
session.odbs[name].parts[name].surfaces[name].elements[i]\
.sectionCategory.sectionPoints[i]
session.odbs[name].rootAssembly.elements[i].sectionCategory\
.sectionPoints[i]
session.odbs[name].rootAssembly.elementSets[name].elements[i]\
.sectionCategory.sectionPoints[i]
session.odbs[name].rootAssembly.instances[name].elements[i]\
.sectionCategory.sectionPoints[i]
session.odbs[name].rootAssembly.instances[name].elementSets[name]\
.elements[i].sectionCategory.sectionPoints[i]
session.odbs[name].rootAssembly.instances[name].nodeSets[name]\
.elements[i].sectionCategory.sectionPoints[i]
session.odbs[name].rootAssembly.instances[name].surfaces[name]\
.elements[i].sectionCategory.sectionPoints[i]
session.odbs[name].rootAssembly.nodeSets[name].elements[i]\
.sectionCategory.sectionPoints[i]
session.odbs[name].rootAssembly.surfaces[name].elements[i]\
.sectionCategory.sectionPoints[i]
session.odbs[name].sectionCategories[name].sectionPoints[i]
session.odbs[name].steps[name].frames[i].fieldOutputs[name]\
.locations[i].sectionPoints[i]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.elements[i].sectionCategory.sectionPoints[i]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.elementSets[name].elements[i].sectionCategory\
.sectionPoints[i]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.nodeSets[name].elements[i].sectionCategory.sectionPoints[i]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.instance.surfaces[name].elements[i].sectionCategory.sectionPoints[i]
session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]\
.sectionPoint
```

## SectionPoint(...)



This method creates a SectionPoint object.



### Path

session.odbs[*name*].sectionCategories[*name*].SectionPoint

### Required arguments

- *number*

  An Int specifying the number of the section point. See [Beam elements](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-m-BeamElements-sb.htm?ContextScope=all) and [Shell elements](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-m-ShellElements-sb.htm?ContextScope=all) for the numbering convention.

- *description*

  A String specifying the description of the section point.

### Optional arguments

None.

### Return value

A SectionPoint object.

### Exceptions

None.



## Members

The SectionPoint object has members with the same names and descriptions as the arguments to the [SectionPoint ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpointpyc.htm?ContextScope=all#simaker-sectionpointsectionpointpyc)method.