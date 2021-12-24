# Datum object

The Datum object is the abstract base type for other Datum objects. The Datum object has no explicit constructor. The methods and members of the Datum object are common to all objects derived from the Datum.

## Access

```
import part
mdb.models[name].parts[name].datums[i]
import assembly
mdb.models[name].rootAssembly.allInstances[name].datums[i]
mdb.models[name].rootAssembly.datums[i]
mdb.models[name].rootAssembly.instances[name].datums[i]
mdb.models[name].rootAssembly.modelInstances[i].datums[i]
```

## Members

The Datum object has no members.