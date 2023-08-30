SYCL Code Basic Elements
========================

SYCL offers a broad range of advantages to developers, including improved productivity, 
better performance, and enhanced code maintainability. In this lesson, students 
will gain an overall understanding of basic SYCL features and concepts. 

Most featured SYCL offerings
----------------------------

**1.** SYCL provides an **easier programming model for heterogeneous applications** than traditional models such as OpenCL or CUDA. 

**2.** SYCL **supports modern C++ language features** and can help simplify writing portable and maintainable code. 

**3.** SYCL allows developers to take advantage of heterogeneous hardware architectures and **utilize multiple processors or accelerators simultaneously**. 

**4.** SYCL provides an abstraction layer that makes it **easier to port code to different hardware** architectures. 

**5.** SYCL enables the development of **high-performance** and **data-parallel** applications. 

**6.** SYCL **allows third-party vendors to provide tools** that help optimize code for different hardware architectures. 

.. First parallel SYCL code:  [[this doesn't show up in Preview mode]]
.. -------------------------

Basic SYCL code: single_task
-----------------------------

Here we will use a very common SYCL code as the first approach to 
learn about the basic SYCL components.  The intent of this code is to modify only 
the 6th element of a 10-size vector using SYCL specification within C++:

.. // source: 'SYCL Parallelism Using parallel_for | Intel Software <https://www.youtube.com/watch?v=KConKN1olYI>'_

.. code-block:: cpp

    #include <CL/sycl.hpp>
    using namespace sycl;
    
    int main() {

        queue Q;                        // The queue, Q, is the object that
                                        // submits the task to the device
        int const size = 10;
        buffer<int> A{ size };          // The buffer, A, is the memory used to
                                        // transfer data between host and device
        
        Q.submit([&](handler& h) {      // The handler, h, is the object that contains 
                                        // the parallel_for function to be used
            
            accessor A_acc(A, h);       // The accessor, A_acc, is the object that
                                        // efficiently accesses the buffer elements
                                        
            h.single_task([=]() {
                A_acc[5] = 77; 
                });
            });

        host_accessor result(A);        // host_accessor is the object that allows 
                                        // the host to access the buffer memory

        for (int i = 0; i < size; i++)  // Print output
            std::cout << result[i] << " "; std::cout << "\n";
        return 0;

    }

The first object that it is necessary in the SYCL code is the **queue**, Q.  
The queue is the fundamental construct used to submit work, control the 
execution flow, and coordinate data transfers between the host and device
in a parallel and heterogeneous computing environment, such as CPUs or GPUs.

Next, we have to define the **buffer**, A, which is the data container that 
represents the region of memory that is accessible by the host and the device,
and it is used to share and transfer data.

The queue requires the use of the **command group**, which in the code above
is defined with:

.. code-block:: cpp

        Q.submit([&](handler& h) {

            ...

        }

The command group represents a unit of work that can be submitted to
a SYCL queue for execution; its main function is to define the
operations or computations that are to be performed on the target device.

The command group needs the **accessor**, A_acc,

.. code-block:: cpp

            accessor A_acc(A, h);

that is the object that efficiently accesses the buffer elements.

Inside of the command group as well, it resides the specific **SYCL kernel function**, 
which is **single_task** in this case. Note that single_task is provided
by the handler, h:

.. code-block:: cpp

            h.single_task([=]() {
                A_acc[5] = 77; 
            });

The **handler**, h, is the object that represents a context in which command
groups are defined.  It specifies the operations and dependencies 
within a command group and controls the execution behavior of those operations.

One consideration to keep in mind is that only one SYCL kernel function, even if 
it is the same, can be executed in the command group. The **kernel code** in this case is:

.. code-block:: cpp

                A_acc[5] = 77;

Note that a lambda function can be used as kernel code as well.

**Source**: https://www.youtube.com/watch?v=KConKN1olYI&t=1s

.. // source: 'SYCL Parallelism Using parallel_for | Intel Software <https://www.youtube.com/watch?v=KConKN1olYI>'_



Basic SYCL code: parallel_for Hands-on 
--------------------------------------

To become familiar with of the SYCL structure, we propose 
the following hands-on exercise:  **Create a variation of the above single_task code
that changes all elements of the 10-size vector with the value 77 using 
a SYCL kernel function parallel_for instead of using single_task.**

**Hint**: Since the loop has to be a SYCL kernel function, we can use the parallel_for
function provided by the handler, h.

.. code-block:: cpp

    #include <CL/sycl.hpp>
    using namespace sycl;
    
    int main() {

        queue Q;                        // The queue, Q, is the object that
                                        // submits the task to the device
        int const size = 10;
        buffer<int> A{ size };          // The buffer, A, is the memory used to
                                        // transfer data between host and device
    


    //********** YOUR CODE STARTS HERE **********//

    // Step 1) Submit the queue with the handler definition:
    
    // Step 2) Define the accessor with buffer and handler:
    
    // Step 3) Call parallel_for from the handler specifying range and index:
    
    // Step 4) Change the accessor elements with the desired value using the index:
    

    //********** YOUR CODE ENDS HERE **********//



        host_accessor result(A);        // host_accessor is the object that allows 
                                        // the host to access the buffer memory

        for (int i = 0; i < size; i++)  // Print output
            std::cout << result[i] << " "; std::cout << "\n";
        return 0;

    }

The solution to this parallel_for hands-on exercise is in the next section.


Main SYCL concepts takeaways
----------------------------

To recap, these are the main concepts introduced in this section and
collectively provide a framework for expressing parallelism,
managing data transfers, and controlling the execution of workloads
in SYCL programs to enable efficient execution on heterogeneous platforms.

- **Queue**: A SYCL queue manages the execution of command groups on a specific device. It acts as a command queue, allowing you to submit command groups for execution and control the order of execution.

- **Scheduler**: The scheduler in SYCL is an internal component of the runtime system that manages the execution and scheduling of command groups on devices. It optimizes the execution by considering device capabilities, workload distribution, dependencies, and resource availability. The queue is the primary interface through which tasks are submitted to the scheduler for execution.

- **Buffer**: A buffer in SYCL is a data container that represents a region of memory accessible by both the host and the device. It enables efficient data transfer and sharing between the host and the device without explicit memory management.

- **Command group**: In SYCL, a command group represents a unit of work that is submitted for execution on an OpenCL device. It encapsulates a set of operations and allows you to express parallelism and dependencies between tasks. Remember to call only a SYCL kernel function per command group.

- **Handler**: A handler in SYCL represents a context in which command groups are defined. It provides methods for specifying operations within a command group, such as kernel invocations and memory transfers, and controls the execution behavior of those operations.






.. SYCL example #2: vector_add    [[this part doesn't show up in preview mode]]
.. ---------------------------

.. .. code-block:: cpp

..     #include <sycl/sycl.hpp>
..     #include <vector>
..     #include <string>
..     using namespace sycl;
                                                        
..     size_t num_repetitions = 1;             // Times to repeat the kernel invocation
..     size_t vector_size = 10000;             // Vector type and data size for this example
..     typedef std::vector<int> IntVector; 

..     void VectorAdd(queue &q, const IntVector &a_vector, const IntVector &b_vector,
..                 IntVector &sum_parallel) {

..     range<1> num_items{a_vector.size()};    // Range object for vectors managed by the buffer

..     buffer a_buf(a_vector);                             // Create buffer a_buf
..     buffer b_buf(b_vector);                             // Create buffer b_buf
..     buffer sum_buf(sum_parallel.data(), num_items);     // Create buffer sum_buf

..     for (size_t i = 0; i < num_repetitions; i++ ) {     // Loop for the number of additions

..         q.submit([&](handler &h) {
..         accessor a(a_buf, h, read_only);                // Create accesor for a_buf
..         accessor b(b_buf, h, read_only);                // Create accesor for b_buf
..         accessor sum(sum_buf, h, write_only, no_init);  // Create accesor for sum_buf
    
..         h.parallel_for(num_items, [=](auto i) { sum[i] = a[i] + b[i]; });

..         });
..     };
    
..     q.wait();                                           // Wait until compute task is done
..     }


..     int main(int argc, char* argv[]) {

..     IntVector a, b, sum_sequential, sum_parallel;
..     a.resize(vector_size);
..     b.resize(vector_size);
..     sum_sequential.resize(vector_size);
..     sum_parallel.resize(vector_size);

..     InitializeVector(a);        // Initialize input vector a with values from 0
..     InitializeVector(b);        // Initialize input vector b with values from 0

..     try {
..         queue q(selector, exception_handler);
..         VectorAdd(q, a, b, sum_parallel);       // Call to the VectorAdd SYCL function
..     } 

.. **Note**: For teaching purposes, this code has been simplified.
.. For more details about this code sample visit (https://www.intel.com/content/www/us/en/developer/articles/code-sample/vector-add.html)



.. Backup
.. As an example of **how easy it is to create a parallel task in SYCL**, below there is a comparison between, **a)**, a regular for loop in only C++ and **b)**, a parallel_for in SYCL:

.. **a) C++** (sequential):

.. .. code-block:: cpp

..     #include <iostream>
..     #include <vector>

..     int main() {

..         std::vector<int> myVector(10);      // Creating a vector of size 10//

..         int valueToAdd = 77;                // Value to be added
                                        
..         for (int i = 0; i < myVector.size(); ++i) {
..             myVector[i] += valueToAdd;      // Adding the value to each element
..         }

..         for (int i = 0; i < myVector.size(); ++i) {
..             std::cout<<myVector[i]<<" ";    // Printing vector elements
..         }
..         std::cout << std::endl;
..         return 0;
..     }
