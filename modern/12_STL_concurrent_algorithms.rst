Standard Template Library(STL) on concurrent & parallel algorithms
##################################################################

This chapter talks about concurrent and parallel STL algorithms. You will learn:

#. What STL algorithms are? 
#. What are the execution policies available as art of STL?
#. How to use different execution policies?
#. What are the benefits and drawbacks of using specific execution policies?
#. What are the best practices when using concurrent and parallel STL algorithms?

Introduction
************

The Standard Template Library (STL) offers over 150 algorithms. They are algorithms that run 
sequentially. And to take advantage of the capabilities of many cores, programmers must parallelize 
these libraries using the low-level concurrency APIs which is not easy.

Fortunately, since C++17 most of the STL algorithms are parallelized and there is a vectorization 
support added.

What are the STL algorithms
****************************

STL algorithms are a set of powerful functions offered by the C++ Standard Library that allow you to
execute various operations on data containers such as vectors, lists, and arrays. These algorithms 
are designed to be very effective and generic, making them best for a wide range of applications. 
By use of STL techniques, you may avoid implementing simple functions all over again and instead 
focus on addressing higher-level problems.

Examples of algorithms available within the STL include :code:`std::find`, :code:`std::sort`, 
:code:`std::replace`. Using those algorithms can drastically improve the efficiency and readability 
of the code.

Execution policies
*******************

To be able to use the parallel algorithms from STL, you need to include the :code:`<execution>` 
header. The next step is to invoke the chosen algorithm with an execution policy. The execution 
policy allows you to specify how the algorithm should be executed. In C++ there are available 
following execution policies:

* sequenced_policy (and the corresponding global object :code:`std::execution::seq`) - sequential 
  execution of the algorithm 
* parallel_policy (and the corresponding global object :code:`std::execution::par`) - parallel 
  execution of the algorithm
* parallel_unsequenced_policy (and the corresponding global object :code:`std::execution::par_unseq`) - 
  parallel execution of the algorithm with ability to use vector instructions.
* unsequenced_policy (and the corresponding global object :code:`std::execution::unseq`) - execution
  of the algorithm with ability to use vector instructions.

Let's see the usage of all the policies in examples. 

.. note:: 
   We will be using small sets of data just to show how the policies works but remember 
   that the benefits of using policies usually came from dealing with large amount of data.

sequenced_policy
=================

For sequential policy we will use :code:`std::sort` algorithm.

.. code-block:: cpp
   
   #include <algorithm>
   #include <iostream>
   #include <vector>
   #include <execution>

   int main(){
      // container creation with unsorted elements
      std::vector<int> vec {7, 13, 4, 2, 56, 24, 1};

      // using std::sort on the prepared container vec with sequential execution policy
      std::sort(std::execution::seq, vec.begin(), vec.end());

      for(int i : vec) {
         std::cout << i << ' ';
      }
      return 0;
   }

Using sequential policy has several advantages that include:

* good for small task (when the parallel overhead doesn't exist),
* you can avoid data races,
* it is simple and predictable. 

At the same time sequenced_policy is not efficient for large tasks with a lot of data. 

parallel_policy
================

For parallel policy we will use :code:`std::find` algorithm.

.. code-block:: cpp
   
   #include <algorithm>
   #include <iostream>
   #include <vector>
   #include <execution>

   int main(){
      // container creation 
      std::vector<int> vec {7, 13, 4, 2, 56, 24, 1};

      // using std::find on the prepared container vec with parallel execution policy
      auto it = std::find(std::execution::par, vec.begin(), vec.end(), 4);

      if(it != vec.end()){
          std::cout << *it;
      }
      return 0;
   }

When using parallel_policy we can benefit form:

* faster execution for larger tasks and on the larger datasets,
* optimal usage of multi-core systems.

At the same time it is important to remember that:

* it may introduce overhead and it that case it is not always faster than sequential execution,
* it is the programmer's responsibility to avoid data races and deadlocks.


parallel_unsequenced_policy
=============================

For parallel_unsequenced_policy we decided to use :code:`std::transform` algorithm with prepared 
lambda function that returns a number squared. What is important, the result can be every 
permutation of the {1, 4, 9, 16, 25} as the operations are performed unsequentially.

.. code-block:: cpp
   
   #include <algorithm>
   #include <iostream>
   #include <vector>
   #include <execution>

   int main(){
      // container creation 
      std::vector<int> vec {1, 2, 3, 4, 5};

      // using std::transform on the prepared container vec 
      // with parallel unsequential execution policy
      std::transform(std::execution::par_unseq, 
        vec.begin(), 
        vec.end(), 
        vec.begin(), 
        [](int x){ return x*x; });

      for(int i : vec){
          std::cout << i << ' ';
      }
      return 0;
   }

Here, the same as in the parallel_policy, we have:

* faster execution for repetitive operations,
* taking benefit from hardware with vector instructions.

On the other hand, we need to remember that it is not suitable fo all tasks (e.g. for tasks where 
the order of operations is important).

unsequenced_policy
====================

For the lest policy - unsequenced_policy - we are using :code:`std::for_each` algorithm.

.. code-block:: cpp
   
   #include <algorithm>
   #include <iostream>
   #include <vector>
   #include <execution>

   int main(){
      // container creation 
      std::vector<int> vec {1, 2, 3, 4, 5};

      // using std::for_each on the prepared container vec 
      // with unsequential execution policy
      std::for_each(std::execution::unseq, 
        vec.begin(), 
        vec.end(), 
        [](int x){ std::cout << x << ' ';});

      return 0;
   }

Using unsequenced_policy we:

* have fast execution on a single thread,
* avoid race conditions.

At the same time the execution of the sequence is not deterministic, so we need to make sure that 
the order is not important for the task we are doing.

Best practices 
***************

To be able to make the most of STL on concurrent and parallel algorithms it is worth to take into 
consideration the following best practices:

#. **Chose the right algorithm** - the STL provides a lot of different algorithm so it is really 
   important to chose the right one and accordingly select the right execution policy. So, please 
   make sure you fully understand the problem you want to solve.
#. **Profile your code** - it can be really useful to profile your code to identify the performance 
   bottlenecks. Remember that you're able to achieve the best results optimizing the critical 
   sections of the code.
#. **Minimize shared data** - minimizing the amount of shared data allows to reduce the chances of 
   race conditions and synchronization overhead.

Summary
********

STL algorithms and concurrent programming approaches are useful additions to the toolkit of data 
scientists and software engineers. Try it yourself and create the code that compares the performance 
of different execution policies on the same task. Remember to work on the big set of data. 