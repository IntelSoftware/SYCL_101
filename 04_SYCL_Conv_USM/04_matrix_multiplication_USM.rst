SYCL-USM: matrix_multiplication
===============================

Matrix multiplication, often referred to as matmul, is a fundamental 
operation in linear algebra; it plays a crucial role in various 
scientific and engineering applications, such as image processing, 
simulation, and machine learning. The operation involves taking the 
dot product of rows from one matrix with the columns of another matrix 
to produce a resulting matrix. While conceptually simple, efficient 
computation of matrix multiplication becomes a challenge when dealing 
with large matrices due to the inherent parallelism that can be leveraged 
for optimization. This is where SYCL comes into play. SYCL is a 
programming model and API that enables developers to write code that 
can be executed on a variety of heterogeneous platforms, including CPUs, 
GPUs, FPGAs, and other accelerators, using a single-source approach.
SYCL abstracts the complexities of heterogeneous hardware and facilitates 
the development of high-performance code while maintaining portability 
across different devices.

In this context, leveraging SYCL for matrix multiplication offers the 
potential to harness the power of various computing devices while 
maintaining a unified codebase. By expressing parallelism through SYCL's 
constructs, developers can achieve optimized matrix multiplication 
routines that efficiently distribute computation across available 
resources. In the code below we present the matrix multiplication code in
SYCL format using USM:

.. code-block:: c++

    //==============================================================
    // Copyright © Intel Corporation
    //
    // SPDX-License-Identifier: MIT
    // =============================================================

    #include <CL/sycl.hpp>
    
    using namespace sycl;

    static const int N = 3;

    int main() {
        queue q;

        // STEP 1 : Get device information
        std::cout << "Device : " << q.get_device().get_info<info::device::name>() << "\n";

        // STEP 2 : Initialize vectors in shared memory
        int *data1 = malloc_shared<int>(N * N, q);
        int *data2 = malloc_shared<int>(N * N, q);
        int *dataR = malloc_shared<int>(N * N, q);

        // STEP 3 : Asign values to vectors
        for (int i = 0; i < N * N; i++) {
            data1[i] = 10;
            data2[i] = 20;
            dataR[i] =  0;
        }

        // STEP 4 : Proceed with the calculation
        q.parallel_for(range<2>{N,N}, [=](item<2> item){
            const int j = item.get_id(0);
            const int i = item.get_id(1);
            
            for (int k = 0; k < N; ++k)
                dataR[i*N+j] += data1[i*N+k] * data2[k*N+j];
        }).wait();

        // STEP 5 : Print output values
        for (int i = 0; i < N * N; i++) std::cout << dataR[i] << " ";
        std::cout << "\n";

        //# STEP 6 : Release memory
        free(data1, q);
        free(data2, q);
        free(dataR, q);

        return 0;
    }

The code above produces the following output:

.. code-block:: c++

    Device : Intel(R) UHD Graphics [0x9a60]
    600 600 600 600 600 600 600 600 600 
