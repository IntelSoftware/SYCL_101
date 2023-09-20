Multithreading
##############

This chapter covers multithreading. You will learn the following:

#. What is multithreading?
#. What are the benefits of multithreading?
#. How multithreading is implemented in C++?
#. How to launch, join, and detach threads?
#. What are the problems with multithreading? 

Introduction
************

**Multithreading** is a feature that allows concurrent execution of two or more parts of a program for maximum utilization of the resources. Each part of such a program is called thread. So, threads are lightweight sub-processes within a bigger process.  In C++, multithreading was introduced in C++11, but became a part of the standard library (STL) in C++17. 

Why Use Multithreading?
***********************

With the introduction of multiprocessor and multicore hardware, the use of multithreading started to be very important in terms of application efficiency. 

There are various reasons to use multithreading:

* Higher throughput
* Better responsiveness
* Resource efficiency
* Parallelism

It is important to remember that even when using more and more threads, due to potential overhead the application may not always run faster.

Basic Concepts of Multithreading
********************************

Let's start with some basics concepts, like process and thread.

**Process** is what executes the program. Each process is able to run concurrent subtasks called threads.

**Thread**, as it was already explained, is a sub-task of the process. It can give the illusion that the application is performing multiple things all at once. Without threads, there will be a need to write one program per task and synchronize them at the operating system level.

Concurrency and Parallelism
============================

Before we delve deeper into the topic of multithreading in C++, let's start by explaining the terms **concurrency** and **parallelism**. They are often used interchangeably, but it's important to understand their differences.

Put simply, **concurrency** is about multiple tasks which start, run, and complete in overlapping time periods, in no specific order, while parallelism is about multiple tasks or subtasks of the same task that run at the same time on hardware with multiple computing resources.  It is important to understand that both parallelism and concurrency can occur separately as well as together depending on the context. 

C++ Multithreading Syntax
*************************

Now, let's get back to multithreading itself. C++ multithreading involves creating and using thread objects, seen as :code:`std::thread` in code, to carry out delegated sub-tasks independently.

Creating a Thread
=================

Creating and launching a thread is really simple, e.g.:

.. code-block:: cpp
   
   #include <iostream>
   // 1. We need to add the threads header to work with threads in C++
   #include <threads>

   // 2. Create a function that will be mapped to a thread
   void callFromThread() {
      std::cout << "Hello world!\n";
   }

   int main() {
      // 3. Initialize thread and execute
      std::thread my_thread(callFromThread);

      // 4. Rejoin thread to the main thread 
      my_thread.join();

      return 0;
   }

Let's analyze this code step-by-step:

#. The first step imported the necessary library from the STL — it contains all the classes and functions related to the C++ multithreading like :code:`std::thread` class.
#. The next step declared a function that was mapped to the thread — all threads must be given a function to complete at their creation.
#. The next step initialized a thread to execute the function — we are using default executor.
#. At the end, we used :code:`join()` multithreading command — this task pauses the main function's thread until the specified thread completes. Without :code:`join()`, the main thread could finish its task and terminate the process before the thread executing completes :code:`callFromThread`. This race condition could result in an error.

Creating Multiple Threads
=========================

The previous example created a single thread (in addition to the main thread). We can just as easily create and execute multiple threads, e.g.:

.. code-block:: cpp
   
   #include <iostream>
   // 1. We need to add threads header to work with threads in C++
   #include <thread>
   #include <vector>

   // 2. Create a function that will be mapped to a thread
   void print(int n, const std::string &str)  {
     std::string msg = std::to_string(n) + " : " + str + '\n';
     std::cout << msg;
   }
    
   int main() {
     std::vector<std::string> s = {
         "SYCL 101",
         "Intel",
         "multithreading",
         "education"
     };
     
     // 3. Initialize threads and execute them
     std::vector<std::thread> threads;
     for (int i = 0; i < s.size(); i++) {
       threads.push_back(std::thread(print, i, s[i]));
     }
    
     // 4. Rejoin threads to the main thread 
     for (auto &th : threads) {
       th.join();
     }

     return 0;
   }

This code is similar to the previous one-thread example:

#. First, we imported the :code:`thread` library.
#. Then, we created a function that was mapped to the threads. In this example, the function is printing a given string and number.
#. Then, we initialized the threads and executed them. We created the :code:`std::vector<std::threads>` to store the thread handles.
#. The last step rejoined the threads to the main thread. 

In this case, as we are using multiple threads, it is important to mention that even though we initialized the threads in sequential order, there is no guarantee that they will execute in that order. You might see different output every time you run this program.


Joining and Detaching Threads
=============================

We've already used :code:`join()` on the threads, but let's take a deeper look at join and detach operations.
Joining threads is a form of synchronization that makes them wait for each other. Imagine that a thread is started, then another thread waits for this new thread to finish. In that scenario, we are calling the :code:`join()` function on the :code:`std::thread` object, like in the example below:

.. code-block:: cpp
   
   std::thread th(functionPointer);

   // ...

   th.join(); // waiting for the thread th to finish

In addition to **joining** threads, one can also **detach** them. A detached thread will continue without blocking or synchronizing its execution with any other threads. For this, we call :code:`detach()` on the :code:`ste::thread` object:

.. code-block:: cpp
   
   std::thread th(functionPointer);

   th.detach(); // continue without waiting for thread th to finish

Remember that after calling :code:`detach()`, :code:`std::thread` object is no longer join with other threads in the process.

Commonly Used Methods of the Thread Class
=========================================

We have introduced the class ``std::thread`` with its ``join()`` method, but ``std::thread`` has more.  These are brief descriptions of the most relevant methods:

* ``get_id()``: This returns a unique numerical identifier for the calling thread. A key application of this identifier is the facilitation of synchronization and thread-local storage, which is often used to managing static or global data that needs to be distinct for each individual thread.

* ``interrupt()``: This method compels the thread halt immediately. The scheduler will ignore this thread, even if it is in the middle of a task. We recommend caution when using this method.

* ``yield()``: This method informs the scheduler that the current thread is temporarily yielding control and can be revisited later. In a preemptive scheduling context, this is valuable to ensure that threads with lower priority tasks do not monopolize execution that could be more effectively utilized by other productive threads.

* ``join()``: This suspends the execution of the current thread until the thread being joined completes its execution. It serves as the primary mechanism for thread synchronization. A typical scenario for its application involves the main thread initiating a background task within a separate thread, performing other operations in the meantime, and then pausing to ensure that the background task has concluded before proceeding further.


Problems with Multithreading
****************************

When running multithreaded programs we can face problems with **access to shared data** by multiple threads. Simultaneous access to the same resource can lead to race conditions, errors, and chaos in programs. This problem occurs mostly due to the consequences of modifying shared data.  There will be no issue if the data we share is read-only because the data read by one thread is unaffected by whether or not another thread is reading the same data. However, once data is shared between threads and one or more threads begin modifying the data, difficulties arise.  We will take a look at some different possible problems with shared data that can happen in multithreading programming.

Deadlock
========

Deadlock is a situation where a thread cannot proceed because it is waiting for a resource that will never become available. Imagine the situation where we have two threads (T1 and T2) and two resources (R1 and R2). Thread T1 requires resource R1, and thread T2 requires resource R2. In that situation deadlock can arise when T1 is holding on R2 and waiting for R1 while at the same time, thread T2 is holding R1 and waiting for R2. This situation is depicted in the image below, which illustrates a bad locking cycle.

.. figure:: /_images/deadlock.png

To avoid such deadlocks, shared resources should be acquired and released in reverse order. For example, a thread cannot acquire R2 unless it already holds R1,
and it cannot release R1 until it first releases R2.


Race Conditions
===============

A race condition occurs when threads can modify a shared resource in indeterminate order. This can produce incorrect results when correct results depend on a particular execution order. Imagine two threads doing different operations. The first takes a value and overwrites it with its square while the second takes the value and overwrites its double. Depending on the order of thread execution, the final value will be different:

.. figure:: /_images/race-condition.png

As you can see in the first scenario, Thread 1 executed first so its result was doubled, which resulted in a final value of 50. In the second scenario, Thread 2 executed first so its resulted was squared, which resulted in a final value of 100.

To avoid race conditions, any operation that modifies a shared resource must be synchronized.

Summary
*******

To summarize, multithreading is used to express concurrency in an algorithm and to execute independent tasks in parallel. It can increase the efficiency of a program but can also be tricky when dealing with shared resources. This was a very short introduction to multithreading. There is still much more to be learned.
