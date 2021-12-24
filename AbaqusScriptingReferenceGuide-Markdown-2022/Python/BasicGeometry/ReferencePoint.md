# ReferencePoint object

The ReferencePoint object has no direct constructor; it is created when a [Feature](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) object is created. The ReferencePoint method creates a [Feature](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-featurepyc.htm?ContextScope=all) object that creates a ReferencePoint object.

## Access

```
import part
mdb.models[name].parts[name].allInternalSets[name].referencePoints[i]
mdb.models[name].parts[name].allSets[name].referencePoints[i]
mdb.models[name].parts[name].referencePoints[i]
mdb.models[name].parts[name].sets[name].referencePoints[i]
import assembly
mdb.models[name].rootAssembly.allInstances[name].referencePoints[i]
mdb.models[name].rootAssembly.allInstances[name].sets[name]\
.referencePoints[i]
mdb.models[name].rootAssembly.allInternalSets[name].referencePoints[i]
mdb.models[name].rootAssembly.allSets[name].referencePoints[i]
mdb.models[name].rootAssembly.instances[name].referencePoints[i]
mdb.models[name].rootAssembly.instances[name].sets[name]\
.referencePoints[i]
mdb.models[name].rootAssembly.modelInstances[i].referencePoints[i]
mdb.models[name].rootAssembly.modelInstances[i].sets[name]\
.referencePoints[i]
mdb.models[name].rootAssembly.referencePoints[i]
mdb.models[name].rootAssembly.sets[name].referencePoints[i]
```

## Members

The ReferencePoint object has no members.