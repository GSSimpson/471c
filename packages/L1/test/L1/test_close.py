from L0 import syntax as L0
from L1 import syntax as L1
from L1.close import close_statement


def test_close_statement_copy():
    statement = L1.Copy(destination="t0", source="t1", then=L1.Halt(value="t2"))
    actual = close_statement(statement)
    expected = L0.Copy(destination="t0", source="t1", then=L0.Halt(value="t2"))
    assert expected == actual


def test_close_statement_abstract():
    # fresh = SequentialNameGenerator()
    statement = L1.Abstract(
        destination="t0",
        parameters=["t1", "t2"],
        body=L1.Immediate(destination="t1", value=2, then=L1.Halt(value="t2")),
        then=L1.Halt(value="t3"),
    )
    env = ["t1", "t2"]
    actual = close_statement(statement)

    expected = L0.Procedure(
        name="t0", parameters=env, body=L0.Immediate(destination="t1", value=2, then=L0.Halt(value="t2"))
    )

    # process: 1 produce a procedure from the abstract, 2 save the parameters in an environment variable, 3 maintain contunuity for instructions

    assert actual == expected


def test_close_statement_apply():
    statement = L1.Apply(target="t0", arguments=["t1", "t2"])
    expected = close_statement(statement)
    actual = _
    assert expected == actual


def test_close_statement_immediate():
    statement = L1.Immediate(destination="t0", value=1, then=L1.Halt(value="t1"))
    actual = close_statement(statement)
    expected = L0.Immediate(destination="t0", value=1, then=L0.Halt(value="t1"))
    assert expected == actual


def test_close_statement_primitive():
    statement = L1.Primitive(destination="t0", operator="+", left="t1", right="t2", then=L1.Halt(value="t3"))
    actual = close_statement(statement)
    expected = L0.Primitive(destination="t0", operator="+", left="t1", right="t2", then=L0.Halt(value="t3"))
    assert expected == actual


def test_close_statement_branch():
    statement = L1.Branch(operator="<", left="t0", right="t1", then=L1.Halt(value="t2"), otherwise=L1.Halt(value="t3"))
    actual = close_statement(statement)
    expected = L0.Branch(operator="<", left="t0", right="t1", then=L0.Halt(value="t2"), otherwise=L0.Halt(value="t3"))
    assert expected == actual


def test_close_statement_allocate():
    statement = L1.Allocate(destination="t0", count=1, then=L1.Halt(value="t1"))
    actual = close_statement(statement)
    expected = L0.Allocate(destination="t0", count=1, then=L0.Halt(value="t1"))
    assert expected == actual


def test_close_statement_load():
    statement = L1.Load(destination="t0", base="t1", index=1, then=L1.Halt(value="t2"))
    actual = close_statement(statement)
    expected = L0.Load(destination="t0", base="t1", index=1, then=L0.Halt(value="t2"))
    assert expected == actual


def test_close_statement_store():
    statement = L1.Store(base="t0", index=1, value="t1", then=L1.Halt(value="t2"))
    actual = close_statement(statement)
    expected = L0.Store(base="t0", index=1, value="t1", then=L0.Halt(value="t2"))
    assert expected == actual


def test_close_statement_halt():
    statement = L1.Halt(value="t0")
    actual = close_statement(statement)
    expected = L0.Halt(value="t0")
    assert expected == actual


def test_close_statements():
    pass


def test_close_program():
    pass
