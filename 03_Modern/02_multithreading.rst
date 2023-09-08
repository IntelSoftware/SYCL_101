Multithreading
#############################

This chapter talks about multithreading. You will learn the following:

#.	What is multithreading?
#. What are the benefits of using multithreading?
#. How multithreading is implemented in C++?
#. How to launch, join and detach threads?
#. What are the problems with multithreading? 

Introduction
************

**Multithreading** is a feature that allows concurrent execution of two or more parts of a program for maximum utilization of the resources. Each part of such a program is called  thread. So, threads are lightweight processes within a bigger process.  In C++, multithreading was introduced in C++11, but became a part of the standard library (STL) in C++17. 

Why use Multithreading?
***********************

With the development of hardware and the introduction of multiple cores, the use of multithreading started to be very important in terms of application efficiency. 

There are various reasons to use multithreading, among others:

* Higher throughput
* Better responsiveness
* Resource efficiency
* Parallelism

It is important to remember that even when using more and more threads, due to potential overhead the application may not always run faster.

Basic Concepts of Multithreading
********************************

Let's start with some basics concepts, like process and thread.

**Process** is what executes the program. Each process is able to run concurrent subtasks called threads.

**Thread**, as it was already explained, is a sub-task of the process. It can give an illusion that the application is performing multiple things all at once. Without threads there will be a need to write one program per task and synchronize multiple of them at the operating system level.

Concurrency and Parallelism
============================

Before we delve deeper into the topic of multithreading in C++, let's start by explaining the terms **concurrency** and **parallelism**. They are often mixed, but it's important to understand their differences.

Put simply, **concurrency** is about multiple tasks which start, run, and complete in overlapping time periods, in no specific order, while parallelism is about multiple tasks or subtasks of the same task that run at the same time on hardware with multiple computing resources.  It is important to understand that both parallelism and concurrency can occur separately as well as together depending on the context. 

C++ Multithreading Syntax
*************************

Now, let's get back to multithreading itself. C++ multithreading involves creating and using thread objects, seen as :code:`std::thread` in code, to carry out delegated sub-tasks independently.

Single-thread execution
========================

Creating and launching a thread is really simple. Let's look at the simple example with threads:

.. code-block:: cpp
   
   #include <iosteram>
   // 1. We need to add threads header to work with threads in C++
   #include <threads>

   // 2. Create function that will be called from thread
   void callFromThread() {
      std::cout << "Hello world!\n";
   }

   int main() {
      // 3. Initialize thread and execute
      std::thread t(callFromThread);

      // 4. Join thread t with the main thread 
      t.join();

      return 0;
   }

Let's analyze this code step by step:

#. The first step was to import the necessary library form STL — it contains all the classes and functions related to the C++ multithreading like :code:`std::thread` class.
#. The next step was to declare a function called from thread — all threads must be given a function to complete at their creation.
#. The next step is to initialize a thread and have it execute a prepared function — we are using default executor.
#. At the end, we are using :code:`join()` multithreading command — this task pauses the main function's thread until the specified thread. Without :code:`join()` here, the main thread would finish its task before :code:`t` would complete :code:`callFromThread`, resulting in an error.

Multithread execution
=====================

Similarly to the single thread, we can create and execute multiple of them. See the code below:

.. code-block:: cpp
   
   #include <iostream>
   // 1. We need to add threads header to work with threads in C++
   #include <thread>
   #include <vector>

   // 2. Create function that will be called from thread
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
    
     // 4. Join threads with the main thread 
     for (auto &th : threads) {
       th.join();
     }

     return 0;
   }

The code has similar structure as with single thread:

#. First, we imported the :code:`thread` library.
#. Then, we created a function that will be called form the single thread. In this example the function is printing given string and given number.
#. Then we initialize the thread and execute them. We created the :code:`std::vector<std::threads>` to store all created threads. Later we pushed back initialized with created function threads.
#. The last step was to join all the threads with the main one. 

In this case, as we are using multiple threads, it is important to mention, that even as we initialize the threads in the specific order, there is no guarantee that the will execute in that order. It means that every time you run this program, you can receive different output. 


Joining and Detaching Threads
==============================

We already used :code:`join()` on the threads. But take a deeper look on join and detach operations.

Joining threads make them waiting for each other. Imagine that once a thread is started then another thread can wait for this new thread to finish. In that scenario, we are calling :code:`join()` function on the :code:`std::thread` object, like in example below:

.. code-block:: cpp
   
   std::thread th(functionPointer);

   // ...

   th.join(); // waiting for the thread th to finish

In addition to **joining** threads, one can also **detach** them. The detached thread allows it to execute independently from other threads. A detached thread will continue without blocking or synchronizing executing independently. For this, we need to call :code:`detach()` on the :code:`ste::thread` object. See code below:

.. code-block:: cpp
   
   std::thread th(functionPointer);

   th.detach(); // continue without waiting for thread th to finish

Remember that after calling :code:`detach()`, :code:`std::thread` object is no longer associated with the actual thread of execution.

Problems with Multithreading
******************************

When running multithreaded programs we can face problems with **access to shared data** by multiple threads. Simultaneous access to the same resource can lead to race conditions, errors and chaos in programs. This problem occurs mostly due to the consequences of modifying shared data.  There will be no issue if the data we share is read-only because the data read by one thread is unaffected by whether or not another thread is reading the same data. However, once data is shared between threads and one or more threads begin modifying the data, difficulties arise.  We will take a look at some different possible problems with shared data that can happen in multithreading programming.

Deadlock
===========

Deadlock is a situation where none of the threads can proceed with operation because each waits for another. Imagine the situation where we have two threads (T1 and T2) and two resources (R1 and R2). Thread T1 requires resource R1, and thread T2 requires resource R2. In that situation deadlock can arise when T1 is holding on R2 and waiting for R1 while at the same time, thread T2 is holding R1 and waiting for R2. This situation is depicted in the image below with the circle waiting.

.. figure:: /_images/deadlock.png

There is a general guide to avoid deadlocks. Simply don't wait for another thread if there is a chance it is waiting for you. 

Race Conditions
================

Race condition is the situation when two concurrent threads access the same resources and unintentionally produces different results depending on the execution order.

Imagine having two threads doing different operations. The fist one takes a value and overwrites it with the square of it and then the second one takes the value and overwrites it with the doubled value. Depending on the order of the thread execution the final value will be different as in the image below:

.. figure:: /_images/race-condition.png

As you can see in the first scenario, thread 1 executed first, so its result was doubled which resulted in 50. In the second scenario, thread 2 was executed first so its resulted was squared which resulted in 100 at the end.

To avoid race conditions, any operation on a shared resource must be executed atomically. One way to achieve atomicity is by using critical sections — mutually exclusive parts of the program.

Summary
********

To summarize, multithreading is used for parallel execution of multiple tasks. It can increase the efficiency of the program but also can be tricky when dealing with shared data. This was a very short introduction to multithreading. There is still much more to be learned.