Initializers in if and switch statements
#########################################

This chapter talks about initializers statements is if and switch blocks. You will learn:

#. What initializer-statement is? 
#. Why you can benefit from using it inside the if-else and switch blocks?
#. What is the syntax of initializer statements in if and switch blocks? 

Introduction
************

There is a lot of situation when we need to check the value returned by function or perform 
conditional operations based on this value. Let's take a look at the example pseudo-code below:

.. code-block:: cpp
   
   // some function declaration
   int foo(/*...*/)

   // function call and return value storing in variable
   int var = foo(/*...*/);

   if (var == /*some value*/){
      // do something
   } else {
      // do something else
   }

There is nothing wrong with this code it can be improved in some specific situation. 

You can see, that in shown example, the variable :code:`var` is used only for this if-else 
statement. At the same time it leaks into the surrounding scope. In that case we need to deal with 
it, and make sure to not mix it up with other variables.

Also, if the compailer can explicitly know that this variable will be used only there, it may 
optimize the code better.

Syntax
*******

Let's take a look at the syntax of the if-else and switch blocks. 

Initializer statement outside the conditional blocks
========================================================

You may notice that if-else conditional blocks and switch blocks have a generic format.
First, we have an initialization of a variable that will be checked, and then there is a conditional
block using this initialized variable. 

For if-else block it usually looks like this:

.. code-block:: cpp
   
   // initializer-statement

   if (condition){
      // do something
   } else {
      // do something else
   }

And for switch block, similarly, like this:


.. code-block:: cpp
   
   // initializer-statement

   switch(variable){
      // cases
   }

Initializer statements in if and switch blocks
===============================================

Starting with C++17 it is possible to initialize a variable inside an if-statement and 
a switch-statement. It means that the examples shown before can now be presented as:

For if-else block:

.. code-block:: cpp

   if (initializer-statement; condition){
      // do something
   } else {
      // do something else
   }

And for switch block, similarly, like this:

.. code-block:: cpp

   switch(initializer-statement; variable){
      // cases
   }

Summary
********

Initializers in if-statements and switch-statements allow assignment of the variable to the scope 
of this statement. It is important that using it can result in more complex code than when those 
concerns (initialization and comparison) are separate.