What is SYCL?
=============


Definition
-----------

SYCL is a high-level single-source standard C++ programming model that can 
target a wide range of heterogeneous platforms.

SYCL is an industry-driven standard —developed 
by Khronos Group and announced in March 2014— that allows data parallelism for heterogeneous 
systems based on C++ 17. It is a royalty-free, cross-platform abstraction 
layer that enables the development of applications and frameworks with 
the portability and efficiency of OpenCL, while providing a user interface 
that's flexible and easy to use.

SYCL standard is designed to be both highly portable and highly efficient
and allows applications to offload compute kernels and data transfer to 
OpenCL-enabled accelerators such as GPUs, FPGAs, and other processors.

SYCL Features
--------------

- **SYCL is modern standard C++:** Unlike many other programming models and languages that require language extensions, SYCL does not need any of that. It is pure standard C++; any SYCL application will compile and run using a SYCL library, even if a device compiler and a device are not available in your system. 

- **SYCL is open, multivendor, and multiarchitecture:** Because there is no need to copy data, it enables pointer-based algorithms and data structures to be used across architectures of different vendors and makes it easier to use the same code on different devices. 

- **Separation of data access and data storage:** When using buffers and accessors in SYCL, the data access and data storage are kept separate. This allows the programmer to create data-parallel tasks easily, without needing to manually track data movement and event dependencies between kernels. 

- **No need to copy data:** Unified Shared Memory (USM) allows different devices, such as CPUs and GPUs, to share and access data without having to copy it between them. 

- **Ease of hierarchical parallelism:** Inspired by OpenCL and OpenMP, SYCL makes data parallelism easy to understand by using hierarchical parallelism and modern C++ instructions, so tasks are easily organized and synchronized, which makes the code more efficient and less fragmented. 

- **Two compilation phases:** SYCL requires two compilation passes, one for the host code and one for the device code. However, contrarily to OpenCL, SYCL has only one source file, meaning there is only one executable. The two compilations can be made by the same compiler. 

- **High-level programmer model:** SYCL provides several high-level abstractions over common boilerplate code in OpenCL and other backends. This includes selecting devices, allocating, copying data, managing dependencies, scheduling compiling kernels, and much more. 


Specifications
---------------

SYCL utilizes specifications to standardize and streamline the development of parallel 
applications for heterogeneous architectures, enabling portability, productivity, and 
performance while fostering a vibrant community of SYCL users and providers.  New 
specifications are being released to accommadate new features and technological advances.
The SYCL specifications that have been published as of today are:

- SYCL 1.2: Specification released in May of 2015: It is considered obsolete.
- SYCL 2.2: It was a provisional specification published in 2016 that is considered deprecated.
- SYCL 1.2.1: Its latest revision was released on April 27, 2020.
- SYCL 2020: Specification revision 7 released on April 18, 2023.

The SYCL 2020 specification marks a significant leap forward that features over 40 new improvements, such as:

- **Unified Shared Memory (USM)**, enabling code with pointers to work naturally without buffers or accessors.
- **Parallel reductions**, adding a built-in reduction operation and helping to avoid boilerplate code, providing maximum performance for hardware with built-in operations.
- **Work group and sub-group algorithms**, enabling efficient operations between work items.
- **Class template argument deduction (CTAD)** and deduction guides to enable simpler class template instantiation.
- **Simplification of accessors**, which adds a built-in reduction operation, reduces the burden of boilerplate code, and enables simplified C++ patterns.
- **Expanded interoperability** with different backends, enabling support for backends other than OpenCL.
- **Improvements to atomic operations** to be closer to C++ atomics to enable more parallel programming freedom.


Implementations
----------------

A SYCL implementation refers to a software version or revision of the SYCL programming model. 
It consists of the necessary tools, libraries, and runtime support that enable developers
to write SYCL code and execute it on compatible hardware platforms.

Different vendors and organizations can provide their own SYCL implementations,
each with its own set of features, optimizations, and supported hardware platforms. 
These implementations provide the necessary compiler, libraries, and runtime 
components to enable developers to write and execute SYCL code efficiently on their 
respective platforms.

These are some of the popular SYCL implementations that are available:

   - **DPCP++** by Intel as part of the oneAPI solution that supports Intel CPUs, GPUs, and FPGAs as well as NVIDIA and AMD GPUs 
   - **ComputeCpp** by Codeplay
   - **TriSYCL** by Xilinx
   - **HipSYCL** (Open SYCL) by the University of Heidelberg
   - **neoSYCL** by the Tohoku University



* Source: Khronos (https://www.khronos.org/sycl/)
