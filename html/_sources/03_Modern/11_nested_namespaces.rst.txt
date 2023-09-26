Nested Namespaces
##################

This chapter covers C++ namespaces. You will learn the following:

#. What is a namespace?
#. How can you declare your own namespace?
#. How do nested namespaces work in C++?

Introduction
************

The **namespace** is a declarative region that provides scope to the identifiers like names of types, functions, and variables. Namespaces are usually used to organize the code into logical groups and to avoid name collisions. It can be especially important when you're using different libraries.  One of the examples of the namespace scope is the C++ Standard Template Library (STL), where all the classes, methods, and templates are declared. You can find STL namespace in the code :code:`std::\` before multiple class or function declarations from STL in C++. Sometimes you can also find the directive :code:`using namespace std;`. 

Defining a Namespace
=====================

To define a namespace, you have to start with the :code:`namespace` keyword followed by the name:

.. code-block:: cpp
   
   namespace your_namespace_name {
      // ...
      // declarations
      // ...
   }

Note that there is no semicolon :code:`;` after the closing bracket. To call the function or variable declared within the namespace, prepend the namespace name as shown below:

.. code-block:: cpp
   
   your_namespace_name::function_name(/*...*/);
   your_namespace_name::variable_name;


Nested Namespaces
******************

In C++, namespaces can be nested, which makes it possible to define one namespace inside another. The resolution of namespace variables is hierarchical. The syntax is shown below:

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

As you can see, those declarations take a lot of space and sometimes it's difficult to track all the levels of the declared namespaces. But in modern C++, writing nested namespaces can be simplified:

.. code-block:: cpp
   
   namespace A::B::C {
         // ...
         // declarations
   }

It is useful when you want to declare functions and variables in the deepest namespace. It also allows you to easily track the namespace in which you're writing your declarations.  Similarly, as with a single namespace, to call the function or variable declared within the nested namespace, you need to write all levels of the namespaces:

.. code-block:: cpp
   
   A::B::C::function_name(/*..*/);
   A::B::C::variable_name;

Now, let's see it in the real example:

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
   
The output of the code will look like this:

.. code-block:: 
   
   Inner foo() function call. 
   Outer foo() function call. 


This means that the inner foo function was called first, followed by the outer foo function.
