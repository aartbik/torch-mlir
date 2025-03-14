# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Also available under a BSD-style license. See LICENSE.

import torch

from torch_mlir_e2e_test.framework import TestUtils
from torch_mlir_e2e_test.registry import register_test_case
from torch_mlir_e2e_test.annotations import annotate_args, export

# ==============================================================================


class TypeConversionF32ToF64Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.float32, True)])
    def forward(self, x):
        return x.to(torch.float64)


@register_test_case(module_factory=lambda: TypeConversionF32ToF64Module())
def TypeConversionF32ToF64Module_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5))


class TypeConversionF64ToF32Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.float64, True)])
    def forward(self, x):
        return x.to(torch.float32)


@register_test_case(module_factory=lambda: TypeConversionF64ToF32Module())
def TypeConversionF64ToF32Module_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5).type(torch.float64))


class TypeConversionI32ToI64Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.int32, True)])
    def forward(self, x):
        return x.to(torch.int64)


@register_test_case(module_factory=lambda: TypeConversionI32ToI64Module())
def TypeConversionI32ToI64Module_basic(module, tu: TestUtils):
    module.forward(tu.randint(2, 3, high=5).type(torch.int32))


class TypeConversionI64ToI32Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.int64, True)])
    def forward(self, x):
        return x.to(torch.int32)


@register_test_case(module_factory=lambda: TypeConversionI64ToI32Module())
def TypeConversionI64ToI32Module_basic(module, tu: TestUtils):
    module.forward(tu.randint(2, 3, high=5))


class TypeConversionI1ToI32Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.bool, True)])
    def forward(self, x):
        return x.to(torch.int32)


@register_test_case(module_factory=lambda: TypeConversionI1ToI32Module())
def TypeConversionI1ToI32Module_basic(module, tu: TestUtils):
    tensor = tu.randint(3, 4, low=0, high=2).to(torch.bool)
    module.forward(tensor)


class TypeConversionI1ToI64Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.bool, True)])
    def forward(self, x):
        return x.to(torch.int64)


@register_test_case(module_factory=lambda: TypeConversionI1ToI64Module())
def TypeConversionI1ToI64Module_basic(module, tu: TestUtils):
    tensor = tu.randint(3, 4, low=0, high=2).to(torch.bool)
    module.forward(tensor)


class TypeConversionI1ToF32Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.bool, True)])
    def forward(self, x):
        return x.to(torch.float32)


@register_test_case(module_factory=lambda: TypeConversionI1ToF32Module())
def TypeConversionI1ToF32Module_basic(module, tu: TestUtils):
    tensor = tu.randint(3, 4, low=0, high=2).to(torch.bool)
    module.forward(tensor)


class TypeConversionI1ToF64Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.bool, True)])
    def forward(self, x):
        return x.to(torch.float64)


@register_test_case(module_factory=lambda: TypeConversionI1ToF64Module())
def TypeConversionI1ToF64Module_basic(module, tu: TestUtils):
    tensor = tu.randint(3, 4, low=0, high=2).to(torch.bool)
    module.forward(tensor)


class TypeConversionUint8ToF32Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([3], torch.uint8, True),
        ]
    )
    def forward(self, x):
        return x.to(torch.float)


@register_test_case(module_factory=lambda: TypeConversionUint8ToF32Module())
def TypeConversionUint8ToF32Module_basic(module, tu: TestUtils):
    module.forward(torch.tensor([0, 1, 255]).to(torch.uint8))


# ==============================================================================


class ToDtypeLayoutNoneModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.float32, True)])
    def forward(self, x):
        return torch.ops.aten.to(
            x,
            dtype=torch.float64,
            layout=None,
            device=None,
            pin_memory=None,
            non_blocking=False,
            copy=False,
            memory_format=None,
        )


@register_test_case(module_factory=lambda: ToDtypeLayoutNoneModule())
def ToDtypeLayoutNoneModule_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5))


class ToDtypeLayoutCPUModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.float32, True)])
    def forward(self, x):
        return torch.ops.aten.to(
            x,
            dtype=torch.float64,
            layout=None,
            device="cpu",
            pin_memory=None,
            non_blocking=False,
            copy=False,
            memory_format=None,
        )


@register_test_case(module_factory=lambda: ToDtypeLayoutCPUModule())
def ToDtypeLayoutCPUModule_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5))


class ToDtypeLayoutStridedModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.float32, True)])
    def forward(self, x):
        return torch.ops.aten.to(
            x,
            dtype=torch.float64,
            layout=torch.strided,
            device=None,
            pin_memory=None,
            non_blocking=False,
            copy=False,
            memory_format=None,
        )


@register_test_case(module_factory=lambda: ToDtypeLayoutStridedModule())
def ToDtypeLayoutStridedModule_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5))


class ToDtypeBoolLayoutNoneStaticModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([3, 5], torch.int64, True)])
    def forward(self, x):
        return torch.ops.aten.to(
            x,
            dtype=torch.bool,
            layout=None,
            device=None,
            pin_memory=None,
            non_blocking=False,
            copy=False,
            memory_format=None,
        )


@register_test_case(module_factory=lambda: ToDtypeBoolLayoutNoneStaticModule())
def ToDtypeBoolLayoutNoneStaticModule_basic(module, tu: TestUtils):
    module.forward(tu.randint(3, 5))


class ToDtypeFloatFromIntModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.int64, True)])
    def forward(self, x):
        return torch.ops.aten.to(
            x,
            dtype=torch.float32,
        )


@register_test_case(module_factory=lambda: ToDtypeFloatFromIntModule())
def ToDtypeFloatFromIntModule_basic(module, tu: TestUtils):
    input = torch.randint(low=-5, high=5, size=(2, 2)).to(torch.int64)
    module.forward(input)


class ToDtypeIntFromFloatModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.float64, True)])
    def forward(self, x):
        return torch.ops.aten.to(
            x,
            dtype=torch.int64,
        )


@register_test_case(module_factory=lambda: ToDtypeIntFromFloatModule())
def ToDtypeIntFromFloatModule_basic(module, tu: TestUtils):
    input = tu.rand(2, 2, low=-5, high=5)
    input[1][1] = tu.randint(1, 1) + 0.7
    module.forward(input)


class TypeAsSameModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.float32, True),
            ([-1, -1], torch.float32, True),
        ]
    )
    def forward(self, x, y):
        return torch.ops.aten.type_as(x, y)


@register_test_case(module_factory=lambda: TypeAsSameModule())
def TypeAsSameModule_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5), tu.rand(3, 5))


class TypeAsDifferentModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args(
        [
            None,
            ([-1, -1], torch.int, True),
            ([-1, -1], torch.int64, True),
        ]
    )
    def forward(self, x, y):
        return torch.ops.aten.type_as(x, y)


@register_test_case(module_factory=lambda: TypeAsDifferentModule())
def TypeAsDifferentModule_basic(module, tu: TestUtils):
    module.forward(
        tu.randint(3, 5, low=0, high=10, dtype=torch.int),
        tu.randint(3, 5, low=0, high=10, dtype=torch.int64),
    )


# ==============================================================================


class PrimsConvertElementTypeModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([None, ([-1, -1], torch.float32, True)])
    def forward(self, x):
        return torch.ops.prims.convert_element_type(x, dtype=torch.int64)


@register_test_case(module_factory=lambda: PrimsConvertElementTypeModule())
def PrimsConvertElementTypeModule_basic(module, tu: TestUtils):
    module.forward(tu.rand(3, 5))
