import pytest
from L3.check import Context, check_program, check_term
from L3.syntax import (
    Abstract,
    Allocate,
    Apply,
    Begin,
    Branch,
    Immediate,
    Let,
    LetRec,
    Load,
    Primitive,
    Program,
    Reference,
    Store,
)


# Program
def test_check_program():
    program = Program(parameters=["param1", "param2"], body=Immediate(value=0))
    check_program(program)


def test_check_program_duplicate_params():
    program = Program(parameters=["param1", "param1"], body=Immediate(value=0))
    with pytest.raises(ValueError):
        check_program(program)


# Let
def test_check_let():
    term = Let(bindings=[("term", Immediate(value=1))], body=Reference(name="term2"))
    context: Context = {"term2": None}
    check_term(term, context)


def test_check_let_duplicate_bindings():
    term = Let(bindings=[("term", Immediate(value=1)), ("term", Immediate(value=1))], body=Reference(name="term2"))
    context: Context = {"term2": None}
    with pytest.raises(ValueError):
        check_term(term, context)


def test_check_let_scope():
    term = Let(
        bindings=[
            ("x", Immediate(value=0)),
            ("y", Reference(name="x")),
        ],
        body=Reference(name="y"),
    )
    context: Context = {}
    with pytest.raises(ValueError):
        check_term(term, context)


# LetRec
def test_check_letrec():
    term = LetRec(bindings=[("term", Immediate(value=1))], body=Reference(name="term"))
    context: Context = {"term": None}
    check_term(term, context)


def test_check_letrec_duplicate_bindings():
    term = LetRec(bindings=[("term", Immediate(value=1)), ("term", Immediate(value=1))], body=Reference(name="term"))
    context: Context = {"term": None}
    with pytest.raises(ValueError):
        check_term(term, context)


def test_check_letrec_scope():
    term = Let(
        bindings=[
            ("x", Immediate(value=0)),
            ("y", Reference(name="x")),
        ],
        body=Reference(name="y"),
    )
    context: Context = {}
    with pytest.raises(ValueError):
        check_term(term, context)


# Reference
def test_check_reference():
    term = Reference(name="name")
    context: Context = {"name": None}
    check_term(term, context)


def test_check_reference_no_binding():
    term = Reference(name="name")
    context: Context = {}

    with pytest.raises(ValueError):
        check_term(term, context)


# Abstract
def test_check_abstract():
    term = Abstract(parameters=["a", "b"], body=Reference(name="x"))
    context: Context = {"x": None}
    check_term(term, context)


def test_check_abstract_duplicates():
    term = Abstract(parameters=["a", "a"], body=Reference(name="x"))
    context: Context = {"x": None}

    with pytest.raises(ValueError):
        check_term(term, context)


# Apply
def test_check_apply_empty_args():
    term = Apply(target=Reference(name="target"), arguments=[])
    context: Context = {"target": None}
    check_term(term, context)


def test_check_apply_one_arg():
    term = Apply(target=Immediate(value=1), arguments=[])

    context: Context = {}
    check_term(term, context)


# Immediate
def test_check_immediate():
    term = Immediate(value=0)
    context: Context = {}
    check_term(term, context)


# Primitive
def test_check_primitive_add():
    term = Primitive(operator="+", left=Immediate(value=0), right=Immediate(value=1))
    context: Context = {}
    check_term(term, context)


# Branch
def test_check_branch_LT():
    term = Branch(
        operator="<",
        left=Immediate(value=0),
        right=Immediate(value=1),
        consequent=Immediate(value=3),
        otherwise=Immediate(value=4),
    )

    context: Context = {}
    check_term(term, context)


# Allocate
def test_check_allocate():
    term = Allocate(count=0)
    context: Context = {}
    check_term(term, context)


# Load
def test_check_load():
    term = Load(base=Immediate(value=0), index=0)
    context: Context = {}
    check_term(term, context)


# Store
def test_check_store():
    term = Store(base=Immediate(value=0), index=0, value=Immediate(value=1))
    context: Context = {}
    check_term(term, context)


# Begin
def test_check_begin():
    term = Begin(effects=[Immediate(value=0)], value=Immediate(value=1))
    context: Context = {}
    check_term(term, context)
