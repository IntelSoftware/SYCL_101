std::thread
###########

This chapter talks about single_task. You will learn the following:

#. What is a C++ ``std::thread`` expression?
#. How to use the ``std::thread`` class in C++ code?
#. What are the objects of ``std::thread``?

Introduction
************

``std::thread`` is a C++ Standard Library class that refers to a sequence of execution within a program. Threads allow a program to perform multiple tasks concurrently, which can lead to better utilization of multi-core processors and improved overall program performance.

.. note::
    It's important to note that writing multithreaded code can be complex and error-prone. Proper synchronization and careful design are crucial to avoid issues like:
    
    * data races
    * deadlocks
    * unpredictable behavior

Utilization
***********

To learn how threads can be utilized, let's explore the ``std::thread`` with the example below. Remember that each ``std::thread`` object is an active thread of execution and has a unique thread id.

.. code-block:: cpp

    #include <iostream>
    #include <thread>

    void myFunction_1() {
        std::cout << "myFunction_1 is running" << std::endl;
    }

    void myFunction_2() {
        std::cout << "myFunction_2 is running" << std::endl;
    }

    int main() {
        std::thread thread_1(myFunction_1);    // We create the first thread
        std::thread thread_2(myFunction_1);    // We create the second thread
        std::thread thread_3(myFunction_2);    // We create the third thread
        thread_1.join();                       // Wait for thread_01 to finish
        thread_2.join();                       // Wait for thread_02 to finish
        thread_3.join();                       // Wait for thread_03 to finish
        return 0;
    }

First we create a functions we want to threads to execute. Next, inside of the main function, we create the thread_1, thread_2, and thread_3 with the use of ``std::thread`` library. Here we indicate what function to be assigned to each thread. 

In the part of code shown below note that the three threads are executing concurrently:

.. code-block:: cpp

    int main() {
        std::thread thread_1(myFunction_1);  // We create the first thread
        std::thread thread_2(myFunction_1);  // We create the second thread
        std::thread thread_3(myFunction_2);  // We create the third thread
        ...
    }

Lastly we tell the execution to stop until each of the threads finishes by using ``join()``:

.. code-block:: cpp

    int main() {
        ...
        thread_1.join();    // Program execution on hold until thread_1 finishes
        thread_2.join();    // Program execution on hold until thread_2 finishes
        thread_3.join();    // Program execution on hold until thread_3 finishes
        return 0;
    }

Two concurrent threads can execute the same function as we can see with thread_1 and thread_2 using myFunction_1.

We have introduced the class ``std::thread`` with its object ``join()`` but ``std::thread`` has more.  These are brief descriptions of the most relevant:

* ``get_id()``: This returns a numerical identifier that uniquely represents the thread object under consideration. A key application of this identifier is the facilitation of thread-local storage, a concept employed when managing static or global data that needs to be distinct for each individual thread.

* ``interrupt()``: This object compels the thread to come to an immediate halt. It does not receive the chance to proceed further; no additional tasks or operations will be performed. The scheduler will disregard it, even if it was in the midst of executing a task. We recommend caution when applying this command to a thread.

* ``yield()``: This one informs the scheduler that the current thread is temporarily yielding control and can be revisited later. In a preemptive scheduling context, this is valuable to ensure that threads without meaningful tasks do not monopolize execution time that could be more effectively utilized by other productive threads.

* ``join()``: This suspends the execution of the current thread until the thread being joined completes its execution. It serves as the primary mechanism for thread synchronization. A typical scenario for its application involves the main thread initiating a background task within a separate thread, performing other operations in the meantime, and then pausing to ensure that the background task has concluded before proceeding further.

