Type Inference in C++ (auto and decltype)
############################################

This chapter talks about type inference. You will learn:

#. What is type reference in C++?
#. How should the keywords :code:`auto` and :code:`decltype` be used?
#. What are the differences between :code:`auto` and :code:`decltype`? 

Introduction
************
**Type inference** refers to the automatic deduction of the data type of an expression 
in a programming language. Since C++11 in language specification, many keywords were 
included that allow the type deduction to be left to the compiler. Before C++11, 
it was impossible and each data type needed to be *explicitly declared* at compile time. 

Now, using type inference capabilities, we can avoid wasting time writing out things that the compiler 
knows. As all the types are deduced in the compiler phase only, the compilation time increases 
slightly; at the same time, it doesn't affect the runtime of the created program.

In C++, two keywords are introduced as a type inference, which we will cover below:

* :code:`auto` keyword
* :code:`decltype` type specifier


:code:`auto` keyword
*********************

The :code:`auto` keyword indicates the type of declared variable to be deduced automatically 
from its initializer. If the return type of a function is :code:`auto`, it will be evaluated 
at runtime by the returned type expression.

It's important to note that the variable declared with the :code:`auto` keyword needs to be initialized 
at declaration time. Otherwise, a compilation error occurs.

For better understanding, let's see the example of :code:`auto` usage.

.. note::
   In these examples, we are using :code:`typeid` to get the type of the variables.

.. code-block:: cpp
   
   #include <iostream>
   #include <typeinfo> 

   int main(){
      auto x = 1;
      auto y = 3.7;

      // checking type of declared variables
      std::cout << typeid(x).name() << '\n';
      std::cout << typeid(y).name() << '\n';

      return 0;
   }

The output of the code above is:

.. code-block:: bash
   
   i
   d

and it means that variable :code:`x` is type of :code:`int` when variable :code:`y` is type of :code:`double`.

:code:`auto` and it can be easily used to avoid long initializations (e.g., when creating iterators for 
containers).

:code:`decltype` type specifier
********************************

The :code:`decltype` type specifier inspects the declared type of an entity or the type of 
an expression. We can say that :code:`decltype` is more like an operator that evaluates 
the type of passed expression. 

When you use :code:`auto`, you declare a variable with a particular type; but, when using 
:code:`decltype`, you extract the type from the variable.

For better understanding, let's see the example of :code:`decltype` usage.

.. code-block:: cpp
   
   #include <iostream>
   #include <typeinfo> 

   int foo() { return 13; }

   int main(){
      // x has the same type as a type returned by foo function
      decltype(foo()) x;

      // checking type of x
      std::cout << typeid(x).name();

      return 0;
   }

The output of the code above is:

.. code-block:: bash
   
   i 

and it means that variable :code:`x` is type of :code:`int`.

Now, let's see the example when we are using both :code:`auto` and :code:`decltype`.

.. code-block:: cpp
   
   #include <iostream>
   #include <vector>

   int main(){
      
      std::vector<int> vec(10);
       
      // using auto for type deduction
      for(auto i = vec.begin(); i < vec.end(); i++){
         std::cin >> *i;
      }
      
      // using decltype for type deduction
      for(decltype(vec.begin()) i = vec.begin(); i < vec.end(); i++){
         std::cin >> *i;
      }
      
      return 0;
   } 

In this example, we are using :code:`auto` and :code:`decltype` for the same 
purpose — deduction of the iterator type.

.. note::
   The type denoted by :code:`decltype`  can be different from the type deduced by :code:`auto`.

Summary
*********

In summary, it's important to understand that :code:`auto` and :code:`decltype` 
serve different purposes, so they don't are not exactly the same.

:code:`auto` is a keyword that is used for automatic type deduction when the :code:`decltype` 
type specifier yields the type of a specified expression. Unlike :code:`auto`, which deduces types 
based on values being assigned to the variable, :code:`decltype` deduces the type from an expression 
passed to it. 
