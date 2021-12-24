# EosCompaction object

The EosCompaction object specifies material eos compaction.

## Access

```
import material
mdb.models[name].materials[name].eos.eosCompaction
import odbMaterial
session.odbs[name].materials[name].eos.eosCompaction
```

## EosCompaction(...)



This method creates an EosCompaction object.



### Path

```
mdb.models[name].materials[name].eos.EosCompaction
session.odbs[name].materials[name].eos.EosCompaction
```

### Required arguments

- *soundSpeed*

  A Float specifying reference sound speed in the porous material.

- *porosity*

  A Float specifying value of the porosity of the unloaded material.

- *pressure*

  A Float specifying pressure required to initialize plastic behavior.

- *compactionPressure*

  A Float specifying compaction pressure at which all pores are crushed.

### Optional arguments

None.

### Return value

An EosCompaction object.

### Exceptions

RangeError.



## setValues(...)



This method modifies the EosCompaction object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [EosCompaction ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eoscompactionpyc.htm?ContextScope=all#simaker-eoscompactioneoscompactionpyc)method.

### Return value

None.

### Exceptions

RangeError.



## Members

The EosCompaction object has members with the same names and descriptions as the arguments to the [EosCompaction ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eoscompactionpyc.htm?ContextScope=all#simaker-eoscompactioneoscompactionpyc)method.



## Corresponding analysis keywords

- [EOS COMPACTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-eoscompaction.htm?ContextScope=all#simakey-r-eoscompaction)