import numpy as np
from pydrake.common.containers import namedview
from pydrake.common.value import Value
from pydrake.math import RigidTransform, RotationMatrix
from pydrake.systems.analysis import Simulator
from pydrake.systems.framework import BasicVector, LeafSystem
from pydrake.trajectories import PiecewisePolynomial

class MyAdder(LeafSystem):
    def __init__(self):
        super().__init__()  # Don't forget to initialize the base class.
        self._a_port = self.DeclareVectorInputPort(name="a", size=2)
        self._b_port = self.DeclareVectorInputPort(name="b", size=2)
        self.DeclareVectorOutputPort(name="sum", size=2, calc=self.CalcSum)
        self.DeclareVectorOutputPort(name="difference",
                                     size=2,
                                     calc=self.CalcDifference)

    def CalcSum(self, context, output):
        # Evaluate the input ports to obtain the 2x1 vectors.
        a = self._a_port.Eval(context)
        b = self._b_port.Eval(context)

        # Write the sum into the output vector.
        output.SetFromVector(a + b)

    def CalcDifference(self, context, output):
        # Evaluate the input ports to obtain the 2x1 vectors.
        a = self._a_port.Eval(context)
        b = self._b_port.Eval(context)

        # Write the difference into output vector.
        output.SetFromVector(a - b)

# Construct an instance of this system and a context.
system = MyAdder()
context = system.CreateDefaultContext()

# Fix the input ports to some constant values.
system.GetInputPort("a").FixValue(context, [3, 4])
system.GetInputPort("b").FixValue(context, [1, 2])

# Evaluate the output ports.
print(f"sum: {system.GetOutputPort('sum').Eval(context)}")
print(f"difference: {system.GetOutputPort('difference').Eval(context)}")
