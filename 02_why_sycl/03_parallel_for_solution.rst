SYCL code basic elements: Extra
===============================

Here is the solution for the parallel_for hands-on exercise proposed in the previous section:

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

        host_accessor result(A);        // host_accesor is the object that allows 
                                        // the host to access the buffer memory

        for (int i = 0; i < size; i++)  // Print output
            std::cout << result[i] << " "; std::cout << "\n";
        return 0;

    }

As mentioned before, the parallel_for is called from the handler. This 
SYCL kernel function requires the **range** argument to be stablished:

.. code-block:: cpp

            range<1>(size)

as well as the **id** argument, that refers to the index, and named indx here:

.. code-block:: cpp

            (id<1> indx)

so all elements of the accessor can be modified as follows:

.. code-block:: cpp

            A_acc[indx] = 77; 

Note here that it is not the buffer, **A**, what
is modified inside of the SYCL kernel function, but the accessor, **A_acc**,
that manages the access and usage of the buffer memory.