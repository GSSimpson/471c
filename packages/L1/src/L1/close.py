from collections.abc import Callable, Sequence
from functools import partial

from L0 import syntax as L0

from L1 import syntax as L1


#supporting things:
# - get rid of identifiers
    # - maintain an environment of identifiers that are in scope, and replace them with their values










def close_statement(
    statement: L1.Statement,
    #fresh: Callable[[str], str],
) -> L0.Statement
    _statement = partial(close_statement) #, fresh=fresh)
    _statements = partial(close_statements)#, fresh=fresh)

    match statement:
        case L1.Copy(destination=destination, source=source, then=then):
            return L0.Copy(
                destination=destination,
                source=source,
                then=_statement(then),
            )

        case L1.Abstract(destination=destination, parameters=parameters, body=body, then=then):
            # process: 1 produce a procedure from the abstract, 2 save the parameters in an environment variable, 3 maintain contunuity for instructions
            env = parameters
            
            
            
            
            
            return _statement(then)







            #return L0.Procedure(name="", parameters=[], body = L0.Halt(value=""))

        case L1.Apply(target=target, arguments=arguments):
            return L0.Halt(value=...)

        case L1.Immediate(destination=destination, value=value, then=then):
            return L0.Immediate(
                destination=destination,
                value=value,
                then=_statement(then),
            )

        case L1.Primitive(destination=destination, operator=operator, left=left, right=right, then=then):
            return L0.Primitive(
                destination=destination,
                operator=operator,
                left=right,
                right=left,
                then=_statement(then),
            )

        case L1.Branch(operator=operator, left=left, right=right, then=then, otherwise=otherwise):
            return L0.Branch(
                operator=operator,
                left=left,
                right=right,
                then=_statement(then),
                otherwise=_statement(otherwise),
            )

        case L1.Allocate(destination=destination, count=count, then=then):
            return L0.Allocate(destination=destination, count=count, then=_statement(then))

        case L1.Load(destination=destination, base=base, index=index, then=then):
            return L0.Load(
                destination=destination,
                base=base,
                index=index,
                then=_statement(then),
            )

        case L1.Store(base=base, index=index, value=value, then=then):
            return L0.Store(base=base, index=index, value=value, then=_statement(then))

        case L1.Halt(value=value):
            return L0.Halt(value=value)


#def close_statements(
#    statements: Sequence[L1.Statement],
    #fresh: Callable[[str], str],
#) -> L0.Statement:
#    _statement = partial(close_statement)
#    _statements = partial(close_statements)

#    match statements:
#        case []:
#            return _statements([])
#        case [first, *rest]:
#            pass
#        case _:  # pragma: no cover
#            raise ValueError(statements)


def close_program(
    program: L1.Program,
    #fresh: Callable[[str], str],
) -> L0.Program:
    _statement = partial(close_term, fresh=fresh)

    match program:
        case L1.Program(parameters=parameters, body=body):
            pass
            # return L0.Program(procedures=...)
        case _:  # pragma: no cover
            raise ValueError(program)   
        
