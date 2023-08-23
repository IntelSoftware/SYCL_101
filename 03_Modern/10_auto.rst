Type Inference in C++ (auto and decltype)
############################################

This chapter talks about type inference. You will learn:

#. What is type reference in C++?
#. How to use :code:`auto` and :code:`decltype` keywords?
#. What are the differences between :code:`auto` and :code:`decltype`? 

Introduction
************
**Type Inference** refers to automatic deduction of the data type of an expression 
in a programming language. Since C++11 in language specification many keywords were 
included which allows to leave the type deduction to the compailer. Before C++11 
it was impossible and each data type needed to be *explicitly declared* at compile time. 

Now, using type inference capabilities, we can avoid waisting time writing out things that compailer 
knows. As all the types are deduced in the compiler phase only, the time for compilation increases 
slightly at the same time it doesn't affect the run time of the created program.

In C++ we have two keywords introduced as a type inference:

* :code:`auto` keyword
* :code:`decltype` type specifier

and we will discuss them one by one.

:code:`auto` keyword
*********************

:code:`auto` keyword indicates that the type of declared variable to be deduced automatically 
from its initializer. If the return type of a function is :code:`auto` it will be evaluated 
at runtime by the returned type expression.

What is important, the variable declared with :code:`auto` keyword needs to be initialized 
at the declaration time. Otherwise the compilation error occurs.

For better understanding, let us see the example of :code:`auto` usage.

.. note:: 
   In shown examples we are using :code:`typeid` to get the type of the variables.

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

and it means that variable :code:`x` is type od :code:`int`, when variable :code:`y` is type of 
:code:`double`

:code:`auto` can be easily used to avoid long initializations, e.g. when creating iterators for 
containers.

:code:`decltype` type specifier
********************************

:code:`decltype` type specifier inspects the declared type of an entity or the type of 
an expression. We can say that :code:`decltype` is more like a operator that evaluates 
the type of passed expression. 

When you use :code:`auto` you declare a variable with a particular type, byt when using 
:code:`decltype` you extract the type from the variable.

For better understanding, let us see the example of :code:`decltype` usage.

.. code-block:: cpp
   
   #include <iostream>
   #include <typeinfo> 

   int foo() { return 13; }

   int main(){
      // x has the sam type as a type returned by foo function
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

In this example we are using :code:`auto` and :code:`decltype` for the same 
purpose - deduction of the iterator type.

.. note::
   The type denoted by decltype can be different from the type deduced by auto.

Summary
*********

As a summary, let's make sure that we understand that :code:`auto` and :code:`decltype` 
serve different purposes so they don't map one-to-one.

:code:`auto` is a keyword that is used for automatic type deduction, when :code:`decltype` 
type specifier yields the type of a specified expression. Unlike auto that deduces types 
based on values being assigned to the variable, decltype deduces the type from an expression 
passed to it. 
