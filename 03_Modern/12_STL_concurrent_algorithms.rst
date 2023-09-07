Standard Template Library (STL) on Concurrent and Parallel Algorithms
#######################################################################

This chapter talks about concurrent and parallel STL algorithms. You will learn the following:

#. What are STL algorithms? 
#. What execution policies are available as part of STL?
#. How are different execution policies used?
#. What are the benefits and drawbacks of using specific execution policies?
#. What are the best practices when using concurrent and parallel STL algorithms?

Introduction
************

The Standard Template Library (STL) offers over 150 algorithms including ones that run sequentially. To take advantage of the capabilities of many cores, programmers must parallelize these libraries using the low-level concurrency APIs, which is not easy.  Fortunately, since C++17, most of the STL algorithms are parallelized and support for vectorization has been added.  

What are STL Algorithms?
****************************

STL algorithms are a set of powerful functions offered by the C++ Standard Library that enable the execution of various operations on data containers such as vectors, lists, and arrays. These algorithms are designed to be very effective and generic, making them ideal for a wide range of applications.  STL techniques can be used to help avoid repeatedly implementing simple functions, and instead focus on addressing higher-level problems.  Examples of algorithms available within the STL include :code:`std::find`, :code:`std::sort`, and :code:`std::replace`. These algorithms can drastically improve the efficiency and readability of the code. 

Execution Policies
*******************

To use the parallel algorithms from STL, you need to include the :code:`<execution>` header. The next step is to invoke the chosen algorithm with an execution policy, which allows you to specify how the algorithm should be executed. In C++, the following execution policies are available:

* sequenced_policy (and the corresponding global object :code:`std::execution::seq`) — sequential execution of the algorithm. 
* parallel_policy (and the corresponding global object :code:`std::execution::par`) — parallel execution of the algorithm.
* parallel_unsequenced_policy (and the corresponding global object :code:`std::execution::par_unseq`) — parallel execution of the algorithm with the ability to use vector instructions.
* unsequenced_policy (and the corresponding global object :code:`std::execution::unseq`) — execution of the algorithm with the ability to use vector instructions.

Let's see examples of the use of all the policies. 

.. note::

   We will be using small sets of data just to show how the policies work, but remember that the benefits of using policies usually comes from dealing with large amounts of data.

sequenced_policy
=================

For sequenced_policy, we will use the :code:`std::sort` algorithm.

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

Using sequenced_policy has several advantages that include the following:

* It is ideal for small tasks (when the parallel overhead doesn't exist)
* Data races can be avoided
* It is simple and predictable.

At the same time, sequenced_policy is not efficient for large tasks with a lot of data. 

parallel_policy
================

For parallel_policy, we will use the :code:`std::find` algorithm.

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

When using parallel_policy, we can benefit from the following:

* Faster execution for larger tasks and on larger datasets.
* Optimal usage of multi-core systems.

At the same time, it is important to remember that:

* It may introduce overhead, and if that's the case, it is not always faster than sequential execution.
* It is the programmer's responsibility to avoid data races and deadlocks.


parallel_unsequenced_policy
=============================

For parallel_unsequenced_policy, we used the :code:`std::transform` algorithm with a prepared lambda function that returns a number squared. It's important to understand that the result can be every permutation of {1, 4, 9, 16, 25} as the operations are performed nonsequentially.

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

Here, similar to the parallel_policy, we can:

* Realize faster execution for repetitive operations.
* Benefit from using hardware with vector instructions.

On the other hand, we need to remember that it is not suitable for all tasks (e.g., tasks where the order of operations is important).

unsequenced_policy
====================

For the last policy — unsequenced_policy — we are using the  :code:`std::for_each` algorithm:

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

Using unsequenced_policy, we can:

* Experience fast execution on a single thread.
* Avoid race conditions.

At the same time, the execution of the sequence is not deterministic, so we need to make sure that the order is not important for the task we are doing.

Best practices 
***************

To make the most of STL on concurrent and parallel algorithms, it's worth considering the following best practices:

#. **Choose the right algorithm** — The STL provides many different algorithms, so it is important to choose the right one and select the appropriate execution policy. Ensure that you fully understand the problem you want to solve.
#. **Profile your code** — It can be useful to profile your code to identify the performance bottlenecks. Remember that you can achieve the best results by optimizing the critical sections of the code.
#. **Minimize shared data** — Minimizing the amount of shared data allows you to reduce the chances of race conditions and synchronization overhead.

Summary
********

STL algorithms and concurrent programming approaches are useful additions to data scientists and software engineers' toolkits. Try it yourself and create the code that compares the performance of different execution policies on the same task. Remember to work on a large set of data. 
