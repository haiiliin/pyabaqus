==================
Load and Load Case
==================

A specific type of load object and a specific type of load state object are designed for each type of load. A load object stores the nonpropagating data of a load as well as a number of instances of the corresponding load state object, each of which stores the propagating data of the load in a single step. Instances of the load state object are created and deleted internally by its corresponding load object.

Load Case commands are used for configuring load cases in specific types of steps that may use them.

Load
----

The Load object is the abstract base type for other Load objects. The Load object has no explicit constructor. The methods and members of the Load object are common to all objects derived from Load.


Create loads
~~~~~~~~~~~~

.. autoclass:: abaqus.LoadAndLoadCase.LoadModel.LoadModel
    :members:


Object features of loads
~~~~~~~~~~~~~~~~~~~~~~~~

Load
****

.. autoclass:: abaqus.LoadAndLoadCase.Load.Load
    :members:

LoadState
*********

.. autoclass:: abaqus.LoadAndLoadCase.LoadState.LoadState
    :members:

BodyCharge
**********

.. autoclass:: abaqus.LoadAndLoadCase.BodyCharge.BodyCharge
    :members:

BodyChargeState
***************

.. autoclass:: abaqus.LoadAndLoadCase.BodyChargeState.BodyChargeState
    :members:

BodyConcentrationFlux
*********************

.. autoclass:: abaqus.LoadAndLoadCase.BodyConcentrationFlux.BodyConcentrationFlux
    :members:

BodyConcentrationFluxState
**************************

.. autoclass:: abaqus.LoadAndLoadCase.BodyConcentrationFluxState.BodyConcentrationFluxState
    :members:

BodyCurrent
***********

.. autoclass:: abaqus.LoadAndLoadCase.BodyCurrent.BodyCurrent
    :members:

BodyCurrentDensity
******************

.. autoclass:: abaqus.LoadAndLoadCase.BodyCurrentDensity.BodyCurrentDensity
    :members:

BodyCurrentState
****************

.. autoclass:: abaqus.LoadAndLoadCase.BodyCurrentState.BodyCurrentState
    :members:

BodyForce
*********

.. autoclass:: abaqus.LoadAndLoadCase.BodyForce.BodyForce
    :members:

BodyForceState
**************

.. autoclass:: abaqus.LoadAndLoadCase.BodyForceState.BodyForceState
    :members:

BodyHeatFlux
************

.. autoclass:: abaqus.LoadAndLoadCase.BodyHeatFlux.BodyHeatFlux
    :members:

BodyHeatFluxState
*****************

.. autoclass:: abaqus.LoadAndLoadCase.BodyHeatFluxState.BodyHeatFluxState
    :members:

BoltLoad
********

.. autoclass:: abaqus.LoadAndLoadCase.BoltLoad.BoltLoad
    :members:

BoltLoadState
*************

.. autoclass:: abaqus.LoadAndLoadCase.BoltLoadState.BoltLoadState
    :members:

ConcCharge
**********

.. autoclass:: abaqus.LoadAndLoadCase.ConcCharge.ConcCharge
    :members:

ConcConcFlux
************

.. autoclass:: abaqus.LoadAndLoadCase.ConcConcFlux.ConcConcFlux
    :members:

ConcCurrent
***********

.. autoclass:: abaqus.LoadAndLoadCase.ConcCurrent.ConcCurrent
    :members:

ConcCurrentState
****************

.. autoclass:: abaqus.LoadAndLoadCase.ConcCurrentState.ConcCurrentState
    :members:

ConcentratedChargeState
***********************

.. autoclass:: abaqus.LoadAndLoadCase.ConcentratedChargeState.ConcentratedChargeState
    :members:

ConcentratedConcentrationFluxState
**********************************

.. autoclass:: abaqus.LoadAndLoadCase.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState
    :members:

ConcentratedForce
*****************

.. autoclass:: abaqus.LoadAndLoadCase.ConcentratedForce.ConcentratedForce
    :members:

ConcentratedForceState
**********************

.. autoclass:: abaqus.LoadAndLoadCase.ConcentratedForceState.ConcentratedForceState
    :members:

ConcentratedHeatFlux
********************

.. autoclass:: abaqus.LoadAndLoadCase.ConcentratedHeatFlux.ConcentratedHeatFlux
    :members:

ConcentratedHeatFluxState
*************************

.. autoclass:: abaqus.LoadAndLoadCase.ConcentratedHeatFluxState.ConcentratedHeatFluxState
    :members:

ConcentratedPoreFluidState
**************************

.. autoclass:: abaqus.LoadAndLoadCase.ConcentratedPoreFluidState.ConcentratedPoreFluidState
    :members:

ConcPoreFluid
*************

.. autoclass:: abaqus.LoadAndLoadCase.ConcPoreFluid.ConcPoreFluid
    :members:

ConnectorForce
**************

.. autoclass:: abaqus.LoadAndLoadCase.ConnectorForce.ConnectorForce
    :members:

ConnectorForceState
*******************

.. autoclass:: abaqus.LoadAndLoadCase.ConnectorForceState.ConnectorForceState
    :members:

ConnectorMoment
***************

.. autoclass:: abaqus.LoadAndLoadCase.ConnectorMoment.ConnectorMoment
    :members:

ConnectorMomentState
********************

.. autoclass:: abaqus.LoadAndLoadCase.ConnectorMomentState.ConnectorMomentState
    :members:

CoriolisForce
*************

.. autoclass:: abaqus.LoadAndLoadCase.CoriolisForce.CoriolisForce
    :members:

CoriolisForceState
******************

.. autoclass:: abaqus.LoadAndLoadCase.CoriolisForceState.CoriolisForceState
    :members:

Gravity
*******

.. autoclass:: abaqus.LoadAndLoadCase.Gravity.Gravity
    :members:

GravityState
************

.. autoclass:: abaqus.LoadAndLoadCase.GravityState.GravityState
    :members:

HydrostaticFluidFlowState
*************************

.. autoclass:: abaqus.LoadAndLoadCase.HydrostaticFluidFlowState.HydrostaticFluidFlowState
    :members:

InertiaRelief
*************

.. autoclass:: abaqus.LoadAndLoadCase.InertiaRelief.InertiaRelief
    :members:

InertiaReliefState
******************

.. autoclass:: abaqus.LoadAndLoadCase.InertiaReliefState.InertiaReliefState
    :members:

InwardVolAccel
**************

.. autoclass:: abaqus.LoadAndLoadCase.InwardVolAccel.InwardVolAccel
    :members:

InwardVolAccelState
*******************

.. autoclass:: abaqus.LoadAndLoadCase.InwardVolAccelState.InwardVolAccelState
    :members:

LineLoad
********

.. autoclass:: abaqus.LoadAndLoadCase.LineLoad.LineLoad
    :members:

LineLoadState
*************

.. autoclass:: abaqus.LoadAndLoadCase.LineLoadState.LineLoadState
    :members:

LoadStep
********

.. autoclass:: abaqus.LoadAndLoadCase.LoadStep.LoadStep
    :members:

Moment
******

.. autoclass:: abaqus.LoadAndLoadCase.Moment.Moment
    :members:

MomentState
***********

.. autoclass:: abaqus.LoadAndLoadCase.MomentState.MomentState
    :members:

PEGLoad
*******

.. autoclass:: abaqus.LoadAndLoadCase.PEGLoad.PEGLoad
    :members:

PEGLoadState
************

.. autoclass:: abaqus.LoadAndLoadCase.PEGLoadState.PEGLoadState
    :members:

PipePressure
************

.. autoclass:: abaqus.LoadAndLoadCase.PipePressure.PipePressure
    :members:

PipePressureState
*****************

.. autoclass:: abaqus.LoadAndLoadCase.PipePressureState.PipePressureState
    :members:

Pressure
********

.. autoclass:: abaqus.LoadAndLoadCase.Pressure.Pressure
    :members:

PressureState
*************

.. autoclass:: abaqus.LoadAndLoadCase.PressureState.PressureState
    :members:

RotationalBodyForce
*******************

.. autoclass:: abaqus.LoadAndLoadCase.RotationalBodyForce.RotationalBodyForce
    :members:

RotationalBodyForceState
************************

.. autoclass:: abaqus.LoadAndLoadCase.RotationalBodyForceState.RotationalBodyForceState
    :members:

ShellEdgeLoad
*************

.. autoclass:: abaqus.LoadAndLoadCase.ShellEdgeLoad.ShellEdgeLoad
    :members:

ShellEdgeLoadState
******************

.. autoclass:: abaqus.LoadAndLoadCase.ShellEdgeLoadState.ShellEdgeLoadState
    :members:

SubmodelSB
**********

.. autoclass:: abaqus.LoadAndLoadCase.SubmodelSB.SubmodelSB
    :members:

SubmodelSBState
***************

.. autoclass:: abaqus.LoadAndLoadCase.SubmodelSBState.SubmodelSBState
    :members:

SubstructureLoad
****************

.. autoclass:: abaqus.LoadAndLoadCase.SubstructureLoad.SubstructureLoad
    :members:

SubstructureLoadState
*********************

.. autoclass:: abaqus.LoadAndLoadCase.SubstructureLoadState.SubstructureLoadState
    :members:

SurfaceCharge
*************

.. autoclass:: abaqus.LoadAndLoadCase.SurfaceCharge.SurfaceCharge
    :members:

SurfaceChargeState
******************

.. autoclass:: abaqus.LoadAndLoadCase.SurfaceChargeState.SurfaceChargeState
    :members:

SurfaceConcentrationFlux
************************

.. autoclass:: abaqus.LoadAndLoadCase.SurfaceConcentrationFlux.SurfaceConcentrationFlux
    :members:

SurfaceConcentrationFluxState
*****************************

.. autoclass:: abaqus.LoadAndLoadCase.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState
    :members:

SurfaceCurrent
**************

.. autoclass:: abaqus.LoadAndLoadCase.SurfaceCurrent.SurfaceCurrent
    :members:

SurfaceCurrentDensity
*********************

.. autoclass:: abaqus.LoadAndLoadCase.SurfaceCurrentDensity.SurfaceCurrentDensity
    :members:

SurfaceCurrentState
*******************

.. autoclass:: abaqus.LoadAndLoadCase.SurfaceCurrentState.SurfaceCurrentState
    :members:

SurfaceHeatFlux
***************

.. autoclass:: abaqus.LoadAndLoadCase.SurfaceHeatFlux.SurfaceHeatFlux
    :members:

SurfaceHeatFluxState
********************

.. autoclass:: abaqus.LoadAndLoadCase.SurfaceHeatFluxState.SurfaceHeatFluxState
    :members:

SurfacePoreFluid
****************

.. autoclass:: abaqus.LoadAndLoadCase.SurfacePoreFluid.SurfacePoreFluid
    :members:

SurfacePoreFluidState
*********************

.. autoclass:: abaqus.LoadAndLoadCase.SurfacePoreFluidState.SurfacePoreFluidState
    :members:

SurfaceTraction
***************

.. autoclass:: abaqus.LoadAndLoadCase.SurfaceTraction.SurfaceTraction
    :members:

SurfaceTractionState
********************

.. autoclass:: abaqus.LoadAndLoadCase.SurfaceTractionState.SurfaceTractionState
    :members:


Load case
---------

The LoadCase object is used to define the loads and constraints comprising a particular loading condition and the linear response of a structure subjected to that loading condition.


Create load cases
~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.LoadAndLoadCase.LoadStep.LoadStep
    :members:


Object features of load cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.LoadAndLoadCase.LoadCase.LoadCase
    :members: