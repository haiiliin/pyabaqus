# ConnectorStop object

The ConnectorStop object defines connector stops for one or more components of a connector's relative motion.

The ConnectorStop object is derived from the [ConnectorBehaviorOption](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorbehavioroptionpyc.htm?ContextScope=all) object.

## Access

```
import section
mdb.models[name].sections[name].behaviorOptions[i]
import odbSection
session.odbs[name].sections[name].behaviorOptions[i]
```

## ConnectorStop(...)



This method creates a connector stop behavior option for a [ConnectorSection](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorsectionpyc.htm?ContextScope=all) object.



### Path

```
          import connectorBehavior
          connectorBehavior.ConnectorStop
          import odbConnectorBehavior
          odbConnectorBehavior.ConnectorStop
        
```

### Required arguments

None.

### Optional arguments

- *minMotion*

  None or a Float specifying the lower bound for the connector's relative position for all specified components, or no lower bound. The default value is None.

- *maxMotion*

  None or a Float specifying the upper bound for the connector's relative position for all specified components, or no upper bound. The default value is None.

- *components*

  A sequence of Ints specifying the components of relative motion for which the behavior is defined. Possible values are 1 ≤≤ *components* ≤≤ 6. Only available components can be specified. The default value is an empty sequence.

### Return value

A ConnectorStop object.

### Exceptions

ValueError and TextError.



## setValues(...)



This method modifies the ConnectorStop object.



### Required arguments

None.

### Optional arguments

The optional arguments to setValues are the same as the arguments to the [ConnectorStop ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorstoppyc.htm?ContextScope=all#simaker-connectorstopconnectorstoppyc)method.

### Return value

None.

### Exceptions

ValueError.



## Members

The ConnectorStop object has members with the same names and descriptions as the arguments to the [ConnectorStop ](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorstoppyc.htm?ContextScope=all#simaker-connectorstopconnectorstoppyc)method.



## Corresponding analysis keywords

- [CONNECTOR STOP](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKEYRefMap/simakey-r-connectorstop.htm?ContextScope=all#simakey-r-connectorstop)