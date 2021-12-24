# ConnectorLock object

The ConnectorLock object defines locking criteria for one or more available components of a connector's relative motion.

The ConnectorLock object is derived from the [ConnectorBehaviorOption](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorbehavioroptionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name].behaviorOptions[i]
import odbSection
session.odbs[name].sections[name].behaviorOptions[i]
```

## ConnectorLock(...)



This method creates a connector lock behavior option for a [ConnectorSection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorsectionpyc.htm?ContextScope=all).



### Path

```
          import connectorBehavior
          connectorBehavior.ConnectorLock
          import odbConnectorBehavior
          odbConnectorBehavior.ConnectorLock
        
```

### Required arguments

None.

### Optional arguments

- *lockingComponent*

  The SymbolicConstant ALL or an Int specifying the motion components that are locked. If an Int is specified, only that motion component is locked when the locking criteria are satisfied. If *lockingComponent*=ALL, all motion components are locked. The default value is ALL.

- *minMotion*

  None or a Float specifying the lower bound for the connector's relative position for all specified components, or no lower bound. The default value is None.

- *maxMotion*

  None or a Float specifying the upper bound for the connector's relative position for all specified components, or no upper bound. The default value is None.

- *minForce*

  None or a Float specifying the lower bound of the force or moment in the directions of the specified components at which locking occurs, or no lower bound. The default value is None.

- *maxForce*

  None or a Float specifying the upper bound of the force or moment in the directions of the specified components at which locking occurs, or no upper bound. The default value is None.

- *components*

  A sequence of Ints specifying the components of relative motion for which the behavior is defined. Possible values are 1 ≤≤ *components* ≤≤ 6. Only available components can be specified. The default value is an empty sequence.

### Return value

A ConnectorLock object.

### Exceptions

ValueError and TextError.



## setValues(...)



This method modifies the ConnectorLock object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConnectorLock ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorlockpyc.htm?ContextScope=all#simaker-connectorlockconnectorlockpyc)method.

### Return value

None.

### Exceptions

ValueError.



## Members

The ConnectorLock object has members with the same names and descriptions as the arguments to the [ConnectorLock ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorlockpyc.htm?ContextScope=all#simaker-connectorlockconnectorlockpyc)method.



## Corresponding analysis keywords

[CONNECTOR LOCK](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorlock.htm?ContextScope=all#simakey-r-connectorlock)