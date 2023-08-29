SYCL Essentials: Learning Objectives
====================================

Module 1: **oneAPI Intro**
 * Explain how the **oneAPI** programming model can solve the challenges of programming in a heterogeneous world. 
 * Use oneAPI projects to enable your workflows.
 * Understand the **SYCL** language and programming model.
 * Familiarization on the use Jupyter notebooks for training throughout the course.

Module 2: **DPCPP Program Structure**
 * Explain the **SYCL** fundamental classes.
 * Use **device selection** to offload kernel workloads.
 * Decide when to use **basic parallel kernels** and **ND Range Kernels**.
 * Create a **host Accessor**.
 * Build a sample **SYCL application** through hands-on lab exercises.

Module 3: **DPCPP Unified Shared Memory**
 * Use new SYCL2020 features such as Unified Shared Memory to simplify programming.
 * Understand implicit and explicit way of moving memory using USM.
 * Solve data dependency between kernel tasks in optimal way.

Module 4: **DPCPP Sub Groups**
 * Understand advantages of using Subgroups in SYCL.
 * Take advantage of Subgroup algorithms for performance and productivity.
 * Use Subgroup Shuffle operations to avoid explicit memory operations.

Module 5: **Intel Advisor**
 * To show how Intel® Advisor can help deciding what part of the code should or should not be offloaded on the GPU.
 * To run Offload Advisor and generate a HTML report.
 * To read and understand the metrics in the report.
 * To get a performance estimation of your application on the target hardware.
 * To decide which loops are good candidate for offload.

Module 6: **Intel VTune_Profiler**
 * Profile a DPC++ application using the VTune™ profiling tool on Intel® DevCloud.
 * Understand the basics of VTune™ command line options for collecting data and generating reports.

Module 7: **DPCPP Library**
 * Explain oneDPL Parallel API Algorithms with examples.
 * Explain oneDPL Parallel API Iterators with examples.
 * Explain oneDPL Extension API Utility classes with examples.

Module 8: **DPCPP Reduction**
 * Understand how reductions can be performed with parallel kernels.
 * Take advantages **reduce group function** to do reduction at sub_group and work_group level.
 * Use **reduction object** to simplify reduction with parallel kernels.
 * Use **multiple** reductions in a single kernel.

Module 9: **DPCPP Buffers_And_Accessors_Indepth**
 * Explain Buffers and Accessors in depth.
 * Understand the Sub buffers and how to create and use Sub buffers.
 * Explain buffers properties and when to use_host_ptr, set_final_data and set_write_data.
 * Explain Accessors and the modes of accessor creation.
 * Explain host accessors and the different use cases of host accessors.

Module 10: **DPCPP Graphs Scheduling Data Management**
 * Utilize USM and Buffers and Accessors to apply Memory management and take control over data movement implicitly and explicitly.
 * Utilize different types of data dependences that are important for ensuring execution of graph scheduling.
 * Select the correct modes of dependences in Graphs scheduling.

Module 11: **Intel Distribution_for_GDB**
 * To show how the Intel® Distribution for GDB can help you debug GPU kernels.
 * Run the Intel Distribution for GDB.
 * Understand inferiors, threads, and SIMD lanes as shown in GDB.
 * Use different methods to examine local variables for different threads and lanes.

Module 12: **DPCPP Local_Memory_And_Atomics**
 * Use local memory to avoid repeated global memory access.
 * Understand the usage of group barriers to synchronize all work-items.
 * Use atomic operation to perform reduction.