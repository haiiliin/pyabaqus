# Highlight commands

The Highlight commands are used to highlight objects in the current viewport and to remove the highlighting.

## highlight



This method highlights an object in the current viewport.



### Path

highlight

### Required arguments

- *object*

An object specifying the object in the current viewport to be highlighted. You can specify only a single object. Abaqus/CAE highlights only the edges of a face when highlighting a surface and a face together. The following objects are supported:

**For the MDB**

- Vertex
- Edge
- Face
- Surface
- Cell
- Node
- Element
- Element face
- Element edge
- Feature
- Datum
- Instance
- Set
- Load
- Boundary condition
- Predefined field
- Display group

**For the ODB**

- Node
- Element
- Display group



## unhighlight



This method removes highlighting from an object in the current viewport.



### Path

unhighlight

### Required arguments

- *object*

  An object specifying the object in the current viewport from which the highlighting will be removed. You can specify only a single object. See [highlight](https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-canvascommands.htm?ContextScope=all#simaker-objcanvascommandshighlightpyc) for a list of supported objects.