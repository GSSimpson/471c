## Description of changes from L2
Similar structure as L3 and L2, but with more things added, removed, and changed, along with functionalities being changed to accomodate. It also looks like the language is shifting from a tree-structure to a more linear one, with some statements having 'then' fields that take statements that happen after the current one.

Removed things: term, let, reference, begin
Added things: statement, copy, halt

# Program
same structure as L3 and L2, with the body changing from a term to a statement

# Statement
New type, structured the same as term in L3 and L2. As with term, it encompasses the follwing listed items:

# Copy
Statement that takes a source and destination identifier and a then statement. It loads from the source, and stores it into the destination. The then statement appears to be what is seen in other statements with then fields.

# Abstract
Statement that takes a destination identifier, and a sequence of identifiers as parameters. It also takes a term for the body and a term for 'then.' It differes from L2's abstract by having a destination and then field, and its parameters switched from a sequence of terms to identifiers.

# Apply
Appears to have the same structure as with L2, but with the target field switching from a term/statement to an identifier, and the arguments field switching from a sequence of terms to a sequence of strings.

# Immediate
In addition to its value field seen in L3 and L2, it also has a destination field foe an immediate, along with a then field like some other statements in L1.

# Primitive
Similar to L2 with an identical operator field that takes "+", "-", or "*". It also has a left and right field, but instead of terms, it now takes identifiers. It also has a then field for the next statement, as it no longer holds statements/terms as children like in L3 and L2.

# Branch
Has almost the same fields as with L3 and L2, with operator being the same. Left and right now take identifiers like with primitive. Consequent has been replaced by the then field, taking a statement, and the otherwise field is also still present, taking a statement as well.

# Allocate
Now has a destination identifier, and its count field is unchanged. It also now has a then statement.

# Load
The index is unchanged, and the base is an identifier instead of a term like in L2. It has also gained a destination field that holds an identifier and a then statement.

# Store
Similar to L2, but with base taking an identifier instead of a term, index is also still being handeled the same way as load an allocate do, and value also now being an identifier instead of a term. There is also a then statement.

# Halt
New statement that has a tag like all other statemts, a value field that holds an identifier, and nothing else. The lack of a then statement means nothing is done after it.