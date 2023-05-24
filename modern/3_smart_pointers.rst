Smart Pointers
#############################

This chapter talks about smart pointers. You will learn:

#. What are smart pointers?
#. When to use different smart pointer type?
#. Why should you use smart pointers?


What are the smart pointers and when to use them?
****************************************************

Let's start with some definition of smart pointers. In simple words it's type with values that may be used like pointers,
but with the added benefit of automated memory management. 
We have 3 types of smart pointers declared in `<memory>` STD library: 

* std::unique_ptr, 
* std::shared_ptr,
* std::weak_ptr.

In general, smart pointers are used in code which involves tracking the ownership of a piece of memory, 
allocating or de-allocating it. They typically eliminates the necessity to do these things explicitly.

It is worth to mentioned that regular pointers **can be still used** in code with oblivious memory ownership. 
This would typically be in functions which get a pointer from someplace else and do not allocate nor de-allocate, 
and do not store a copy of the pointer which outlasts their execution.

Let's take a deeper look into all types of smart pointers.

std::unique_ptr 
***************

According to C++ Reference:

    `std::unique_ptr` is a smart pointer that owns and manages another object through a pointer and disposes 
    of that object when the unique_ptr goes out of scope.

In other words it is a smart pointer with **unique object ownership** semantics. It is a 1-to-1 relationship between a pointer 
and its allocated object on the heap. And what is important if the unique pointer is destructed, 
the allocated object on the heap is destructed too.

Syntax
======

The unique pointer is declared as in the code below:

.. code-block:: cpp
   
   std::unique_ptr<int> ptr(new int); // allocation of new int on heap

As it was mentioned, the smart pointer having automated memory management they will be destructed with the end of the code code-block
they were declared in. Remember, that the object it points will be also destructed.

.. code-block:: cpp
   
   {
     std::unique_ptr<int> ptr(new int); 
     
     // pointer usage

   } // ptr is destructed, which means also int object is destructed

Usage
=====

General usage of std::unique_ptr is when you want your object to last only as long as a single owning reference to it does.
Let's take a look into some practical example demonstrate std::unique_ptr usage and some of its functions.

.. code-block:: cpp
   
   // big object declaration
   class foo {
   public:
     void bar() { ... }
   };

   void processFoo(const foo& object) { ... }

First, we will create the smart unique pointer. Remember to not use `new` operator on unique pointer directly.

.. code-block:: cpp
   
   std::unique_ptr<foo> foo_ptr(new foo());

We can call the method on the object using `->` operator:

.. code-block:: cpp
   
   foo_ptr->bar();

And pass the foo object reference to the function using `*` operator. Please remember that unique pointer 
cannot be copied or passed by value.

.. code-block:: cpp
   
   processFoo(*foo_ptr);

There is a possibility to access raw pointer using `get()` method. It's especially helpful if you want to use 
the smart pointer to manage memory while still passing the raw pointer to code that doesn't 
support smart pointers.

.. code-block:: cpp
   
   foo_ptr.get();

We can also free memory before exiting code block with unique pointer declaration using `reset()` method:

.. code-block:: cpp
   
   foo_ptr.reset();

std::make_unique
================

To make creation of unique pointers easier and safer, there `was std::make_unique` function introduced.
It constructs an object of given type and wraps it in a `std::unique_ptr`. See code below:

.. code-block:: cpp
   
   auto ptr = std::make_unique<int>(13);

This is also the preferable way of creating unique pointers (over using `new` operator). The only exception is
if you need a custom way to delete the object or are adopting a raw pointer from elsewhere - in that case do 
not use `std::make_unique`.

std::shared_ptr 
***************

Similarly like with std::unique_ptr we will start with C++ Reference definition of std::shared_ptr:

    `std::shared_ptr` is a smart pointer that retains shared ownership of an object through a pointer. 
    Several shared_ptr objects may own the same object.

It means that std::shared_ptr is smart pointer with **shared object ownership** semantics.
It is worth to mention that the shared pointer is destroyed when the last remaining shared_ptr 
owning the object is destroyed.

Syntax
======

The shared pointer is declared as in the code below:

.. code-block:: cpp
   
   std::shared_ptr<int> ptr(new int); // allocation of new int on heap

The allocated int (or any other object within std:shared_ptr) is called **managed object**.
In contrast to unique pointer, object managed by shared pointer can be shared with as many shared pointers as we like.

.. code-block:: cpp
   
   std::shared_ptr<int> ptr2 = ptr;
   auto ptr3 = ptr;

Usage
=====

Usually you will use std::shared_ptr when you do want to have numerous references to your object 
and you don't want it to be de-allocated until all of these references have been removed.

The methods showed for `std::unique_ptr` are the same for `std::shared_ptr`, like creation, calling object methods,
dereferencing, accessing raw pointer and resetting it. So in this part we will focus only on those functionalities 
specific for `std::shared_ptr`.

Let's start with copy-initialization and via assignment.

.. code-block:: cpp
   
   std::shared_ptr<int> ptr2(ptr);
   std::shared_ptr<int> ptr3 = ptr;


There is also possibility to check how many instances of std::shared_ptr manages the same object 
and if the current object is unique (no other shared pointer doesn't manage this object):

.. code-block:: cpp
   
   ptr.use_count(); // returns number of shared pointers managing the same object as ptr
   ptr.unique();    // returns true if ptr is the only shared_ptr managing object, false otherwise

And the last functionality is the comparison operation. Two unrelated shared pointers never will be equal 
(even when they contain the same information), but related shared pointers are always equal.

.. code-block:: cpp
   
   std::shared_ptr<std::string> pt1(new std::string("str1"));
   std::shared_ptr<std::string> pt2(new std::string("str1"));

   std::cout << pt1 == pt2; // return false as st1 and st2 are not related

   std::shared_ptr<std::string> pt3(pt1);
   
   std::cout << pt1 == pt3; // returns true as st1 and st3 are related

std::make_shared
================

As in std::unique_ptr case, for std::shared_ptr there is a dedicated (and preferred) method for creating pointers
called std::make_shared(). It constructs an object of given type and wraps it in a std::shared_ptr. See code below:

.. code-block:: cpp
   
   auto ptr = std::make_shared<int>(13);

Please be aware that there is no way to release the memory for the control block and the managed object separately 
when using std::make_shared. It creates a single heap-allocation for both the control block and the managed object so 
we have to wait until we can release both the managed object and the control block.

std::weak_ptr 
***************

As C++ Reference defines:

    std::weak_ptr is a smart pointer that holds a non-owning ("weak") reference to an object that is managed 
    by std::shared_ptr. It must be converted to std::shared_ptr in order to access the referenced object.

Syntax
======

The weak pointer is declared as in the code below:

.. code-block:: cpp
   
   std::weak_ptr ptr;

And later it can be used to observe the object of a shared pointer:

.. code-block:: cpp
   
   auto sh_ptr = std::make_shared<int>(13)
   ptr = sh_ptr; // watches the managed object of sh_ptr

Please remember that control block on a shared pointer object keeps track of the number of **shared and weak pointers**. 
The object is removed when the shared counter hits zero, but the control block remains active until the weak counter
reaches zero as well.

Usage
=====

But why we would like to even use it? 

Sometimes an object has to store a way to access the shared_ptr's underlying object 
without increasing the reference count. Often, this problem occurs when shared_ptr objects have cyclic references.

Other general use case is when you do want to refer to your object from multiple places - and do not want your object to 
be de-allocated until all these references are themselves gone.

Summary
*******
