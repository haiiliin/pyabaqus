# DisplayGroup object

DisplayGroup objects are used to select a subset of the entities displayed in the viewport.

## Access

```
        session.displayGroups[name]
        import assembly
        session.viewports[name].assemblyDisplay.displayGroup
        session.viewports[name].layers[name].assemblyDisplay.displayGroup
        import visualization
        session.viewports[name].layers[name].odbDisplay.displayGroup
        import part
        session.viewports[name].layers[name].partDisplay.displayGroup
        session.viewports[name].odbDisplay.displayGroup
        session.viewports[name].partDisplay.displayGroup
      
```

## DisplayGroup(...)



This method creates a DisplayGroup object.



### Path

session.DisplayGroup

### Required arguments

- *name*

  A String specifying the repository key.

- *leaf*

  A [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object specifying the items in the display group.

### Optional arguments

None.

### Return value

A DisplayGroup object.

### Exceptions

InvalidNameError.



## add(...)



This method adds the specified items to the display group.



### Required arguments

- *leaf*

  A [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object specifying the items to add to the display group.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## either(...)



This method redefines the display group to be only those items that are not shared by the *leaf* argument and by the display group.



### Required arguments

- *leaf*

  A [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object specifying the items to be excluded from the display group.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## intersect(...)



This method redefines the display group to be only those items that are shared by the *leaf* argument and the display group.



### Required arguments

- *leaf*

  A [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object specifying the items to be included in the display group.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## redoLast()



This method redoes the last undone operation on the display group.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## remove(...)



This method removes the specified items from the display group.



### Required arguments

- *leaf*

  A [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object specifying the items to remove from the display group.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## replace(...)



This method replaces the contents of the display group with the specified items.



### Required arguments

- *leaf*

  A [Leaf](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-leafpyc.htm?ContextScope=all) object specifying the items with which to replace the current display group contents.

### Optional arguments

None.

### Return value

None.

### Exceptions

None.



## undoLast()



This method undoes the last operation performed on the display group.



### Arguments

None.

### Return value

None.

### Exceptions

None.



## Members

The DisplayGroup object has the following members:

- *canUndo*

  A Boolean specifying whether Undo is possible or not.

- *canRedo*

  A Boolean specifying whether Redo is possible or not.

- *name*

  A String specifying the repository key.

- *module*

  A SymbolicConstant specifying the module in which the display group has been created. The possible values are PART, ASSEMBLY, PART_ASSEMBLY, ODB, and ALL.

- *modelName*

  A String specifying the name of the model to which the display group belongs when the module is part- or assembly-based.

- *partName*

  A String specifying the name of the part to which the display group belongs when the module is part-based.