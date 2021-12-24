# DisplayGroupInstanceRepository object

The DisplayGroupInstanceRepository object stores [DisplayGroupInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygroupinstancepyc.htm?ContextScope=all) objects. In addition to all the standard Python repository methods, the [DisplayGroupInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygroupinstancepyc.htm?ContextScope=all) repository defines additional methods as described below.

## Access

```
        import visualization
        session.viewports[name].layers[name].odbDisplay.displayGroupInstances
        session.viewports[name].odbDisplay.displayGroupInstances
      
```

## syncOptions(...)



This method synchronizes the display options stored on the [OdbDisplay](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdisplaypyc.htm?ContextScope=all) object with the display options stored on the [DisplayGroupInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygroupinstancepyc.htm?ContextScope=all) object.



### Required arguments

- *name*

  A String specifying the repository key.

### Optional arguments

- *updateInstances*

  A Boolean specifying whether to synchronize the display options on all the [DisplayGroupInstance](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displaygroupinstancepyc.htm?ContextScope=all) objects stored in the DisplayGroupInstanceRepository for which *lockOptions* is OFF. The default value of *updateInstances* is ON.

### Return value

None.

### Exceptions

None.



## Members

The DisplayGroupInstanceRepository object has no members.