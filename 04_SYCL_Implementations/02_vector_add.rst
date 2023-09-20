Conventional vector_add with SYCL
=================================
In the following code, we dissect the conventional vector addition technique that uses ``buffer``, ``handler`` and ``accessor``. This approach typically requires explicit memory management, including allocating memory on the host and devices, copying data between them, and synchronizing their operations:

.. code-block:: cpp

   //==============================================================
   // Copyright © Intel Corporation
   //
   // SPDX-License-Identifier: MIT
   // =============================================================
   
   #include <CL/sycl.hpp>

   using namespace sycl;

   int main() {
      const int N = 256;
      
      // STEP 1 : Initialize vectors
      std::vector<int> vector1(N, 10);
      std::vector<int> vector2(N, 20);
      std::vector<int> vectorR(N,  0);

      // STEP 2 : Create buffer for the vectors 
      buffer vector1_buffer(vector1);
      buffer vector2_buffer(vector2);
      buffer vectorR_buffer(vectorR);
      
      // STEP 3 : Submit task to add vector
      queue q;
      q.submit([&](handler &h) {
         
         //# STEP 4 : Create vectors accessors
         accessor vector1_accessor (vector1_buffer, h, read_only);
         accessor vector2_accessor (vector2_buffer, h, read_only);
         accessor vectorR_accessor (vectorR_buffer, h);
         
         //# STEP 5 : Proceed with the calculation
         h.parallel_for(range<1>(N), [=](id<1> index) {
            vectorR_accessor[index] = vector1_accessor[index] + vector2_accessor[index];
         });
         
      });

      // STEP 6 : Create a host accessor to copy data from device to host
      host_accessor h_a(vectorR_buffer,read_only);

      // STEP 7 : Print output values 
      std::cout<<"\nOutput Values: ";
      for (int i = 0; i < N; i++) std::cout<< h_a[i] << " ";
      std::cout<<"\n";

      return 0;
   }

These are the main SYCL steps to read from the code:

* **Vector Initialization:** Three vectors ``vector1``, ``vector2``, and ``vectorR`` of size N are created on the host and initialized with specific values. They represent the input vectors and the result vector of a vector addition operation.

* **Create Buffers:** Three SYCL buffers, ``vector1_buffer``, ``vector2_buffer``, and ``vectorR_buffer``, are created to hold the data of the vectors. These buffers are used for data transfer between the host and the SYCL device (e.g., GPU).

* **Submit SYCL Task:** A SYCL queue q is created, and a task is submitted to the queue using the ``q.submit()`` method. This task will execute on a SYCL device, such as a GPU.

* **Create Accessors:** Accessors are created for the input and output buffers. ``vector1_accessor`` and ``vector2_accessor`` are read-only accessors, while ``vectorR_accessor`` is a regular accessor.

* **Parallel For:** A parallel loop is launched using ``h.parallel_for()``, which will execute the vector addition operation in parallel across multiple work items. Each work item is responsible for adding one element of the vectors. **Note that this function uses the accessors, not the buffers or the initial vectors.** 

* **Host Accessor:** After the SYCL task is completed, a host accessor ``h_a`` is created for the ``vectorR_buffer`` to copy the data from the device to the host.

While effective, this method can lead to intricate code and hinder productivity due to its manual memory management requirements. In the next section, we'll implement vector_add using USM.
