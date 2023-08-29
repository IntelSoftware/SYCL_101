SYCL Essentials: Modules
========================

The concepts build on top of each other introducing and 
reinforcing the concepts of oneAPI and SYCL Programming.

Module 0: **Introduction to Jupyter Notebook `Optional`**
 This module explains how to use Jupyter Notebook 
 which is used in all of the modules to edit and run coding 
 excecises, this can be skipped if you are already familiar 
 with using Jupyter Notebooks.

Module 1: **oneAPI Intro**
 This module introduces you to oneAPI and oneAPI's implementation 
 of SYCL (Data Parallel C++/DPC++). You will learn about basic 
 SYCL hello world program and how to compile SYCL code for 
 Intel hardware using Data Parallel C++ Compiler.

Module 2: **DPCPP Program Structure**
 This module demonstrates basic **SYCL code anatomy** and 
 program structure. You will learn about important **SYCL classes**, 
 different types of kernels. You will also learn about 
 **Buffer Accessor memory model** and synchronizations when using buffers.

Module 3: **DPCPP Unified Shared Memory**
 This module demonstrates hows to implement different modes 
 of **Unified Shared Memory (USM)** in SYCL code, as well 
 as demonstrate how to solve for data dependencies for in-order 
 and out-of-order tasks.

Module 4: **DPCPP Sub Groups**
 This module demonstrates SYCL **Sub-groups** and why they are 
 important. The code samples demonstrate how to implement a query 
 for sub-group info, sub-group shuffles and sub-group group alogorithms.

Module 5: **Intel Advisor**
 This module demonstrates various aspects of **Intel® Advisor**. 
 The first uses Intel® Advisor to show performance offload 
 opportunities found in a sample application, and then additional 
 command-line options for getting offload advisor results. 
 The second, gives an example of **roofline analysis** and command 
 line options for getting advisor results.

Module 6: **Intel VTune_Profiler**
 This module demonstrates using **Intel® Vtune™ Profiler on the command-line** 
 to collect and analyze gpu_hotspots. You will learn how to collect 
 performance metrics and explore the results with the HTML output 
 rendered inside of the notebook.  This module meant for exploration 
 and familiarization, and does not require any code modification.

Module 7: **DPCPP Library**
 This module demonstrates using **Intel® oneAPI DPC++ Library (oneDPL)**
 for heterogeneous computing. You will learn how to use various Parallel
 STL algorithms for heterogeneous computing and also look at 
 gamma-correction sample code that uses oneDPL.

Module 8: **DPCPP Reduction**
 This module demonstrates how reductions can be parallelized. You will 
 learn about **reduction group alogorithm** and also **kernel reductions in SYCL**_.

Module 9: **DPCPP Buffers_And_Accessors_Indepth**
 This module demonstrates various ways to create **Buffers in SYCL**. 
 You will learn how to use **sub-buffers**, buffer properties and when 
 to use_host_ptr, set_final_data and set_write_data. You will also learn 
 accessors, host_accessors and its usecases.

Module 10: **DPCPP Graphs Scheduling Data Management**
 This module demonstrates how to utilize USM and Buffers and accessors 
 to apply Memory management and take control over **data movement implicitly 
 and explicitly**, utilize different types of data dependences that are 
 important for ensuring execution of graph scheduling. You will also learn 
 to select the correct modes of **dependences in Graphs scheduling**.

Module 11: **Intel Distribution_for_GDB**
 This module demonstrates how to use the Intel® Distribution for GDB to 
 debug kernels running on GPUs.

Module 12: **DPCPP Local_Memory_And_Atomics**
 This module demonstrates how to utilize device's **Shared Local Memory** 
 to reduce latency in accessing data for kernel computation. The module 
 also introduces **Atomic operations** to avoid data race conditions when 
 multiple work-items are updating the same memory object.