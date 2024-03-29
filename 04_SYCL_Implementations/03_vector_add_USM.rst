USM vector_add with SYCL
========================

In this discussion, we implement vector addition using Unified Shared Memory (USM), highlighting how the SYCL programming model simplifies the utilization of heterogeneous computing resources. 
The main takeaway is that with USM there is no requirement to define ``buffers``, ``handlers``, and ``accessors``. In this case, the USM ``malloc_shared`` function is sufficient to allocate and manage memory access:

.. code-block:: cpp

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

      // STEP 1 : Get device information
      std::cout << "Device : " << q.get_device().get_info<info::device::name>() << "\n";

      // STEP 2 : Initialize vectors in shared memory
      int *data1 = malloc_shared<int>(N, q);
      int *data2 = malloc_shared<int>(N, q);
      int *dataR = malloc_shared<int>(N, q);

      // STEP 3 : Asign values to vectors
      for (int i = 0; i < N; i++) {
         data1[i] = 10;
         data2[i] = 20;
         dataR[i] =  0;
      }

      // STEP 4 : Proceed with the calculation
      q.parallel_for(range<1>(N), [=](id<1> i) {
         dataR[i] = data1[i] + data2[i];
      }).wait();

      // STEP 5 : Print output values
      for (int i = 0; i < N; i++) std::cout << dataR[i] << " ";
      std::cout << "\n";

      // STEP 6 : Release memory
      free(data1, q);
      free(data2, q);
      free(dataR, q);

      return 0;
   }

This part of the code:

.. code-block:: cpp

      std::cout << "Device : " << q.get_device().get_info<info::device::name>() << "\n";

gets device information from the ``q``, and prints information about the selected device.

**USM** gets established here:

.. code-block:: cpp

      int *data1 = malloc_shared<int>(N, q);
      int *data2 = malloc_shared<int>(N, q);
      int *dataR = malloc_shared<int>(N, q);

where three shared memory arrays ``data1``, ``data2``, and ``dataR`` are allocated using ``malloc_shared<int>(N, q)``. They are accessible during computation by both the host and device.
USM also offers ``malloc_device`` and ``malloc_host`` to explicitly allocate memory on the host or device, but they will not be covered in this course.

So, when should you use USM versus the conventional SYCL? In summary, using USM is a good approach to consider when:

- The code has many pointers that are susceptible to future changes.

- When it is expected that the application will gain complexity over time.
