============
Optimization
============

Optimization commands are used to perform topology, shape, or sizing optimization of your model given a set of objectives and a set of restrictions.

Create optimization tasks
-------------------------

.. automethod:: abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask

.. automethod:: abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask

.. automethod:: abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask

.. automethod:: abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask

Assign features to optimization tasks
-------------------------------------

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.FrozenArea

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.Growth

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry

.. automethod:: abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl


Object features
---------------

BeadFixedRegion
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.BeadFixedRegion.BeadFixedRegion
    :members:

BeadGrowth
~~~~~~~~~~

.. autoclass:: abaqus.Optimization.BeadGrowth.BeadGrowth
    :members:

BeadPenetrationCheck
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.BeadPenetrationCheck.BeadPenetrationCheck
    :members:

BeadPlanarSymmetry
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.BeadPlanarSymmetry.BeadPlanarSymmetry
    :members:

BeadPointSymmetry
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.BeadPointSymmetry.BeadPointSymmetry
    :members:

BeadRotationalSymmetry
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.BeadRotationalSymmetry.BeadRotationalSymmetry
    :members:

BeadTask
~~~~~~~~

.. autoclass:: abaqus.Optimization.BeadTask.BeadTask
    :members:

CombinedTermDesignResponse
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse
    :members:

DesignDirection
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.DesignDirection.DesignDirection
    :members:

DesignResponse
~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.DesignResponse.DesignResponse
    :members:

DrillControl
~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.DrillControl.DrillControl
    :members:

FixedRegion
~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.FixedRegion.FixedRegion
    :members:

FrozenArea
~~~~~~~~~~

.. autoclass:: abaqus.Optimization.FrozenArea.FrozenArea
    :members:

GeometricRestriction
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.GeometricRestriction.GeometricRestriction
    :members:

Growth
~~~~~~

.. autoclass:: abaqus.Optimization.Growth.Growth
    :members:

LocalStopCondition
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.LocalStopCondition.LocalStopCondition
    :members:

ObjectiveFunction
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.ObjectiveFunction.ObjectiveFunction
    :members:

OptimizationConstraint
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.OptimizationConstraint.OptimizationConstraint
    :members:

OptimizationObjective
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.OptimizationObjective.OptimizationObjective
    :members:

OptimizationObjectiveArray
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.OptimizationObjectiveArray.OptimizationObjectiveArray
    :members:

PenetrationCheck
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.PenetrationCheck.PenetrationCheck
    :members:

ShapeDemoldControl
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl
    :members:

ShapeMemberSize
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.ShapeMemberSize.ShapeMemberSize
    :members:

ShapePlanarSymmetry
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry
    :members:

ShapePointSymmetry
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry
    :members:

ShapeRotationalSymmetry
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry
    :members:

ShapeTask
~~~~~~~~~

.. autoclass:: abaqus.Optimization.ShapeTask.ShapeTask
    :members:

SingleTermDesignResponse
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse
    :members:

SizingClusterAreas
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.SizingClusterAreas.SizingClusterAreas
    :members:

SizingCyclicSymmetry
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry
    :members:

SizingFrozenArea
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.SizingFrozenArea.SizingFrozenArea
    :members:

SizingMemberSize
~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.SizingMemberSize.SizingMemberSize
    :members:

SizingPlanarSymmetry
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry
    :members:

SizingPointSymmetry
~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry
    :members:

SizingRotationalSymmetry
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry
    :members:

SizingTask
~~~~~~~~~~

.. autoclass:: abaqus.Optimization.SizingTask.SizingTask
    :members:

SlideRegionControl
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.SlideRegionControl.SlideRegionControl
    :members:

StampControl
~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.StampControl.StampControl
    :members:

StepOption
~~~~~~~~~~

.. autoclass:: abaqus.Optimization.StepOption.StepOption
    :members:

StepOptionArray
~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.StepOptionArray.StepOptionArray
    :members:

StopCondition
~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.StopCondition.StopCondition
    :members:

TopologyCyclicSymmetry
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry
    :members:

TopologyDemoldControl
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl
    :members:

TopologyMemberSize
~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.TopologyMemberSize.TopologyMemberSize
    :members:

TopologyMillingControl
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.TopologyMillingControl.TopologyMillingControl
    :members:

TopologyOverhangControl
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl
    :members:

TopologyPlanarSymmetry
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry
    :members:

TopologyPointSymmetry
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry
    :members:

TopologyRotationalSymmetry
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry
    :members:

TopologyTask
~~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.TopologyTask.TopologyTask
    :members:

TurnControl
~~~~~~~~~~~

.. autoclass:: abaqus.Optimization.TurnControl.TurnControl
    :members:

