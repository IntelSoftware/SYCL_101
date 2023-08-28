Multithreading
#############################

Introduction
************

**Multithreading** is a feature that allows concurrent execution of two or more parts of a program for
maximum utilization of the resources. Each part of such a program is called a thread. So, threads are 
lightweight processes within a bigger process.

In C++, multithreading was introduced in C++11, but became a part of the standard library (STL) in C++17. 

Why use multithreading?[[[text seems too small]]]
=======================

Basic concepts of multithreading
********************************

Concurrency and parallelism
============================

Before we delve deeper into the topic of multithreading in C++, let's start by explaining the 
terms **concurrency** and **parallelism**. They are often mixed, but it's important to understand the 
difference between them.

Put simply, concurrency is about dealing with lots of things[[[between this phrase ad the next, this says "dealing with lots of things" and the next says "doing lots of things." That's not clear enough to tell the difference between them]]], while parallelism is about 
doing lots of things at once. But what is important, both  parallelism and concurrency can occur 
separately as well as together, depending on the context.



C++ multithreading syntax
*************************

Now, let's get back to multithreading itself. C++ multithreading involves creating and using thread 
objects, seen as :code:`std::thread` in code, to carry out delegated sub-tasks independently.

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

Let's analyze this code step by step. 

#. The first step was to import the necessary library form STL — it contains all the classes and functions 
   related to the C++ multithreading like :code:`std::thread` class.
#. The next step was to declare a function called from thread — all threads must be given a function 
   to complete at their creation.
#. The next step is to initialize a thread and have it execute a prepared function — we are using 
   default executor.
#. At the end, we are using :code:`join()` multithreading command — this task pauses the main function's thread until the specified thread. Without :code:`join()` here, the 
   main thread would finish its task before :code:`t` would complete :code:`callFromThread`, 
   resulting in an error.

Multiple threads[[[can it be Multithread?]]] execution
===========================

.. code-block:: cpp
   
   #include <iostream>
   #include <thread>
   #include <vector>
   
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
     
     std::vector<std::thread> threads;
    
     for (int i = 0; i < s.size(); i++) {
       threads.push_back(std::thread(print, i, s[i]));
     }
    
     for (auto &th : threads) {
       th.join();
     }

     return 0;
   }


Detaching[[[TBD?]]]
=========


Shared resources
================
