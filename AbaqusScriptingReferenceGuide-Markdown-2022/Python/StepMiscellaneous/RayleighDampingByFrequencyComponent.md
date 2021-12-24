# RayleighDampingByFrequencyComponent object

A RayleighDampingByFrequencyComponent object is used to define Rayleigh damping over a range of frequencies.

## Access

```
import step
mdb.models[name].steps[name].rayleighDampingByFrequency.components[i]
```

## Members

The RayleighDampingByFrequencyComponent object has the following members:

- *frequency*

  A Float specifying the frequency value in cycles/time.

- *alpha*

  A Float specifying the mass proportional damping, αM.

- *beta*

  A Float specifying the stiffness proportional damping, βM.