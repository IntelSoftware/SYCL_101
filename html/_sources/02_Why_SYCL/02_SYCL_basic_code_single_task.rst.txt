SYCL Basic Code: single_task
============================

SYCL offers many advantages to developers, including improved productivity, better performance, and enhanced code maintainability. In this lesson, you will gain an overall understanding of basic SYCL features and concepts. 

SYCL Advantages
----------------------------

**1.** SYCL provides an **easier programming model for heterogeneous applications** than traditional models such as OpenCL or CUDA. 

**2.** SYCL **supports modern C++ language features** and can help simplify writing portable and maintainable code. 

**3.** SYCL allows developers to take advantage of heterogeneous hardware architectures and **utilize multiple processors or accelerators simultaneously**. 

**4.** SYCL provides an abstraction layer that makes it **easier to port code to different hardware** architectures. 

**5.** SYCL enables the development of **high-performance** and **data-parallel** applications. 

**6.** SYCL **allows third-party vendors to provide tools** that help optimize code for different hardware architectures. 

Basic SYCL Code #1: single_task
-------------------------------

In this subsection, we present a code with a simple SYCL algorithm called ``single_task``, which equivalent in standard C++ would be ``std::thread``, to gain a fundamental understanding of SYCL components. **The construct** ``single_task`` **is used to define a unit of work that should be executed on a single processing element, typically a single CPU core or GPU thread.** Our goal in this code is to modify specifically the 6th element of a 10-size vector using the SYCL ``single_task`` command. We will provide a comprehensive explanation of each segment of the code.

.. code-block:: cpp

    #include <CL/sycl.hpp>
    using namespace sycl;
    
    int main() {

        queue Q;                        // The queue, Q, is the object that
                                        // submits the task to a device.
        int const size = 10;
        buffer<int> A{ size };          // The buffer, A, is the memory used to
                                        // transfer data between host and device.
        
        Q.submit([&](handler& h) {      // The handler, h, is the object that contains 
                                        // the single_task function to be used.
            
            accessor A_acc(A, h);       // The accessor, A_acc, is the object that
                                        // efficiently accesses the buffer elements.
                                        
            h.single_task([=]() {
                A_acc[5] = 77; 
                });

            });

        host_accessor result(A);        // host_accessor is the object that allows 
                                        // the host to access the buffer memory.

        for (int i = 0; i < size; i++)  // Print output
            std::cout << result[i] << " "; std::cout << "\n";
        return 0;

    }

In SYCL code, several fundamental components play vital roles in coordinating work, managing data, and ensuring seamless communication between the host and device. One of these essential elements is the ``queue``, denoted as ``Q``. The queue serves as the central construct used to submit work items, control execution flow, and facilitate data transfers in a parallel and heterogeneous computing environment, such as CPUs or GPUs.

Another critical component is the ``buffer``, represented as ``A``. This ``buffer`` serves as a data container that defines the region of memory accessible by both the host and the device, enabling efficient data sharing and transfer between them.

Another fundamental concept in SYCL programming is the **command group** that, in our code, it is defined by:

.. code-block:: cpp

        Q.submit([&](handler& h) {

            ...

        }

The **command group** represents a unit of work that can be submitted to a SYCL queue for execution; its main function is to define the operations or computations that are to be performed on the target device.

The command group needs the ``accessor``:

.. code-block:: cpp

            accessor A_acc(A, h);

The ``accessor``, ``A_acc``, is the object used to define the access rights (``read-only``, ``write-only``, or ``read-write``) of specific kernels to the buffer elements.

Inside of the command group resides the specific **SYCL kernel function**, which is ``single_task`` in this case. Note that ``single_task`` is provided by the handler, ``h``:

.. code-block:: cpp

            h.single_task([=]() {
                A_acc[5] = 77; 
            });

The ``handler`` is the object that represents a context in which command groups are defined.  It specifies the operations and dependencies within a command group and controls the execution behavior of those operations.  One consideration to keep in mind is that only one SYCL **kernel function**, even if it is the same, can be executed in the command group. 

The **kernel function** in this case is:

.. code-block:: cpp

                A_acc[5] = 77;

Note that a lambda function can be used as kernel function as well.

Basic SYCL Code #2: parallel_for Hands-on 
-----------------------------------------

To become familiar with the SYCL structure, we propose the following hands-on exercise for you to think about:  

**Create a variation of the** ``single_task`` **code that changes, in one step, all elements of a 10-size vector to the value of 77.**

.. code-block:: cpp

    #include <CL/sycl.hpp>
    using namespace sycl;
    
    int main() {

        queue Q;                        // The queue, Q, is the object that
                                        // submits the task to a device.
        int const size = 10;
        buffer<int> A{ size };          // The buffer, A, is the memory used to
                                        // transfer data between host and device.
    


        //********** YOUR CODE STARTS HERE **********//

        // Step 1) Submit the queue with the handler definition:
        
        // Step 2) Define the accessor with buffer and handler:
        
        // Step 3) Call parallel_for from the handler specifying range and index:
        
        // Step 4) Change the accessor elements with the desired value using the index:
        

        //********** YOUR CODE ENDS HERE **********//



        host_accessor result(A);        // host_accessor is the object that allows 
                                        // the host to access the buffer memory.

        for (int i = 0; i < size; i++)  // Print output
            std::cout << result[i] << " "; std::cout << "\n";
        return 0;

    }

If you are thinking that ``single_task`` might not be the best approach you are in the right track.

.. note::

    The best way to tackle this is with the use of ``parallel_for``.

The solution to this ``parallel_for`` hands-on exercise is in the next section.


Main SYCL concepts takeaways
----------------------------

To recap, let's revisit the main concepts introduced in this section for expressing parallelism, managing data transfers, and controlling the execution of workloads in SYCL programs to enable efficient execution on heterogeneous platforms:

- **Queue**: A SYCL queue manages the execution of command groups on a specific device. It acts as a command queue, allowing you to submit command groups for execution and control the order of execution.

- **Scheduler**: The scheduler in SYCL is an internal component of the runtime system that manages the execution and scheduling of command groups on devices. It optimizes the execution by considering device capabilities, workload distribution, dependencies, and resource availability. The queue is the primary interface through which tasks are submitted to the scheduler for execution.

- **Buffer**: A buffer in SYCL is a data container that represents a region of memory accessible by both the host and the device. It enables efficient data transfer and sharing between the host and the device without explicit memory management.

- **Accessor**: Data represented by a buffer cannot be directly accessed through the buffer object. Instead, we must create accessor objects that allow us to safely access a buffer’s data. Accessors inform the runtime where and how we want to access data, allowing the runtime to ensure that the right data is in the right place at the right time.

- **Command group**: In SYCL, a command group represents a unit of work that is submitted for execution on an OpenCL device. It encapsulates a set of operations and allows you to express parallelism and dependencies between tasks. Remember to call only a SYCL kernel function per command group.

- **Handler**: A handler in SYCL represents a context in which command groups are defined. It provides methods for specifying operations within a command group, such as kernel invocations and memory transfers, and controls the execution behavior of those operations.
