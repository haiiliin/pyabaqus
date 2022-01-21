====
Step
====

The Step object stores the parameters that determine the context of the step. The Step object is the abstract base type for other Step objects. The Step object has no explicit constructor. The methods and members of the Step object are common to all objects derived from the Step.


Access
------

- `mdb.models[name].steps[name]`


Create a step
-------------

.. autoclass:: abaqus.Step.StepModel.StepModel
    :members:

Features of the Step
--------------------


Basic features of the Step
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Step.StepBase.StepBase
    :members:


ALE features of the Step
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Adaptivity.AdaptivityStep.AdaptivityStep
    :members:


Output features of the Step
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.StepOutput.OutputStep.OutputStep
    :members:


Table Collection features of the Step
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.TableCollection.TableCollectionStep.TableCollectionStep
    :members:
