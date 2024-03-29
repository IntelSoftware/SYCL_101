Initializers in if and switch Statements
#########################################

This chapter covers initializer statements in if and switch blocks. You will learn the following:

#. What is an initializer statement? 
#. How can you benefit from using it inside the if-else and switch blocks?
#. What is the syntax of initializer statements in if and switch blocks? 

Introduction
************

There are many situations when we need to check the value returned by a function or perform conditional operations based on the value of the function. Let's look at the example pseudocode below:

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

There is nothing wrong with this code, but it can be improved in certain situations. As shown in the example, the variable :code:`var` is used only for this if-else statement. At the same time, it leaks into the surrounding scope. In that case, we need to make sure to not mix it up with other variables.  Also, if the compiler can explicitly know that this variable will only be used there, it may potentially produce more optimized code.

Syntax
*******

Let's look at the syntax of the if-else and switch blocks. 

Initializer Statement Outside the Conditional Blocks
========================================================

You may notice that if-else conditional blocks and switch blocks have a generic format.  First, we have an initialization of a variable that will be checked, and then there is a conditional block using this initialized variable. For an if-else block, it usually looks like this:

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

Initializer Statements in if and switch Blocks
===============================================

Starting with C++17, it is possible to initialize a variable inside if and switch statements:

.. code-block:: cpp

   if (initializer-statement; condition){
      // do something
   } else {
      // do something else
   }


.. code-block:: cpp

   switch(initializer-statement; variable){
      // cases
   }

Summary
********

Initializers in if and switch statements allow the variable to be assigned to the scope of this statement. Note that using this language feature can result in more complex code when initialization and comparison are separate concerns.
