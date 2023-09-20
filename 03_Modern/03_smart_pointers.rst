Smart Pointers
#############################

This chapter covers smart pointers. You will learn the following:

#. What are smart pointers?
#. When should different smart pointer types be used?
#. Why should you use smart pointers?


What are Smart Pointers and When Should They be Used?
**********************************************************

Let's start with the definition of smart pointers. Smart pointers are a type with values that may be used like pointers but with the added benefit of automated memory management. We have three types of smart pointers declared in the :code:`<memory>` STD library: 

* std::unique_ptr 
* std::shared_ptr
* std::weak_ptr

In general, smart pointers are used in code that involves tracking the ownership of a piece of memory and allocating or deallocating it. They typically eliminate the necessity to do these things explicitly.

It is worth mentioning that regular pointers can be still used in code with oblivious memory ownership. This would typically be in functions that get a pointer from someplace else and do not allocate or deallocate memory and do not store a copy of the pointer that outlasts their execution.  Let's take a deeper look at each of the smart pointer types.

std::unique_ptr 
***************

According to the C++ Reference:

    :code:`std::unique_ptr` is a smart pointer that owns and manages another object through a pointer and disposes of that object when the unique_ptr goes out of scope.

In other words, it is a smart pointer with **unique object ownership** semantics. It is a 1-to-1 relationship between a pointer and its allocated object on the heap. It's important to know that if the unique pointer is destructed, the allocated object on the heap is also destroyed.

Syntax
======

The unique pointer is declared as follows:

.. code-block:: cpp
   
   std::unique_ptr<int> ptr(new int); // allocation of new int on heap

As mentioned previously, the smart pointer has automated memory management. It will be destroyed at the end of the code block in which it was declared. Remember, the object it points to will also be destroyed.

.. code-block:: cpp
   
   {
     std::unique_ptr<int> ptr(new int); 
     
     // pointer usage

   } // ptr is destroyed, which means the int object is also destroyed

Usage
=====

Generally, :code:`std::unique_ptr` is used when you want your object to last only as long as a single owning reference to it does. Let's look at a practical example to demonstrate :code:`std::unique_ptr` usage and some of its functions.

.. code-block:: cpp
   
   // big object declaration
   class foo {
      public:
      void bar() { ... }
   };

   void processFoo(const foo& object) { ... }

First, we will create the smart unique pointer. Remember, do not use :code:`new` operator on the unique pointer directly.

.. code-block:: cpp
   
   std::unique_ptr<foo> foo_ptr(new foo());

We can call the method on the object using the `->` operator:

.. code-block:: cpp
   
   foo_ptr->bar();

And pass the foo object reference to the function using the :code:`*` operator. Note that the unique pointer cannot be copied or passed by value because it is a pointer.

.. code-block:: cpp
   
   processFoo(*foo_ptr);

It's possible to access the raw pointer using the :code:`get()` method. It's especially helpful if you want to use the smart pointer to manage memory while still passing the raw pointer to code that doesn't support smart pointers.

.. code-block:: cpp
   
   foo_ptr.get();

We can also free memory before exiting the code block with a unique pointer declaration using the :code:`reset()` method:

.. code-block:: cpp
   
   foo_ptr.reset();

std::make_unique
================

To make the creation of unique pointers easier and safer, the :code:`std::make_unique` function constructs an object of a given type and wraps it in :code:`std::unique_ptr`:

.. code-block:: cpp
   
   auto ptr = std::make_unique<int>(13);

This is also the preferred way to create unique pointers (instead of using the :code:`new` operator). The only exception is when you need to customize a way to delete the object or are adopting a raw pointer from elsewhere —. In that case, do not use :code:`std::make_unique`.

std::shared_ptr 
***************

Similar to :code:`std::unique_ptr`, we will start with the C++ Reference definition of :code:`std::shared_ptr`:

    :code:`std::shared_ptr` is a smart pointer that retains shared ownership of an object through a pointer. Several shared_ptr objects may own the same object.

This means that :code:`std::shared_ptr` is a smart pointer with **shared object ownership** semantics. It is worth mentioning that the shared pointer is destroyed when the remaining :code:`std::shared_ptr` owning the object is destroyed.

Syntax
======

The shared pointer is declared as follows:

.. code-block:: cpp
   
   std::shared_ptr<int> ptr(new int); // allocation of new int on heap

The allocated int (or any other object within :code:`std:shared_ptr`) is called a **managed object**.  In contrast to the unique pointer, an object managed by a shared pointer can be shared with as many shared pointers as we like.

.. code-block:: cpp
   
   std::shared_ptr<int> ptr2 = ptr;
   auto ptr3 = ptr;

Usage
=====

Usually, you will use :code:`std::shared_ptr` when you do want numerous references to your object and you don't want it to be deallocated until all of these references have been removed.

The methods shown for :code:`std::unique_ptr` are the same for :code:`std::shared_ptr`, like creation, calling object methods, dereferencing, accessing the raw pointer, and resetting it. In this part, we will focus only on those functionalities specific to :code:`std::shared_ptr`.

Let's start with copy initialization and via assignment.

.. code-block:: cpp
   
   std::shared_ptr<int> ptr2(ptr);
   std::shared_ptr<int> ptr3 = ptr;


It's also possible to check how many instances of :code:`std::shared_ptr` manage the same object and if the current object is unique (i.e., other shared pointers don't manage this object):

.. code-block:: cpp
   
   ptr.use_count(); // returns number of shared pointers managing the same object as ptr
   ptr.unique();    // returns true if ptr is the only shared_ptr managing object, false otherwise

Finally, the last functionality is the comparison operation. Two unrelated shared pointers will never be equal (even when they contain the same information), but related shared pointers are always equal.

.. code-block:: cpp
   
   std::shared_ptr<std::string> pt1(new std::string("str1"));
   std::shared_ptr<std::string> pt2(new std::string("str1"));

   std::cout << pt1 == pt2; // return false because pt1 and pt2 are not related

   std::shared_ptr<std::string> pt3(pt1);
   
   std::cout << pt1 == pt3; // returns true because pt1 and pt3 are related

std::make_shared
================

As in the case of :code:`std::unique_ptr`, :code:`std::shared_ptr` includes a dedicated (and preferred) method for creating pointers called :code:`std::make_shared()`. It constructs an object of a given type and wraps it in :code:`std::shared_ptr`:

.. code-block:: cpp
   
   auto ptr = std::make_shared<int>(13);

Be aware that there isn't a way to release the memory for the control block and the managed object separately when using :code:`std::make_shared`. It creates a single heap allocation for both the control block and the managed object, so we have to wait until we can release both the managed object and the control block.

std::weak_ptr 
***************

As the C++ Reference defines:

    :code:`std::weak_ptr` is a smart pointer that holds a non-owning ("weak") reference to an object that is managed by :code:`std::shared_ptr`. It must be converted to :code:`std::shared_ptr` in order to access the referenced object.

Syntax
======

The weak pointer is declared as in the code below:

.. code-block:: cpp
   
   std::weak_ptr ptr;

And later it can be used to observe the object of a shared pointer:

.. code-block:: cpp
   
   auto sh_ptr = std::make_shared<int>(13)
   ptr = sh_ptr; // watches the managed object of sh_ptr

Remember that a control block on a shared pointer object keeps track of the number of **shared and weak pointers**. The object is removed when the shared counter hits zero, but the control block remains active until the weak counter also reaches zero.

Usage
=====

Why would we ever use a weak pointer? Generally, weak pointers are used when you do want to refer to your object from multiple places and do not want your object to be deallocated until all these references are themselves gone.  Sometimes, you need to store the shared_ptr's underlying object without increasing the reference count. Often, this issue occurs when :code:`shared_ptr` objects have cyclic references. Let's see an example:

.. code-block:: cpp
   
   struct A;

   struct B {
      std::shared_ptr<A> A_ptr;
      ~B() { std::cout << "~B()"; }
   };

   struct A {
      std::shared_ptr<B> B_ptr;
      ~A() { std::cout << "~A()"; }
   };

   int main() {
      auto BB = std::make_shared<B>();
      auto AA = std::make_shared<A>();

      AA->B_ptr = BB;
      BB->A_ptr = AA;

      return 0;
   }

The problem with the code above is that destructors will not be called so there is a memory leak. Keep in mind that the managed object of the shared pointer is deleted when the reference count reaches zero —. Let's analyze the situation.
When :code:`BB` goes out of scope, it will be not be deleted because it still manages the object to which :code:`AA.B_ptr` points. A similar situation occurs with the :code:`AA` —. If it goes out of scope, its managed object is not deleted either because :code:`BB.A_ptr` points to it.
This problem can be solved with a weak pointer.


.. code-block:: cpp
   
   struct A;

   struct B {
      std::shared_ptr<A> A_ptr;
      ~B() { std::cout << "~B()"; }
   };

   struct A {
      std::weak_ptr<B> B_ptr; // using weak_ptr instead of shared_ptr
      ~A() { std::cout << "~A()"; }
   };

   int main() {
      auto BB = std::make_shared<B>();
      auto AA = std::make_shared<A>();

      AA->B_ptr = BB;
      BB->A_ptr = AA;

      return 0;
   }

Now, both destructors are called when :code:`BB` goes out of scope. It can be destroyed because a weak pointer pointed to it and later, :code:`AA` can be destroyed because it is pointing to nothing. It doesn't matter whether :code:`AA` or :code:`BB` goes out of scope first. When :code:`BB` goes out of scope, it calls for the destruction of all managed objects, like :code:`A_ptr`.  So, even if :code:`AA` went out of scope first and was not destroyed, they will be destroyed together with :code:`BB`.
