from L2 import syntax as L2
from L3 import syntax as L3
from L3.eliminate_letrec import Context, eliminate_letrec_program, eliminate_letrec_term


<<<<<<< HEAD
# Let
def test_check_term_let():
=======
def test_eliminate_letrec_term_let():
>>>>>>> upstream/main
    term = L3.Let(
        bindings=[("x", L3.Reference(name="x"))],
        body=L3.Reference(name="y"),
    )

    context: Context = {}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Let(
        bindings=[("x", L2.Reference(name="x"))],
        body=L2.Reference(name="y"),
    )

    assert actual == expected


def test_eliminate_letrec_term_letrec():
    term = L3.LetRec(
        bindings=[("x", L3.Reference(name="y"))],
        body=L3.Reference(name="z"),
    )

    context: Context = {}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Let(
        bindings=[("x", L2.Allocate(count=1))],
        body=L2.Begin(
            effects=[
                L2.Store(
                    base=L2.Reference(name="x"),
                    index=0,
                    value=L2.Reference(name="y"),
                )
            ],
            value=L2.Reference(name="z"),
        ),
    )

    assert actual == expected


def test_eliminate_letrec_term_reference_value():
    term = L3.Reference(name="x")

    context: Context = {}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Reference(name="x")

    assert actual == expected


def test_eliminate_letrec_term_reference_variable():
    term = L3.Reference(name="x")

    context: Context = {"x": None}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Load(base=L2.Reference(name="x"), index=0)

    assert actual == expected


def test_eliminate_letrec_term_abstract():
    term = L3.Abstract(
        parameters=["x"],
        body=L3.Reference(name="x"),
    )

    context: Context = {}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Abstract(
        parameters=["x"],
        body=L2.Reference(name="x"),
    )

<<<<<<< HEAD
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


# LetRec
def test_check_term_Letrec_nonrecursive():
    term = L3.LetRec(
        bindings=[
            ("x", L3.Immediate(value=0)),
        ],
        body=L3.Reference(name="x"),
    )
    context: Context = {}
    expected = L2.Let(bindings=[("x", L2.Immediate(value=0))], body=L2.Reference(name="x"))
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


@pytest.mark.skip
def test_check_term_Letrec_recursive():
    #    term = L3.LetRec(
    #    bindings=[
    #        ("x", L3.Immediate(value=0)),
    #    ],
    #    body=L3.Reference(name="x"),
    # )
    # context : Context = {}
    pass


# Reference
def test_check_reference_nonrecursive():
    term = L3.Reference(name="x")
    context: Context = {"x", None}
    expected = L2.Reference(name="x")
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


def test_check_reference():
    term = L3.Reference(name="x")
    context: Context = {}
    expected = L2.Load(base=L3.Reference(name="x"), index=0)
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


# Abstract
def test_check_term_abstract():
    term = L3.Abstract(parameters=[], body=L3.Reference(name="x"))
    context: Context = {}

    expected = L2.Abstract(parameters=[], body=L2.Reference(name="x"))
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


# Apply
def test_check_term_apply():
    term = L3.Apply(target=L3.Reference(name="x"), arguments=[])
    context: Context = {}

    expected = L2.Apply(target=L2.Reference(name="x"), arguments=[])
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


# Immediate
def test_check_term_immediate():
    term = L3.Immediate(value=1)
    context: Context = {}
    expected = L2.Immediate(value=1)
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


# primitive
def test_check_term_primitive():
    term = L3.Primitive(operator="+", left=L3.Immediate(value=1), right=L3.Immediate(value=2))
    context: Context = {}
    expected = L2.Primitive(operator="+", left=L2.Immediate(value=1), right=L2.Immediate(value=2))
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


# branch
def test_check_term_branch():
    term = L3.Branch(
        operator="<",
        left=L3.Immediate(value=1),
        right=L3.Immediate(value=2),
        consequent=L3.Reference(name="x"),
        otherwise=L3.Reference(name="y"),
    )
    context: Context = {}
    expected = L2.Branch(
        operator="<",
        left=L2.Immediate(value=1),
        right=L2.Immediate(value=2),
        consequent=L2.Reference(name="x"),
        otherwise=L2.Reference(name="y"),
    )
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


# allocate
def test_check_term_allocate():
    term = L3.Allocate(count=1)
    context: Context = {}
    expected = L2.Allocate(count=1)
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


# load
def test_check_term_load():
    term = L3.Load(base=L3.Reference(name="x"), index=1)
    context: Context = {}
    expected = L2.Load(base=L2.Reference(name="x"), index=1)
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


# store
def test_check_term_store():
    term = L3.Store(base=L3.Reference(name="x"), index=1, value=L3.Immediate(value=1))
    context: Context = {}
    expected = L2.Store(base=L2.Reference(name="x"), index=1, value=L2.Immediate(value=1))
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


# begin
def test_check_term_begin():
    term = L3.Begin(effects=[], value=L3.Reference(name="x"))
    context: Context = {}
    expected = L2.Begin(effects=[], value=L2.Reference(name="x"))
    actual = eliminate_letrec_term(term, context)
    assert actual == expected


# Program
def test_eliminate_letrec_program():
    program = L3.Program(
        parameters=[],
        body=L3.Immediate(value=0),
=======
    assert actual == expected


def test_eliminate_letrec_term_apply():
    term = L3.Apply(
        target=L3.Reference(name="x"),
        arguments=[],
>>>>>>> upstream/main
    )

    context: Context = {}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Apply(
        target=L2.Reference(name="x"),
        arguments=[],
    )

    assert actual == expected


def test_eliminate_letrec_term_immediate():
    term = L3.Immediate(value=0)

    context: Context = {}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Immediate(value=0)

    assert actual == expected


def test_eliminate_letrec_term_primitive():
    term = L3.Primitive(
        operator="+",
        left=L3.Reference(name="x"),
        right=L3.Reference(name="y"),
    )

    context: Context = {}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Primitive(
        operator="+",
        left=L2.Reference(name="x"),
        right=L2.Reference(name="y"),
    )

    assert actual == expected


def test_eliminate_letrec_term_branch():
    term = L3.Branch(
        operator="<",
        left=L3.Reference(name="w"),
        right=L3.Reference(name="x"),
        consequent=L3.Reference(name="y"),
        otherwise=L3.Reference(name="z"),
    )

    context: Context = {}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Branch(
        operator="<",
        left=L2.Reference(name="w"),
        right=L2.Reference(name="x"),
        consequent=L2.Reference(name="y"),
        otherwise=L2.Reference(name="z"),
    )

    assert actual == expected


def test_eliminate_letrec_term_allocate():
    term = L3.Allocate(count=3)

    context: Context = {}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Allocate(count=3)

    assert actual == expected


def test_eliminate_letrec_term_load():
    term = L3.Load(
        base=L3.Reference(name="x"),
        index=0,
    )

    context: Context = {}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Load(
        base=L2.Reference(name="x"),
        index=0,
    )

    assert actual == expected


def test_eliminate_letrec_term_store():
    term = L3.Store(
        base=L3.Reference(name="x"),
        index=0,
        value=L3.Reference(name="y"),
    )

    context: Context = {}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Store(
        base=L2.Reference(name="x"),
        index=0,
        value=L2.Reference(name="y"),
    )

    assert actual == expected


def test_eliminate_letrec_term_begin():
    term = L3.Begin(
        effects=[],
        value=L3.Reference(name="x"),
    )

    context: Context = {}
    actual = eliminate_letrec_term(term, context)

    expected = L2.Begin(
        effects=[],
        value=L2.Reference(name="x"),
    )

    assert actual == expected


def test_eliminate_letrec_program():
    program = L3.Program(
        parameters=["x"],
        body=L3.Reference(name="x"),
    )

    actual = eliminate_letrec_program(program)

    expected = L2.Program(
        parameters=["x"],
        body=L2.Reference(name="x"),
    )

    assert actual == expected
