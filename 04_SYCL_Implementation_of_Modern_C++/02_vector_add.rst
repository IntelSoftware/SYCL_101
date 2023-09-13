SYCL-Conventional: vector_add
=============================
In the following, we dissect the conventional vector addition technique. This approach typically requires explicit memory management, including allocating memory on the host and devices, copying data between them, and synchronizing the operations.

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
      
      //# STEP 1 : Initialize vectors
      std::vector<int> vector1(N, 10);
      std::vector<int> vector2(N, 20);
      std::vector<int> vectorR(N,  0);

      //# STEP 2 : Create buffer for the vectors 
      buffer vector1_buffer(vector1);
      buffer vector2_buffer(vector2);
      buffer vectorR_buffer(vectorR);
      
      //# STEP 3 : Submit task to add vector
      queue q;
      q.submit([&](handler &h) {
         
         //# STEP 4 : Create vectors accessors
         accessor vector1_accessor (vector1_buffer,h, read_only);
         accessor vector2_accessor (vector2_buffer,h, read_only);
         accessor vectorR_accessor (vectorR_buffer,h);
         
         //# STEP 5 : Proceed with the calculation
         h.parallel_for(range<1>(N), [=](id<1> index) {
            vectorR_accessor[index] = vector1_accessor[index] + vector2_accessor[index];
         });
         
      });

      //# STEP 6 : Create a host accessor to copy data from device to host
      host_accessor h_a(vectorR_buffer,read_only);

      //# STEP 7 : Print output values 
      std::cout<<"\nOutput Values: ";
      for (int i = 0; i < N; i++) std::cout<< vectorR[i] << " ";
      std::cout<<"\n";

      return 0;
   }

We can see that using the conventional approach with SYCL, the programmer is required to define the memory buffers, handlers, and accessors. While effective, this method can lead to intricate code and hinder productivity due to its manual memory management requirements. In the next section, we present the same vector_add code sample approached with the use of USM.
