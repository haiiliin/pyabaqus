========
Sketcher
========


A ConstrainedSketch object contains the entities that are used to create a sketch. The objects include ConstrainedSketchGeometry objects contained in the Geometry Repository, such as Line, Arc, and Spline. Vertex, Dimension, Constraint, and Parameter objects are contained in their respective repositories.


Access
------

- `mdb.models[name].sketches[name]`


Create a Constrained Sketch
---------------------------

.. autoclass:: abaqus.Sketcher.SketchModel.SketchModel
    :members:


Features of ConstrainedSketch
-----------------------------

Basic features ConstrainedSketch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Sketcher.ConstrainedSketchBase.ConstrainedSketchBase
    :members:


Constraint of ConstrainedSketch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel
    :members:


Dimension of ConstrainedSketch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel
    :members:


Geometry of ConstrainedSketch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel
    :members:


Parameter of ConstrainedSketch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel
    :members:


Vertex of ConstrainedSketch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel
    :members:


ConstrainedSketch class
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Sketcher.ConstrainedSketch.ConstrainedSketch
    :members:
