Module 12: DPCPP Local Memory And Atomics
#########################################

This module demonstrates how to utilize a device's **shared local memory** to reduce latency in accessing data for kernel computation. The module also introduces **atomic operations**, which help avoid data race conditions when multiple work items are updating the same memory object.

Learning Objectives 
********************

* Use local memory to avoid repeated global memory access.

* Understand the usage of group barriers to synchronize all work items.

* Use atomic operations to perform reduction.
