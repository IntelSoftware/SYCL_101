SYCL Basic Code: parallel_for
=============================

In this section we will explain ``parallel_for`` which is a core concept in SYCL, designed to facilitate parallel execution of code across a range of processing elements, such as GPU threads or CPU cores. **Essentially** ``parallel_for`` **distributes work across multiple processing elements for parallel execution and allows developers to express parallelism easily .** The equivalent of ``parallel_for`` in standard C++ would be ``std::for_each``. With ``parallel_for`` programmers only have to define a function or a lambda expression that represents the work to be done in parallel while maintaining code portability.

Here's an example of how ``parallel_for`` works (solution of previous section):

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
                                        
            h.parallel_for(range<1>(size), [=](id<1> indx) {
                A_acc[indx] = 77; 
                });

            });

        host_accessor result(A);        // host_accessor is the object that allows 
                                        // the host to access the buffer memory

        for (int i = 0; i < size; i++)  // Print output
            std::cout << result[i] << " "; std::cout << "\n";
        return 0;

    }

Note that

.. code-block:: cpp

            h.parallel_for(range<1>(size), [=](id<1> indx) {
                A_acc[indx] = 77; 
                });

is where ``parallel_for`` is presented within the code and, as it happened with ``single_task``, ``parallel_for`` is provided by the handler ``h``, as well. Let's explain these components:

 * ``h.parallel_for``: This line initiates a parallel computation using the parallel_for construct. It means that the enclosed code block will be executed in parallel across multiple processing elements (e.g., CPU cores or GPU threads). The ``h`` is the handler, which manages the execution of SYCL tasks on a specific device.

 * ``range<1>(size)``: This part specifies the range of work items for the parallel computation. In this case, it's a 1D range defined by ``range<1>`` with a size of ``size=10``. The range defines how many times the enclosed code block will execute in parallel meaning that in this case the code block will be executed 10 times concurrently, each time with a different value of ``indx`` ranging from 0 to 9.

 * ``[=](id<1> indx) { A_acc[indx] = 77; }``: This is a lambda function that represents the work to be performed in parallel. The lambda function takes an ``id<1>`` argument named ``indx``, which represents the unique identifier of the current work item. Inside the lambda function, the code sets the value at the indx-th position of the array ``A_acc`` to ``77``. In essence, each parallel instance will update a different element of the ``A_acc`` array to the value 77.


Note that it is not the buffer, ``A``, what is modified inside the SYCL kernel function, but the accessor, ``A_acc``, which manages the access and usage of the buffer memory.
