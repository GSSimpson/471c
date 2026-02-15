## Description
Very similar to L1, but it appears to be even more linear, and with statements not containing other statements as much as possible beyond then fields for the next one in line. There is also the inclusion of a new class called procedure that isn't a statement and exists between program and statements.

Added: Procedure, Address, Call
Removed: Abstract, Apply

# Program
Changed from L1 to no longer have parameters or a body, but instead it now hols a sequence of procedures that seem to function far more like programs did in the other languages.

# Procedure
New class structured identically to programs from L1, but with the inclusion of a name field that holds an identifier. Sits in bewtween the program and the statements, and allows the program to be divided into separate procedures. 

# Statement
Unchanged from L1, other than adjustments to include new statements an not include removed ones.

# Copy
unchanged from L1

# Immediate
unchanged from L1

# Primitive
unchanged from L1

# Branch
unchanged from L1

# Allocate
unchanged from L1

# Load
unchanged from L1

# Store 
unchanged from L1

# Address
New statement that takes a destination identifier and a name identifier. It also takes a then statement.

# Call
New statement that takes a target identifier, and a sequence of identifiers as parameters to allow the statement to call a procedure. It also has a then statement.

# Halt
unchanged from L1