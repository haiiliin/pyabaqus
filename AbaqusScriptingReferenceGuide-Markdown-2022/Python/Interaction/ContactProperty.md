# ContactProperty object

The ContactProperty object defines a contact interaction property.

The ContactProperty object is derived from the [InteractionProperty](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-interactionpropertypyc.htm?ContextScope=all) object.

## Access

```
import interaction
mdb.models[name].interactionProperties[name]
```

## ContactProperty(...)



This method creates a ContactProperty object.



### Path

```
mdb.models[name].ContactProperty
```

### Required arguments

- *name*

  A String specifying the interaction property repository key.

### Optional arguments

None.

### Return value

A ContactProperty object.

### Exceptions

None.



## Members

The ContactProperty object can have the following members:

- *tangentialBehavior*

  A [ContactTangentialBehavior](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contacttangentialbehaviorpyc.htm?ContextScope=all) object.

- *normalBehavior*

  A [NormalBehavior](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-normalbehaviorpyc.htm?ContextScope=all) object.

- *damping*

  A [ContactDamping](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactdampingpyc.htm?ContextScope=all) object.

- *damage*

  A [ContactDamage](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactdamagepyc.htm?ContextScope=all) object.

- *fractureCriterion*

  A [FractureCriterion](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fracturecriterionpyc.htm?ContextScope=all) object.

- *cohesiveBehavior*

  A [CohesiveBehavior](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cohesivebehaviorpyc.htm?ContextScope=all) object.

- *thermalConductance*

  A [ThermalConductance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-thermalconductancepyc.htm?ContextScope=all) object.

- *heatGeneration*

  A [GapHeatGeneration](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gapheatgenerationpyc.htm?ContextScope=all) object.

- *radiation*

  A [Radiation](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-radiationpyc.htm?ContextScope=all) object.

- *geometricProperties*

  A [GeometricProperties](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricpropertiespyc.htm?ContextScope=all) object.

- *electricalConductance*

  A [GapElectricalConductance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gapelectricalconductancepyc.htm?ContextScope=all) object.



## Corresponding analysis keywords

- [SURFACE INTERACTION](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-surfaceinteraction.htm?ContextScope=all#simakey-r-surfaceinteraction)