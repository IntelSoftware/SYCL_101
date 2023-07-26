std::array container
####################

This chapter talks about :code:`std::array` container. You will learn:

#. What is std::array and why it was created?
#. What is the syntax of std::array?

Introduction
************

Let's start with definition.

**std::array** is a container build on top of fixed size arrays. 
It combines the performance and accessibility of a C-style array 
with other benefits of a standard container, such as:

* knowing its own size,
* supporting assignment, 
* random access iterators.

It also means that it supports standard container operations like :code:`std::sort`, :code:`std::find` etc.

std::array is similar to C-style array but not identical. When we pass C-style array to a function,
we have to pass both address of the array and its size. The reason for that is that the information
about array size gets lost when passing array address to the function i.e. in form of pointer.
This problem can be solved using std::array.

To use std::array remember to include :code:`<array>` STL.

This datatype is especially important when using SYCL as it doesn't allow 
to dynamically allocate memory in a kernel.

syntax of std::array
********************

Example std::array declaration is shown in code below:

.. code-block:: cpp
   
   std::array<int, 5> n;

We need to specify the datatype that will be stored in array (in example it is :code:`int`) 
and its size (:code:`5` in example code).

To initialize an std::array we can simply assign values to it at the time of declaration.

.. code-block:: cpp
   
   std::array<int, 5> n = {0, 1, 2, 3, 4};
   std::array<int, 5> m {0, 1, 2, 3, 4}; 

As the length of array needs to be know as the time of compilation we can declare array 
and later initialize it with values.

.. code-block:: cpp
   
   std::array n;
   n = {0, 1, 2, 3, 4};

Usage
======

We can use std::array in every situation when we are using C-style array. Just make sure 
\you know the size of it in advance.

To access the element at specific position we can use C-style brackets :code:`[ ]` (because the 
std::array elements are placed side by side in the memory) or :code:`at()` method. 
The only difference between them is that :code:`at()` checks bound, when using brackets doesn't perform it.

.. code-block:: cpp
   
   std::array n {1, 2, 3, 4, 5};
   n[3];    // returns element of the array at position 3, doesn't check bound
   n.at(3); // returns element of the array at position 3, checks bound

We can also access first and last element of the array using :code:`front` and :code:`back`:

.. code-block:: cpp
   
   n.front(); // returns first element of the array
   n.back();  // returns last element of the array

To get the length of the std::array use :code:`size()` method:

.. code-block:: cpp
   
   n.size();

The std::array like every other standard container provides iterator functions that allow
to iterate over container in standard or reversed way. 

Multidimensional array
======================

Like in C-style arrays, there is a possibility to create multidimensional std::array. Let's look 
at the example with 5x3 std::array:

.. code-block:: cpp
   
   std::array<std::array<int, 5>, 3> n {
     {0, 1, 2, 3, 4}, 
     {0, 1, 2, 3, 4}, 
     {0, 1, 2, 3, 4}
   };

It means that as a datatype for the outer array we are using other array. 

    When using SYCL please consider not using array of arrays. Instead of that, use 
    dedicated structure containing arrays. It will allow for better memory optimization
    when storing the elements but also when accessing them. What is more, it will be 
    more readable for other developers.

Summary
*******
