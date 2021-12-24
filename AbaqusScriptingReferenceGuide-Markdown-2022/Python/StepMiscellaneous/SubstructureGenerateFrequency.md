# SubstructureGenerateFrequency object

A SubstructureGenerateFrequency object is used to define the modes to be used in a modal dynamic analysis. These modes are selected from the specified frequency range including the frequency boundary.

## Access

```
import step
mdb.models[name].steps[name].frequencyRange[i]
```

## Members

The SubstructureGenerateFrequency object has the following members:

- *lower*

  A Float specifying the lower limit of the frequency range, in cycles/time.

- *upper*

  A Float specifying the upper limit of the frequency range, in cycles/time.