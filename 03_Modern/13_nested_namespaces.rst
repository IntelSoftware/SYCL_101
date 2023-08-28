Nested Namespaces with inlined variables explanation 
##################################################################

This chapter talks about C++ namespaces. You will learn:

#. What is namespace?
#. How to declare your own namespace?
#. How nested namespaces work in C++?

Introduction
************

The **namespace** is a declarative region providing a scope to the identifiers like names of types, 
functions, variables, etc. Namespaces are usually used to organize the code into logical groups and,
also, to avoid name collisions. It can be especially important, when you're using different 
libraries.

One of the example of namespace scope is the C++ standard library (std) where all the classes, 
methods and templates are declared. You can find in the code :code:`std::` before multiple class or 
functions declarations form STL in C++. Sometimes you can also find directive
:code:`using namespace std;`.

Defining a namespace
=====================

To define a namespace you have to start with :code:`namespace` keyword followed by the name, as 
below:

.. code-block:: cpp
   
   namespace your_namespace_name {
      // ...
      // declarations
      // ...
   }

Note that there i no semicolon :code:`;` after the closing bracket. 
To call the function or variable declared within the namespace, prepend the namespace name as below:

.. code-block:: cpp
   
   your_namespace_name::function_name(/*...*/);
   your_namespace_name::variable_name;


Nested namespaces
******************

In C++, namespaces can be nested, where there is a possibility to define one namespace inside 
another one. The resolution of namespace variables is hierarchical. The syntax looks as below:

.. code-block:: cpp
   
   namespace A {
      // ...
      // declarations
      namespace B {
      // ...
      // declarations
         namespace C {
         // ...
         // declarations
         }
      }
   }

As you can see, hose declaration take a lot of space and sometimes it can be difficult to track all 
of the levels of namespaces declared. But in modern C++ nested namespaces can be also write simpler,
as below:

.. code-block:: cpp
   
   namespace A::B::C {
         // ...
         // declarations
   }

It is really useful when you want to declare functions, variables etc. just in the deepest 
namespace. It also allows you to easy track the namespace in which yore writing your declarations.

Similarly as with single namespace, to call the function or variable declared within the nested 
namespace you need to write all levels of the namespaces, like below:

.. code-block:: cpp
   
   A::B::C::function_name(/*..*/);
   A::B::C::variable_name;

Now, let's see it on the real example:

.. code-block:: cpp
   
   #include <iostream>

   // outer namespace declaration
   namespace outer {
      void foo() {
         std::cout << "Outer foo() function call. \n";
      }

      // inner namespace declaration
      namespace inner {
         void foo() {
            std::cout << "Inner foo() function call. \n";
         }
      }
   }


   int main() {
      outer::inner::foo();
      outer::foo();

      return 0;
   }
   
Output of the following code will be:

.. code-block:: 
   
   Inner foo() function call. 
   Outer foo() function call. 


It means, that first inner foo function was called, then the outer foo function.




