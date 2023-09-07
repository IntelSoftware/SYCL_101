SYCL Essentials: Learning Objectives
====================================

Module 1: **oneAPI Intro**
 * Explain how the **oneAPI** programming model can solve the challenges of programming in a heterogeneous world. 
 * Use oneAPI projects to enable your workflows.
 * Understand the **SYCL** language and programming model.
 * Familiarize yourself with Jupyter Notebooks for training throughout the course.

Module 2: **DPCPP Program Structure**
 * Explain the **SYCL** fundamental classes.
 * Use **device selection** to offload kernel workloads.
 * Decide when to use **basic parallel kernels** and **ND Range Kernels**.
 * Create a **host accessor**.
 * Build a sample **SYCL application** through hands-on lab exercises.

Module 3: **DPCPP Unified Shared Memory**
 * Use new SYCL2020 features such as Unified Shared Memory (USM) to simplify programming.
 * Understand implicit and explicit ways of moving memory using USM.
 * Solve data dependency between kernel tasks optimally.

Module 4: **DPCPP Sub Groups** 
 * Understand the advantages of using sub-groups in SYCL.
 * Take advantage of sub-group algorithms for performance and productivity.
 * Use Sub Group Shuffle operations to avoid explicit memory operations.

Module 5: **Intel® Advisor**
 * Intel® Advisor can help deciding what part of the code should or should not be offloaded on the GPU.
 * Run Offload Advisor and generate an HTML report.
 * Read and understand the metrics in the report.
 * Get a performance estimation of your application on the target hardware.
 * Decide which loops are good candidates for offload.

Module 6: **VTune™ Profiler**
 * Profile a DPC++ application using the VTune™ Profiler tool on Intel® DevCloud.
 * Understand the basics of VTune command-line options for collecting data and generating reports.

Module 7: **DPCPP Library**
 * Explain oneDPL Parallel API Algorithms with examples.
 * Explain oneDPL Parallel API Iterators with examples.
 * Explain oneDPL Extension API Utility classes with examples.

Module 8: **DPCPP Reduction**
 * Understand how reductions can be performed with parallel kernels.
 * Take advantage of the **reduce group function** to make reductions at the sub group and work group level.
 * Use **reduction object** to simplify reduction with parallel kernels.
 * Use **multiple** reductions in a single kernel.

Module 9: **DPCPP Buffers And Accessors In Depth**
 * Explain buffers and accessors in depth.
 * Understand how to create and use sub-buffers.
 * Explain buffer properties and when to use host ptr, set final data, and set write data.
 * Explain accessors and the modes of accessor creation.
 * Explain host accessors and the different use cases of host accessors.

Module 10: **DPCPP Graphs Scheduling Data Management**
 * Utilize USM, buffers, and accessors to apply memory management and take control over data movement implicitly and explicitly.
 * Utilize different types of data dependencies that are important for ensuring execution of graphs scheduling.
 * Select the correct modes of dependencies in graphs scheduling.

Module 11: **Intel® Distribution for GDB**
 * Show how Intel® Distribution for GDB can help you debug GPU kernels.
 * Run the Intel Distribution for GDB.
 * Understand inferiors, threads, and SIMD lanes as shown in GDB.
 * Use different methods to examine local variables for different threads and lanes.

Module 12: **DPCPP Local Memory And Atomics**
 * Use local memory to avoid repeated global memory access.
 * Understand the use of group barriers to synchronize all work items.
 * Use atomic operation to perform reduction.
