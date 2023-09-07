Uniform Initialization
#######################

This chapter talks about uniform initialization. You will learn the following:

#.	What is uniform initialization and how can it be used?
#. Why should uniform initialization be used?
#. What are the common problems with uniform initialization? 

Introduction
************

In modern C++ there is a uniform method for initializing data called **uniform initialization**.

Expression Initialization 
=========================

To better understand the concept, let's get familiar with the following terms:

* **direct initialization**, which uses an explicit set of constructor arguments to create an object.
* **copy initialization**, which uses another object to initialize an object.

The code below shows both direct and copy initialization:

.. code-block:: cpp
   
   std::string direct("direct initialization");
   std::string copy = "copy initialization";

Brace-initialization
====================

To uniformly initialize objects of any type, **brace-initialization form {}** may be used for both direct and copy initialization. When used with brace-initialization, we call initializations, direct-list and copy-list. 

The code below shows both direct-list and copy-list initialization:

.. code-block:: cpp
   
   std::string direct{"direct-list initialization"};
   std::string copy = {"copy-list initialization"};

Let's look at uniform initialization on different build-in and custom types:

#. Build-in types:

   .. code-block:: cpp
   
      int i {13};
      float f {2.7};

#. Arrays:

   .. code-block:: cpp

      int my_array[5] {0, 1, 2, 3, 4};

#. Dynamically allocated arrays:

   .. code-block:: cpp

      int* my_array = new int[5]{0, 1, 2, 3, 4};

#. Standard library containers:

   .. code-block:: cpp

      std::vector<int> my_vector{0, 1, 2, 3, 4};
      std::map<int, std::string> my_map{{1, "str1"}, {7, "str2"}};

#. User-defined types:

   .. code-block:: cpp

      class foo{
         public:
            foo() : _i(0), _f(0.0) {}
            foo(int i, float f) : _i(i), _f(f) {}

         private:
            int _i;
            float _f;
      };

      foo f1{};
      foo f2{13, 2.7};

Why should uniform initialization be used?
*******************************************

Within the uniform initialization, we can list several advantages. 

Consistent syntax
=================

The first is **very consistent syntax**.
To exemplify, we already know there are many ways to initialize the variable.

.. code-block:: cpp

   int i = 1;   // historically the most common way
   int i(1);    // direct initialization
   int i{1};    // direct-list initialization
   int i = {1}; // copy-list initialization
   auto i{1};   // direct initialization of type deduced to int 

For simple type initialization, it's not a problem to use the most common method. However, when we use different, more complicated custom types, the consistent syntax can change the experience with code. This can be especially important if you consider the generic code that should be able to initialize any type — it will be not possible with :code:`()` initialization.

.. code-block:: cpp

   int i{1};
   foo f{13, 2.7};
   std::vector<int> v{0, 1, 2, 3, 4};
   std::unordered_set<int> s{13, 17, 8};
   std::unordered_map<int, std::string> {{1, "one"}, {2, "two"}};


Narrowing conversions are not allowed
=====================================

The second benefit is that uniform initialization **does not allow narrowing conversions**.

Before uniform initialization, with C-style C++, the code below will work, and :code:`double` will just convert to :code:`int`.

.. code-block:: cpp

   double d = 5.5;
   int i = d; // double to int conversion 

The same with bracket initialization will not work and it forces the user to type-cast values explicitly.

.. code-block:: cpp

   int i{d}; // compilation error

   int i{static_cast<int>(d)}; // modern C++ cast - best practice
   int i{(int)d};              // C-style type-cast
   int i{int(d)};              // old C++-style type-cast


Fixes most Vexing Parse
=======================

The most vexing parse comes from a rule in C++ that says that anything that could be considered a function declaration should be parsed by the compiler as a function declaration.

Let's examine the example when we want to initialize the vector that's a private member of the foo class 
with three zeros :code:`{0, 0, 0}`,

.. code-block:: cpp

   class foo{
      public:
         foo() { ... }

      private:
         std::vector<int> v(3, 0); 
   };

This code will not compile because the vector initialization was interpreted by the compiler as a function declaration. We have three possible solutions for this problem. 

The first is the most obvious — we can just use uniform initialization for the vector.

.. code-block:: cpp

   std::vector<int> v{0, 0, 0};

This is not always the best solution, especially when we need to initialize the long vector and typing every element is not an option.

The second solution is to move the initialization to the constructor:

.. code-block:: cpp

   foo() : v(3, 0) { ... }

And the last solution is to use copy initialization:

.. code-block:: cpp

   std::vector<int> v = std::vector<int>(3, 0);



Common problems with uniform initialization 
*******************************************

Even when the uniform initialization helps with a lot of problems in C++, there are also some issues related to using it. The first of them is about using :code:`auto` for variable declaration. Deduced type for the variable can be :code:`std::initializer_list` instead of the type a programmer would expect. This happens mostly when we combine auto variable declaration with an equal sign or if it has multiple elements, like in the code shown below: 

.. code-block:: cpp

   auto variable{13};       // variable is type of int
   auto variable = {13};    // variable is of type std::initializer_list<int>

   auto variable{13, 17, 8};    // compilation error variable contains multiple expressions
   auto variable = {13, 17, 8}; // variable is of type std::initializer_list<int>

Another problem can happen with the vector initialization. It can be tricky, especially when a programmer is learning C++. See the difference between declarations below:

.. code-block:: cpp

   std::vector<int> v(3,0); // vector contains tree zeros {0, 0, 0}
   std::vector<int> v{3,0}; // vector contains three and zero {3, 0}

The last problem can be called "strongly prefer :code:`std::initializer_list` constructors." It means that when calling the constructor using the uniform initialization syntax, the constructor will overload while declaring its parameter of type :code:`std::initializer_list` (when it exists).

The example below demonstrates this situation:

.. code-block:: cpp

   class foo {
      public:
         foo(int i, float f) { ... }
         foo(std::initializer_list<bool> list) { ... }
   };

   foo object{13, 2.7}; // compilation error

The error occurs because instead of using the first constructor (with :code:`int` and :code:`float`), there is the constructor overload to the "strongly preferred" one with :code:`std::initializer_list` as a parameter. So, the problem is caused by narrowing conversions from :code:`int` and :code:`double` to :code:`bool`. 
