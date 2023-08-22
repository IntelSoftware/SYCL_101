Move Semantics
#############################

This chapter talks about move semantics. You will learn:

#. What is move semantics?
#. What are different value categories and when to use them?
#. What is universal reference T&&?
#. How and why to use std::move?
#. How to create move constructor? (Rule of 5)

Introduction
************

Move semantics allows an object, under certain conditions, to take ownership of some other object's 
external resources.

Value categories (glvalue and rvalue)
**************************************

In C++ every expression has a type and belongs to specific **value category**. Those are some basic 
rules for compiler to follow when creating, copying and moving objects during expression evaluation.

Here are C++ expression value categories:
   
* **glvalues** - expressions that have an identity; possible to determine if two expressions refer 
  to the same entity
* **rvalues** - expressions that can be moved from
* **lvalues** - have an identity and can't be moved from
* **xvalues** - have an identity and can be moved from
* **prvalues** - don't have an identity and can be moved from

The diagram below shows different expression types and dependencies between them:

.. figure:: /_images/move-semantics-expressions.png

Let's take a look on the lvalue and rvalue in example.

.. code-block:: cpp
   
   size_t x = 0;
   x = 1; // x expression is l-value

   size_t foo() { /* ... */ }
 
   foo(); // Result of foo call expr is an r-value

Any name of variable, function, template parameter object or data member is an lvalue. What can be 
important, is that it doesn't matter how complex the expression is. As long as it maintains identity,
the expression is an lvalue.

The integer constants are *prvalues* like in the code above - result of function call.

Functions returning lvalue and prvalue
=======================================

Let's imagine function returning :code:`int` value, like below:

.. code-block:: cpp
   
   int returnValue() {
      return 3;
   }

In that case :code:`returnValue()` returns the temporary number :code:`3` which is un prvalue. Now, 
if we will try to assign the value to it, like shown:

.. code-block:: cpp
   
   returnValue() = 17; // error

we will receive un error: :code:`lvalue required as left operand of assignment`. Thats because we 
are trying to use left operand od assignment on prvalue. 

But when we change :code:`returnValue()` function to return a reference to already existing memory 
location, everything will work fine. See code below:

.. code-block:: cpp
   
   int globalValue = 43;

   int& returnValue() {
      return globalValue;
   }

   // ...
   
   returnValue() = 17; // works fine

And even though the ability to return lvalue may not seem intuitive, 
it can be useful when implementing more advanced functions like overloaded operators.

lvalue to prvalue conversion
============================

An lvalue may be converted to a prvalue. This is totally legal and occurs frequently. Let's look on 
:code:`+operator` as an example. According to C++ specification it takes two prvalues as arguments 
and returns an prvalue.
    
.. code-block:: cpp
   
   int x = 10, y=20;
   int z = x + y;
    
:code:`x` and :code:`y` are lvalues, but the addition operator wants prvalues. 
*How is it possible?* Because of an implicit lvalue-to-prvalue conversion. There are many more 
operators performing such conversion. 

But what about the opposite - converting prvalue to lvalue? It is not possible due to the C++ design.

Universal references (&&)
*************************

One of the main features related to the rvalues introduced in C++11 was rvalue reference. Usually 
the :code:`&&` notation is known as a sytnax for it. But it is not always true. 

:code:`T&&` can hold both lvalue and rvalue reference - which is called **universal reference**.
But remember that :code:`&&` only means a universal reference when type deduction is involved. In 
other cases we can assume that it means only an rvalue reference.

Let's see it in a code. We will start with universal reference - as the :code:`T` is deducted.

.. code-block:: cpp
   
   template<typename T>
   void foo(T&& param);

Now, let's move on to rvalue reference, as there is no type deduction.

.. code-block:: cpp
   
   void foo(std::string&& param);

And the last thing is to show concept of prefect forwarding, when universal reference can be 
propagated preserving the l-r 'valueness'. 

.. code-block:: cpp
   
   template<typename T>
   void foo(T&& param) { /* ... */ }
  
   template<typename T>
   void bar(T&& param) {
      foo(std::forward<T>(param)); // l or r value depending on the param passed to `bar`
   }

In that case as both functions :code:`foo` and :code:`bar` are using universal reference, :code:`foo` 
will receive a l or r value depending on the param passed to :code:`bar`.

std::move
**********

Let's start wth answering the question: What is :code:`std::move`?

According to C++ Reference:

   :code:`std::move` is used to indicate that an object t may be "moved from", i.e. allowing the 
   efficient transfer of resources from t to another object.
   
In other words it is a way to efficiently transfer contents of an object to another leaving the 
source in a valid but undefined state. We can say, that when you move a value from a register or 
memory location to another place, the value on the source register or memory location is still there.

An mor formally, :code:`std::move` is a C++ Standard Library function defined in the :code:`<utility>` 
header. It is used to cast an l-value reference to an r-value reference, which enables move semantics.

Let's see some example to better understand it. We will start with declaration of the function 
consuming the element.

.. code-block:: cpp
   
   void consume_element(std::unique_ptr<int> element);

Then, let's declare it and consume using prepared function and :code:`std:move`.

.. code-block:: cpp
   
   std::unique_ptr<int> element = std::make_unique<int>(30);
   consume_element(std::move(el));

After those operations, declared element :code:`element` is nullptr, as it was moved.

.. code-block:: cpp
   
   assert(element == nullptr);


Move constructor and rule of five 
*********************************

:code:`std::move` is actually just a request to move. If the type of the object has not 
a move constructor/assign-operator defined the move operation will fall back to a copy. 
In that case we will not experience any benefits of using move operation.

That is why it is important to know how to create move constructor. At the same time 
in C++ we have something called **rule of five**, which follows:

#. If a class requires a user-defined destructor, a user-defined copy constructor, or a user-defined 
#. copy assignment operator, it almost certainly requires all three.
#. Any class for which move semantics are desirable, has to declare also the move constructor and 
#. the move assignment operator

Let's show it in the example. Imagine class called :code:`MoveClass` with private member called 
:code:`str_ptr` being :code:`char*`. To show rule of five we need to declare:

* custom destructor,
* custom copy constructor,
* custom move constructor,
* custom copy assignment operator,
* custom move assignment operator.

.. code-block:: cpp
   
   class MoveClass {
      char* str_ptr; 

   public:
      explicit MoveClass(const char* s = "") : str_ptr(nullptr) {
         if (s) {
            std::size_t size = std::strlen(s) + 1;
            str_ptr = new char[size];      // allocate
            std::memcpy(str_ptr, s, size); // populate 
         }
      }

      // Destructor - we need to deallocate str_ptr
      ~MoveClass() {
         delete[] str_ptr; 
      }

      // Copy constructor - uses explicit constructor, parameter passed is const&
      MoveClass(const MoveClass& other) 
         : MoveClass(other.str_ptr) {}

      // Move constructor - uses std::exchange function, parameter passed is &&
      MoveClass(MoveClass&& other) noexcept
         : std_ptr(std::exchange(other.str_ptr, nullptr)) {}

      // Copy assignment operator - uses copy constructor, 
      // passed parameter similarly to copy constructor is const&
      MoveClass& operator=(const MoveClass& other) {
         return *this = MoveClass(other);
      }

      // Move assignment operator - uses std::swap function, 
      // passed parameter similarly to copy constructor is &&
      MoveClass& operator=(MoveClass&& other) noexcept {
         std::swap(str_ptr, other.str_ptr);
         return *this;
      }
   };
