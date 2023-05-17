Move Semantics
#############################

This chapter talks about move semantics. You will learn:

#. What is move semantics?
#. What are different value categories and when to use them?
#. What is universal reference T&&?
#. How and why to use std::move?
#. How to create move constructor? (Rule of 5)

Introduction
************

Move semantics allows an object, under certain conditions, to take ownership of some other object's external resources.

Value categories (glvalue and rvalue)
**************************************

#. Definitions and differences between them
   
   * glvalues - expressions that have an identity; possible to determine if two expressions refer to the same entity
   * rvalues - expressions that can be moved from
   * lvalues - have an identity and can't be moved from
   * xvalues - have an identity and can be moved from
   * prvalues - don’t have an identity and can be moved from
   * diagram showing different expression types and dependencies between them

   .. figure:: /_images/move-semantics-expressions.png

#. Example of functions returning lvalue and prvalue
#. Conversion from lvalue to prvalue

   * An lvalue may be converted to a rvalue: this is totally legal and occurs frequently. Let’s look on +operator as an example. According to C++ specification it takes two rvalues as arguments and returns an rvalue.
    
    .. code-block:: cpp
       
       int x = 10, y=20;
       int z = x+y;
    
   x and y are lvalues, but the addition operator wants rvalues. How is it possible? Because of an implicit lvalue-to-rvalue conversion. 

#. rvalue reference 

Universal references (&&)
*************************

#.	What is it?

std::move
***************

#. What is std::move?

   * According to cppreference (https://en.cppreference.com/w/cpp/utility/move) > std::move is used to indicate that an object t may be "moved from", i.e. allowing the efficient transfer of resources from t to another object.
   * way to efficiently transfer contents of an object to another leaving the source in a valid but undefined state
   * when you move a value from a register or memory location to another place, the value on the source register or memory location is still there

#. Code showing std::move usage and its explanation


Move constructor (and its comparison with copy constructor) 
************************************************************

weak reference to an object managed by std::shared_ptr

#. What it is?
#. Creating simple move constructor
#. Rule of 5

How to benefit from move semantics
**********************************

#. a.	Performance impact of move

Summary
=======
