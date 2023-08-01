Lambdas
#######

This chapter talks about lambdas. You will learn:

#. What is C++ lambda expression?
#. What are the parts of lambda?
#. How to use lambda expression in C++ code?

Introduction
************

**C++ lambda expression** - often called a lambda - allows us 
to define anonymous function objects (functors) which can be 
used inline or passed as an argument. This was introduces in C=++11
as a more convenient and concise way for creating anonymous functors.

Let's take a look at the few simple lambdas examples:

.. code-block:: cpp
   
   // Simple lambda printing string
   [] { std::cout << "Simple lambda\n"; };

   // Simple lambda returning sum of 2 elements
   auto lambda_sum = [](int x, int y){ return x + y; };
   
   // Simple lambda for sorting elements of the vector using std::sort
   std::vector<int> vec{23, 1, 2, 44, 56, 37, 4, 9, 0};
   std::sort(vec.begin(), vec.end(), [](int a, int b) { return a > b; });


Parts of lambda expression
**************************

There are six basic parts of lambda expression:

#. capture clause,
#. parameter list - *optional*,
#. mutable specification - *optional*,
#. exception specification - *optional*,
#. trailing-return-type - *optional*,
#. lambda body.

Image below shows them in a practical example:

.. figure:: /_images/lambda-expression.png

Capture clause
==============

Also known as **capture list** or **lambda-introducer**. It is the beginning of the 
lambda expression and specifies which variables are captured, and whether the capture 
is by value or by reference. Examples of capture clause are:

* :code:`[]` - capture nothing,
* :code:`[=]` - capture local objects like variables and parameters by value,
* :code:`[&]` - capture local objects like variables and parameters by reference,
* :code:`[this]` - capture :code:`this` by reference,
* :code:`[a, &b]` - capture objects :code:`a` by value and :code:`b` by reference.

Let's see them in an example code.

.. code-block:: cpp
   
   int number = 7;
   
   // Lambda returning vale of number by using [=]
   auto getNumber =  [=] { return number; };
   getNumber(); // returns 7

   // Lambda returning sum of number and passed argument as a value by using [=]
   auto addNumbers = [=](int y) { return number + y; };
   addNumbers(6); // returns 13 (7+6=13)

   // Lambda returning reference to the number by using [&]
   auto getReference = [&]() -> int& { return number; };
   getReference(); // returns int& to number

There is also a feature called **generalized capture**. Thanks to it we can introduce and initialize new 
variables in the capture cause, without the need to have those variables exist in the lambda function's 
enclosing scope. The type of the variable is deducted from the type produced by the expression.

This feature is really useful when we want to use in lambda move-only variables from the surrounding scope.
See the code below:

.. code-block:: cpp
   
   auto ptr = std::make_unique<int>(8);

   // Lambda using generalized capture
   auto lambda = [capturedValue = std::move(ptr)] { /* use ptr*/ };

Parameter list
==============

Lambdas can both capture variables and accept *input parameters*. A **parameter list** is optional and in 
most aspects resembles the parameter list for a function. Let's see the same simple code in a form of 
function and lambda expression.

.. code-block:: cpp
   
   int add(int x, int y) {
      return x + y;
   }

   auto lambdaAdd = [](int x, int y) { return x + y; };

In lambdas there is also possibility to use :code:`auto` keyword as the type specifier in a parameter list it 
it the type is generic. It can also take another lambda expression as an argument.

.. code-block:: cpp
   
   auto lambdaAdd = [](auto x, auto y) { return x + y; };

Mutable specification
======================

By default, value-captures cannot be modified inside the lambda because the compiler-generated method is 
marked as :code:`const`, but use of the :code:`mutable` keyword cancels this out. Which means that the 
**mutable specification** enables the body of a lambda expression to modify variables that are captured by 
value.

.. code-block:: cpp
   
   int number = 7;

   // number is reference, so the lambda modifies original
   auto lambdaReference = [&number] { number = 2; }; 
   
   // Error - lambda can perform const-only operations on number
   auto lambdaValue = [number] { number = 2; }; 

   // Due to usage of mutable lambda can modify number
   auto lambdaMutable = [number] () mutable { number = 2; };

Exception specification
=======================

You can specify that the lambda will not throw any exception using :code:`noexcept` keyword. You can see what 
will happen if you will run the code below.

.. code-block:: cpp
   
   []() noexcept { throw 13; } ;

Most of the C++ compilers should show the warning during compilation, but other than that the code will not 
throw the exception.

Return type
===========

In general, the returned type of the lambda expression is automatically deducted ant there is no need of 
using :code:`auto` keyword for that, like shown below:

.. code-block:: cpp
   
   []() { std::cout << "Sample output.\n"; }; // deduced type of the lambda is void

You can specify **trailing-return-type** that resembles the return-type part  of standard function. But 
please remember that it must follow the parameter list (even if it is empty) and you must use :code:`->` 
keyword before the return type.

.. code-block:: cpp
   
   // lambda returning int as trailing-return-type specifies
   []() -> int { return 13; };

You can omit the return-type part of a lambda expression if the lambda body contains just one return 
statement. Or, if the expression doesn't return a value.

.. code-block:: cpp
   
   // lambda returning int as deduced type from the single return statement
   [](int x) { return x; }(7);

Lambda body
===========

As the lambda expression is the same as the ordinary function, its body can contain anything that's allowed 
in function body. It means that lambda body, similarly as function body, can access:

* captured variables from the enclosing scope,
* parameter,
* locally declared variables,
* class data members (when lambda is declared inside a class and :code:`this` is captured),
* variables with static storage duration (like global variables).

Let's take a look at the code example. We would like to print the elements of declared vector together with 
information if the number is even or odd. The vector declaration is as followed:

.. code-block:: cpp
   
   std::vector<int> v {1, 2, 3, 4};

And now, we can prepare the function printing number and information :code:`is even` or :code:`is odd`.

.. code-block:: cpp
   
   // lambda returning int as deduced type from the single return statement
   void isEvenOrOdd(int n){
      std::cout << n;

      if (n % 2 == 0) {
         std::cout << " is even\n";
      } else {
         std::cout << " is odd\n";
      }
   }

To use this function on the vector elements we are using :code:`for_each` function form algorithms library.

.. code-block:: cpp
   
   for_each(v.begin(), v.end(), isEvenOrOdd);

The same result we can achieve using lambda-expression instead of :code:`isEvenOrOdd` function:

.. code-block:: cpp
   
   for_each(v.begin(), v.end(), [](int n) {
      std::cout << n;

      if (n % 2 == 0) {
         std::cout << " is even\n";
      } else {
         std::cout << " is odd\n";
      }
   });

As we can see, there is no limitations related to the size of the lambda. The only thing that may 
limit us is the readability of the code and the fact that lambdas are typically used as minor helper 
functions in our code.
