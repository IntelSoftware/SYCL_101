std::array Container
####################

This chapter covers the :code:`std::array` container. You will learn the following:

#. What is std::array and why was it created?
#. What is the syntax of :code:`std::array`?

Introduction
************

Let's start with the definition.

**std::array** is a container that is built on top of fixed-size arrays. It combines the performance and accessibility of a C-style array with other benefits of a standard container such as:

* knowing its own size
* supporting assignment 
* random access iterators

It also supports standard container operations like :code:`std::sort`, :code:`std::find`, etc.

:code:`std::array` is similar to a C-style array but not identical. When we pass a C-style array to a function, we have to pass the address and the size of the array. The reason is that the information about the array size gets lost when passing the array address to the function (i.e., in form of pointer).  This problem can be solved using std::array.  To use std::array, remember to include :code:`<array>` STL.

This datatype is especially important when using SYCL as it doesn't allow dynamic memory allocation in a kernel.

Syntax of std::array
********************

An example of a :code:`std::array` declaration is shown in the code below:

.. code-block:: cpp
   
   std::array<int, 5> n;

We need to specify the datatype that will be stored in the array (in the example, it is :code:`int`) and its size (:code:`5` in the example code).

To initialize an :code:`std::array`, we can simply assign values to it at declaration.

.. code-block:: cpp
   
   std::array<int, 5> n = {0, 1, 2, 3, 4};
   std::array<int, 5> m {0, 1, 2, 3, 4}; 

As the length of the array needs to be known at compile time, we can declare the array and later initialize it with values.

.. code-block:: cpp
   
   std::array n;
   n = {0, 1, 2, 3, 4};

Usage
======

We can use :code:`std::array` in every situation when we are using a C-style array. Just make sure you know its size in advance.

To access the element at a specific position, we can use C-style brackets :code:`[ ]` (because the std::array elements are placed side by side in memory) or the :code:`at()` method. The only difference between them is that :code:`at()` checks bound, while using the C-style brackets doesn't check bound.

.. code-block:: cpp
   
   std::array n {1, 2, 3, 4, 5};
   n[3];    // returns element of the array at position 3, doesn't check bound
   n.at(3); // returns element of the array at position 3, checks bound

We can also access the first and last element of the array using :code:`front` and :code:`back`:

.. code-block:: cpp
   
   n.front(); // returns first element of the array
   n.back();  // returns last element of the array

To get the length of the :code:`std::array`, use the :code:`size()` method:

.. code-block:: cpp
   
   n.size();


Like other standard containers, the :code:`std::array` provides iterator functions that allow it to iterate over the container in a standard or reversed way.

Multidimensional Array
======================

Like in C-style arrays, it's possible to create a multidimensional :code:`std::array`. Let's look at the example with a 5x3 :code:`std::array`:

.. code-block:: cpp
   
   std::array<std::array<int, 5>, 3> n {
     {0, 1, 2, 3, 4}, 
     {0, 1, 2, 3, 4}, 
     {0, 1, 2, 3, 4}
   };

This means that as a datatype for the outer array, we are using another array.

    When using SYCL, consider not using an array of arrays. Instead, use a dedicated structure that contains arrays. It will improve memory optimization when storing and accessing the elements. What is more, it will be more readable for other developers.
