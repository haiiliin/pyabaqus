# DataTable object

A DataTable is an object used to define the domain and data for a [DiscreteField](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?ContextScope=all).

## Access

```
import field
mdb.models[name].discreteFields[name].data[i]
```

## Members

The DataTable object has the following members:

- *dataWidth*

  An Int specifying the width of the data. Valid widths are 1, 6, 21, corresponding to scalar data, orientations and 4D tensors.

- *name*

  A String specifying the index.

- *instanceName*

  A String specifying the instance name.

- *domain*

  A tuple of Ints specifying the domain node, element or integration point identifiers.

- *table*

  A tuple of Floats specifying the data within the domain.