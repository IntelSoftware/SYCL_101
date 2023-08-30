Move Semantics
#############################

This chapter talks about move semantics. You will learn the following:

#. What is move semantics?
#. What are the different value categories and when should they be used?
#. What is universal reference T&&?
#. How and why should std::move be used?
#. How is a move constructor created? (Rule of Five)[[[based on later uses I changed to "Rule of Five" here. Also made it a proper noun because it looks cool.]]]

Introduction
************

Move semantics allows an object, under certain conditions, to take ownership of some other object's 
external resources.

Value categories (glvalue and rvalue)
**************************************

In C++, every expression has a type and belongs to a specific **value category**. These are the basic 
rules for a compiler to follow when creating, copying, and moving objects during expression evaluation.

Here are some C++ expression value categories:[[[below, I made all "values" singular and adjusted the verbs.]]]
   
* **glvalue** — Expression that has an identity; it's possible to determine if two expressions refer 
  to the same entity.
* **rvalue** — Expression that can be moved from.
* **lvalue** — Has an identity and can't be moved from.
* **xvalue** — Has an identity and can be moved from.
* **prvalue** — Doesn't have an identity and can be moved from.

The diagram below shows different expression types and the dependencies between them.

.. figure:: /_images/move-semantics-expressions.png

Let's look at the lvalue and rvalue in the following example.

.. code-block:: cpp
   
   size_t x = 0;
   x = 1; // x expression is l-value

   size_t foo() { /* ... */ }
 
   foo(); // Result of foo call expr is an r-value

Any name of variable, function, template parameter object, or data member is an lvalue. It's important to note that it doesn't matter how complex the expression is. As long as it maintains an identity,
the expression is an lvalue.

The integer constants are *prvalues*, like in the code above — the result of a function call.

Functions returning lvalue and prvalue
=======================================

Let's imagine a function returning a :code:`int` value, like below:

.. code-block:: cpp
   
   int returnValue() {
      return 3;
   }

In this case, :code:`returnValue()` returns the temporary number :code:`3`, which is a prvalue. Now, 
we will try to assign the value to it, as shown below:

.. code-block:: cpp
   
   returnValue() = 17; // error

We will receive an error: :code:`lvalue required as left operand of assignment`. That's because we 
are trying to use the left operand of the assignment[[[edit accurate?]]] on prvalue. 

But when we change the :code:`returnValue()` function to return a reference to an already existing memory 
location, everything will work fine. See the code below:

.. code-block:: cpp
   
   int globalValue = 43;

   int& returnValue() {
      return globalValue;
   }

   // ...
   
   returnValue() = 17; // works fine

And even though the ability to return an lvalue may not seem intuitive, 
it can be useful when implementing more advanced functions like overloaded operators.

lvalue-to-prvalue conversion
============================

An lvalue may be converted to a prvalue. This is totally legal and occurs frequently. Let's look at 
:code:`+operator` as an example. According to the C++ specification, it takes two prvalues as arguments 
and returns a prvalue.
    
.. code-block:: cpp
   
   int x = 10, y=20;
   int z = x + y;
    
:code:`x` and :code:`y` are lvalues, but the additional operator wants prvalues. 
*How is it possible?* Because of an implicit lvalue-to-prvalue conversion. There are many more 
operators performing similar conversions. 

But what about the opposite — converting prvalue to lvalue? It is not possible due to the C++ design.

Universal references (&&)
*************************

One of the main features related to the rvalues introduced in C++11 was rvalue reference. Usually, 
the :code:`&&` notation is known as a sytnax for it.[[[syntax for what? rvalue reference?]]] But it is not always true. 

:code:`T&&` can hold both lvalue and rvalue references, which is called a **universal reference**.
But remember that :code:`&&` only means a universal reference when type deduction is involved. In 
other cases, we can assume that it means only an rvalue reference.

Let's see it in code. We will start with a universal reference, as the :code:`T` is deducted.

.. code-block:: cpp
   
   template<typename T>
   void foo(T&& param);

Now, let's move on to an rvalue reference, as there is no type deduction.

.. code-block:: cpp
   
   void foo(std::string&& param);

Finally, the last thing is to show the concept of prefect forwarding, which is when a universal reference can be 
propagated, preserving the l-r 'valueness.' 

.. code-block:: cpp
   
   template<typename T>
   void foo(T&& param) { /* ... */ }
  
   template<typename T>
   void bar(T&& param) {
      foo(std::forward<T>(param)); // l or r value depending on the param passed to `bar`
   }

In this case, since both functions :code:`foo` and :code:`bar` are using a universal reference, :code:`foo` 
will receive an l or r value, depending on the param passed to :code:`bar`.

std::move
**********

Let's start by answering the question: What is :code:`std::move`?

According to C++ Reference:

   :code:`std::move` is used to indicate that an object t may be "moved from" (i.e., allowing the 
   efficient transfer of resources from t to another object).
   
In other words, it is a way to efficiently transfer contents of an object to another, leaving the 
source in a valid but undefined state. When you move a value from a register or 
memory location to another place, the value on the source register or memory location is still there.

And more formally, :code:`std::move` is a C++ Standard Library function that's defined in the :code:`<utility>` 
header. It is used to cast an l-value reference to an r-value reference, which enables move semantics.

Let's see an example. We will start with a declaration of the function 
consuming the element.

.. code-block:: cpp
   
   void consume_element(std::unique_ptr<int> element);

Then, let's declare it and consume using a prepared function and :code:`std:move`.

.. code-block:: cpp
   
   std::unique_ptr<int> element = std::make_unique<int>(30);
   consume_element(std::move(el));

After those operations, the declared element :code:`element` is nullptr, as it was moved.

.. code-block:: cpp
   
   assert(element == nullptr);


Move constructor and Rule of Five 
*********************************

:code:`std::move` is actually just a request to move. If the type of the object does not have[[[I guessed here, please confirm accuracy]]] 
a move constructor/assign-operator defined, the move operation will fall back to a copy. 
In that case, we will not experience any benefits of using the move operation.

That is why it is important to know how to create a move constructor. At the same time, 
in C++ we have something called **Rule of Five**, which is as follows:[[[I don't get the Rule of 5. there are 4 bullets, and 1&2 are 1 sentence, and 3&4 are another sentence. what are the numbered 1-4? I guess it is what it is.]]]

#. If a class requires a user-defined destructor, a user-defined copy constructor, or a user-defined 
#. copy assignment operator, it almost certainly requires all three.
#. Any class for which move semantics are desirable, it also needs to declare the move constructor and 
#. the move assignment operator.

Let's show it in the example. Imagine a class called :code:`MoveClass` with a private member called 
:code:`str_ptr` being :code:`char*`. To show the Rule of Five, we need to declare the following:

* custom destructor
* custom copy constructor
* custom move constructor
* custom copy assignment operator
* custom move assignment operator

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
