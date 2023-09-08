std::for_each in Parallel
#########################

This chapter talks about for_each. You will learn the following:

#. What is a *std::for_each* expression?
#. How can a *std::for_each* be used in C++ code?
#. What kind of parallelization can be used with *std::for_each*?


Introduction
************

**std::for_each** is a commonly used algorithm in C++ that allows you to iterate over elements in a range and apply a specified operation or function to each element. It is part of the C++ Standard Library's header and provides a convenient and expressive way to perform actions on every element in a collection without having to write explicit loops. The equivalent of std::for_each in SYCL is **parallel_for**.

Parallelization with execution policies
***************************************

To make the operation run in parallel it is necessary to use an execution policy inside of std::for_each. In the code below we use the **std::execution::par_unseq** execution policy to parallelize the square of the vector index on multi-core processors over the range of the vector length:

.. code-block:: cpp

    #include <iostream>
    #include <vector>
    #include <execution>

    int main() {

        std::vector<int> v(100);
        
        // Initialize the vector with increasing values.
        for (int i = 0; i < v.size(); i++) {
            v[i] = i;
        }

        // Parallelize the for loop using the `std::execution::par_unseq` policy.
        std::for_each(std::execution::par_unseq, v.begin(), v.end(), [](int i) {
            
            int square = i * i;
            result[i] = square;

        });

        // Print the modified vector
        for (const auto& i : result) {
            std::cout << i << " ";
        }

        std::cout << std::endl;

        return 0;
    }

In this example, the std::for_each algorithm is used to iterate over the elements of the v vector. The first argument to the std::for_each algorithm is the execution policy, which specifies how the loop should be executed. In this case, the std::execution::par_unseq policy is used, which tells the compiler to execute the loop in parallel, but not to reorder the iterations.

The std::execution header file defines a number of different execution policies, which can be used to control the parallelism of a program. The std::execution::par_unseq policy is a good choice for loops that do not depend on the order of the iterations.

There are four types of execution policies inside of the execution class:

* **execution::seq** or sequenced_policy: This policy enforces strict sequential execution. Algorithms using this policy will execute sequentially, one element at a time, without any parallelism. There are no guarantees about the order in which elements are processed unless specified by the algorithm itself.

* **execution::par** or parallel_policy: This policy is designed for parallel execution. Algorithms using this policy will attempt to execute in parallel if possible, utilizing multiple threads or cores to process elements concurrently. The order in which elements are processed is not guaranteed.

* **execution::par_unseq** or parallel_unsequenced_policy: This policy is similar to std::execution::parallel_policy, as it allows for parallel execution, but it also provides more freedom for the compiler and runtime to optimize and reorder operations. This policy can result in more aggressive optimizations, possibly sacrificing some determinism in the order of operations.

* **execution::unseq** or unsequenced_policy: This policy provides maximum freedom for the compiler and runtime to optimize and reorder operations. It doesn't guarantee any specific order of execution, and it may even execute operations in an entirely unpredictable manner. This policy is typically used for low-level, performance-critical code when you want to allow aggressive compiler optimizations.

In summary, the choice of which policy to use depends on specific requirements for performance, determinism, and the behavior of the algorithm. In most cases, you'll use sequenced_policy for serial execution, and parallel_policy for parallel execution when order doesn't matter. The other policies are used when you need to fine-tune performance and are aware of the trade-offs involved.
