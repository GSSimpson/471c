## Description
The general design of this language is that it consists of 'terms' that interact in a tree structure. Some terms have direct values while others have bodies and/or left and right branches that are other terms.

# Program
The highest scope and root of the tree. Has a body of one term and a parameter of a sequence of identifiers. Is also the one class to not correspond with a valid term, in order to keep it from duplicating.

# Term
A defined type that consists of the items listed below, each defined with a tag that states the specific item in the sequence of valid terms.

# Let
A term that produces a sequence of bindings that associate specific terms with identifiers. It also has a term for a body.

# LetRec
Performs a similar role to Let, but works recursively

# Reference
term that holds a specified identifier

# Abstract
A term that holds a sequece of identifiers and a body consisting of a term. Same structure of a program, but a term and can be placed where terms can be. Identifiers are used in the subtree originating from it.

# Apply
A term that takes a target term and a sequence of terms as arguments for the target

# Immediate
A term that holds an integer value and has no branches or children--would be a leaf of the tree

# Primitive
A term that has a left and right branch term and performs an addition, subtraction, or multiplication operation with their values.

# Branch
A term that has a left and right branch term and performs a less than or equal to operation on them. It also has a consequent and otherwise term for the result of the evaluation.

# Allocate
A term that takes a count

# Load
A term that takes a bese term and an index from memory to load from

# Store
A term that takes a base term, an index, and a value term to store.


# Begin
A term that takes an 'effects' sequence of terms and a value term
