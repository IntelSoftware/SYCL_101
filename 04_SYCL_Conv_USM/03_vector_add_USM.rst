SYCL-USM: vector_add
====================

In this section, we explore vector addition using USM within the SYCL 
framework. USM enables memory regions that are accessible from 
both the host and the devices, reducing the need for explicit 
data transfers and simplifying memory management. This approach 
not only streamlines code but also allows developers to focus 
on algorithmic design rather than memory-related intricacies. 
The code sample below presents the steps for using USM with SYCL for
vector_add, which offers a more intuitive and efficient 
way to harness the capabilities of heterogeneous computing resources.

Note that using USM eliminates the need to define buffers,
handlers, and accessors. In this case, the malloc_shared function of USM is sufficient
to allocate and manage memory access:

.. In this discussion, we delve into the world of vector addition 
.. using USM with SYCL. We'll explore the benefits of using USM 
.. for memory management, examine the steps involved in implementing 
.. vector addition with SYCL, and highlight how the SYCL programming 
.. model simplifies the utilization of heterogeneous computing resources. 

.. By the end of this exploration, you'll have a solid understanding 
.. of how to harness the power of USM in SYCL to efficiently perform 
.. vector addition and lay the foundation for more intricate parallel 
.. algorithms.[[[these 2 paragraphs don't show up in the Preview mode. Is it from a different section (Intro?) or possibly an earlier draft? I edited anyway.]]]

.. vector_add:
.. --------------

.. vector_add in words

.. code-block:: c++

   //==============================================================
   // Copyright © Intel Corporation
   //
   // SPDX-License-Identifier: MIT
   // =============================================================
   
   #include <CL/sycl.hpp>
   
   using namespace sycl;

   static const int N = 256;

   int main() {
      queue q;

      //# STEP 1 : Get device information
      std::cout << "Device : " << q.get_device().get_info<info::device::name>() << "\n";

      //# STEP 2 : Initialize vectors in shared memory
      int *data1 = malloc_shared<int>(N, q);
      int *data2 = malloc_shared<int>(N, q);
      int *dataR = malloc_shared<int>(N, q);

      //# STEP 3 : Asign values to vectors
      for (int i = 0; i < N; i++) {
         data1[i] = 10;
         data2[i] = 20;
         dataR[i] =  0;
      }

      //# STEP 4 : Proceed with the calculation
      q.parallel_for(range<1>(N), [=](id<1> i) {
         dataR[i] = data1[i] + data2[i];
      }).wait();

      //# STEP 5 : Print output values
      for (int i = 0; i < N; i++) std::cout << dataR[i] << " ";
      std::cout << "\n";

      //# STEP 6 : Release memory
      free(data1, q);
      free(data2, q);
      free(dataR, q);

      return 0;
   }

In this example, we used malloc_shared, which is appropriate when
data movement happens implicitly between the host and device.

Additionally, USM offers **malloc_device** and **malloc_host**, which
are approches to tackle memory management access by the host or device
explicitly, but this course does not cover them for now.

So, when should you use USM versus the conventional SYCL? In summary, 
using USM is a good approach to consider when:

- The code has many pointers that are susceptible to future changes.

- When it is expected that the application will gain complexity over time.
