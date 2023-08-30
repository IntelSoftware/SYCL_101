SYCL Essentials: Modules
========================

The concepts build on top of each other, introducing and 
reinforcing the concepts of oneAPI and SYCL Programming.

Module 0: **Introduction to Jupyter Notebook `Optional`**
 This module explains how to use Jupyter Notebook, 
 which is used in all of the modules to edit and run coding 
 exercises. You can skip this if you are already familiar 
 with using Jupyter Notebooks.

Module 1: **oneAPI Intro**
 This module introduces you to oneAPI and oneAPI's implementation 
 of SYCL (Data Parallel C++/DPC++). You will learn about the basic 
 SYCL hello world program and how to compile SYCL code for 
 Intel hardware using Data Parallel C++ Compiler.

Module 2: **DPCPP Program Structure**
 This module demonstrates basic **SYCL code anatomy** and 
 program structure. You will learn about important **SYCL classes** and 
 different types of kernels. You will also learn about 
 **Buffer Accessor memory model** and synchronizations when using buffers.

Module 3: **DPCPP Unified Shared Memory**
 This module demonstrates how to implement different modes 
 of **Unified Shared Memory (USM)** in SYCL code, as well 
 as demonstrate how to solve for data dependencies for in-order 
 and out-of-order tasks.

Module 4: **DPCPP Sub Groups**
 This module demonstrates SYCL **sub-groups** and why they are 
 important. The code samples demonstrate how to implement a query 
 for sub-group info, sub-group shuffles, and sub-group algorithms.

Module 5: **Intel® Advisor**
 This module demonstrates various aspects of **Intel® Advisor**. 
 The first aspect[[[the first aspect, yes?]]] uses Intel Advisor to show performance offload 
 opportunities found in a sample application, and then additional 
 command-line options for getting offload advisor results. 
 The second gives an example of **roofline analysis** and command 
-line options for getting advisor results.

Module 6: **VTune™_Profiler**[[["Intel" not needed with this product name.]]]
 This module demonstrates using ** VTune™ Profiler on the command-line** 
 to collect and analyze gpu_hotspots. You will learn how to collect 
 performance metrics and explore the results with the HTML output 
 rendered inside of the notebook.  This module is meant for exploration 
 and familiarization; it does not require any code modification.

Module 7: **DPCPP Library**
 This module demonstrates using **Intel® oneAPI DPC++ Library (oneDPL)**
 for heterogeneous computing. You will learn how to use various Parallel
 STL algorithms for heterogeneous computing and also look at 
 gamma-correction sample code that uses oneDPL.

Module 8: **DPCPP Reduction**
 This module demonstrates how reductions can be parallelized. You will 
 learn about **reduction group algorithm** and also **kernel reductions in SYCL**.

Module 9: **DPCPP Buffers_And_Accessors_In Depth**[[[I changed to "In Depth." does it need an underscore, are ANY underscores needed in title?]]]
 This module demonstrates various ways to create **buffers in SYCL**. 
 You will learn how to use **sub-buffers**, buffer properties, and when 
 to use_host_ptr, set_final_data, and set_write_data. You will also learn about 
 accessors, host_accessors, and their use cases.

Module 10: **DPCPP Graphs Scheduling Data Management**
 This module demonstrates how to utilize USM and Buffers and accessors[[[USM, buffers, and accessors" or "USM buffers and accessors"?]]]
 to apply memory management and take control over **data movement implicitly 
 and explicitly** to help utilize different types of data dependences that are 
 important for ensuring execution of graph scheduling. You will also learn 
 to select the correct modes of **dependences in graphs scheduling**.

Module 11: **Intel® Distribution_for_GDB**[[[why underscores?]]]
 This module demonstrates how to use Intel® Distribution for GDB to 
 debug kernels running on GPUs.

Module 12: **DPCPP Local_Memory_And_Atomics**[[[why underscores?]]]
 This module demonstrates how to utilize a device's **shared local memory** 
 to reduce latency in accessing data for kernel computation. The module 
 also introduces **atomic operations**, which help avoid data race conditions when 
 multiple work items are updating the same memory object.
