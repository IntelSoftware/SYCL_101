Why SYCL?
#########

What is SYCL
============

.. Definition & History:
.. ---------------------

.. bla

.. **Definition & History:**
.. -------------------------

.. bla

.. Definition & History:
.. ~~~~~~~~~~~~~~~~~~~~~

.. blabla

.. **Definition & History:**
.. ~~~~~~~~~~~~~~~~~~~~~~~~~

.. blabla

Definition & Features:
-----------------------

SYCL is an industry-driven standard, developed by Kronos Group and 
announced in March 2014, that allows data parallelism for heterogeneous 
systems based on C++ 17. It is a royalty-free, cross-platform abstraction 
layer that enables the development of applications and frameworks with 
the portability and efficiency of OpenCL, while providing an ease-of-use
and flexibility interface for developers. 

SYCL standard is designed to be both highly portable and highly efficient
and allows applications to offload compute kernels and data transfer to 
OpenCL-enabled accelerators such as GPUs, FPGAs, and other processors.

SYCL characteristics: 

- **Separation of data access and data storage:** When using buffers and accessors in SYCL, the data access and data storage are kept separate. This allows the programmer to create data-parallel tasks easily, without needing to manually track data movement and event dependencies between kernels 

- **No need of data copying:** Unified Shared Memory (USM) allows different devices, such as CPUs and GPUs, to share and access data without having to copy it between them. 

- **Same code for different architecture:** Because there is no need of data copying, it enables the use of pointer-based algorithms and data structures across devices, and makes it easier to use the same code on different devices. 

- **Ease of hierarchical parallelism:** Inspired by OpenCL and OpenMP, SYCL makes data parallelism easy to understand with the use of hierarchical parallelism and modern C++ instructions, so tasks are easily organized and synchronized making the code more efficient and less fragmented. 

- **Two phases compilation:** SYCL requires two compilation passes, one for the host code and one for the device code, but differently to OpenCL, SYCL has only one source file, meaning there is only one executable.  The two compilations can be made by the same compiler. 

- **High Level programmer model:** This means SYCL provides several high-level abstractions over common boilerplate code in open CL and other backends. This includes things like selecting devices, allocating, copying data, managing dependencies, scheduling compiling kernels and much more. 

- **Standard C++:** Unlike many other programming models and languages that require language extensions, SYCL does not require any of that and it is pure standard C++ so any SYCL application will compile and run using a SYCL library even if there is no device compiler and no device is available in your system. 

- SYCL implementations:

   - DPCP++: Open source implementation led by Intel as part of the oneAPI solution that supports Intel CPUs, GPUs and FPGAs as well as NVIDIA and AMD GPUs 
   - ComputeCpp: 
   - TriSYCL: 
   - HipSYCL: 

Specifications & Implementations:
---------------------------------

bla

First benefits of SYCL
======================

SYCL offers a range of advantages to developers, including improved productivity, better performance, and enhanced code maintainability. In this lesson, students will gain an overall understanding of how SYCL can help them develop efficient parallel programs that scale well. Among others, these are the most important benefits of using SYCL: 

1. SYCL provides an easier programming model for heterogeneous applications than traditional models such as OpenCL or CUDA. 

2. SYCL supports modern C++ language features and can help simplify writing portable and maintainable code. 

3. SYCL allows developers to take full advantage of heterogeneous hardware architectures and utilize multiple processors or accelerators simultaneously. 

4. SYCL provides an abstraction layer that makes it easier to port code to different hardware architectures. 

5. SYCL enables the development of high-performance and data-parallel applications. 

6. SYCL allows third-party vendors to provide tools that help optimize code for different hardware architectures. 


.. Level 1 Header with -
.. ---------------------

.. blabla

.. **Level 1 Header with -**
.. -------------------------

.. blabla

.. Level 2 Header with ~
.. ~~~~~~~~~~~~~~~~~~~~~

.. blabla

.. **Level 2 Header with ~**
.. ~~~~~~~~~~~~~~~~~~~~~~~~~

.. blabla

.. Level 3 Header with asterisc
.. ****************************

.. blabla

.. **Level 3 Header with asterisc **
.. *********************************

.. blabla


and this is a regular text::

   print 'hello'
   >> hello





Additional benefits of SYCL
===========================



this is another thext::

   print 'something else'
   >> hello

.. toctree::
   :hidden:
