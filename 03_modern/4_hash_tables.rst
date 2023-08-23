Hash tables
############

This chapter talks about hash tables. You will learn:

#. What is hash table and why to use it?
#. What is hashing and hash function?
#. What are the C++ standard library implementation of hash tables?


Introduction
************

The **hash table** is a data structure that stores elements in key-value pairs.
**Key** is un unique value used to compute table index, when **value** is a data
associated with the key.

The benefit of using a hash table is its very fast access time. Typically, 
the time complexity is a constant (O(1) access time).

Hashing function
================

Like it was said already, in a hash table new index in processed using the key 
and the corresponding to this key value is stored in the index. This process 
is called hashing and the function performing this operation is called **hashing function**.

Let's understand it better with example.

Please consider hashing function as operation modulo 10 and set of key-value pairs 
to insert to hash table :code:`{{15, 25}, {23, 63}, {12, 22}, {48, 78}, {30, 0}}`.

.. list-table:: 
   :widths: 25 50 25
   :header-rows: 1
   :align: center

   * - key
     - index based on hashing function 
     - value
   * - 15
     - 15 % 10 = 5
     - 25
   * - 23
     - 23 % 10 = 3
     - 63
   * - 12
     - 12 % 10 = 2
     - 22
   * - 48
     - 48 % 10 = 8
     - 78
   * - 30
     - 30 % 10 = 0
     - 0

It means that the positions in the hash table will be as following:

.. list-table:: 

   * - position
     - 0
     - 1
     - 2
     - 3
     - 4
     - 5
     - 6
     - 7
     - 8
     - 9
   * - value
     - 0
     - 
     - 22
     - 63
     - 
     - 25
     - 
     - 
     - 78
     - 

As you can see there a big chance that more than one key value will compute the same index. 
To solve this problem, in standard library values are stored in a buckets - so multiple values
can be under the same index.


C++ standard library hash tables
********************************

In C++ standard library are available 4 different hash tables. They are the equivalents of 
standard containers but with hashing function:

* std::unordered_set (equivalent of std::set)
* std::unordered_multiset (equivalent of std::multiset)
* std::unordered_map (equivalent of std::map)
* std::unordered_multimap (equivalent of std::multimap)

We will take a look at all of them one by one.

Set
===

Let's start with **std::unordered_set**. According to C++ reference:

    :code:`std::unordered_set` is an associative container that contains 
    a set of unique objects of type Key. Search, insertion, and 
    removal have average constant-time complexity.

So the mos important information about std::unordered_set is that it contains 
**unique objects**, they are type of **key** and average access time is **constant**.

Example :code:`std::unordered_set` declaration is shown in code below:

.. code-block:: cpp
   
   std::unordered_set<int> n;

To initialize an :code:`std::unordered_set` we can simply assign values to it at the time of declaration.
Please remember that given values have to be unique.

.. code-block:: cpp
   
   std::unordered_set<int> n {0, 1, 2, 3, 4};

As in other standard containers we can conduct on it operations like:

* size(),
* insert(...),
* erase(...),
* count(...),
* find(...),
* iteration over elements.

Very similar to :code:`std::unordered_set` is **std::unordered_multiset**. 
Let's start with definition:

    :code:`std::unordered_multiset` is an associative container that contains set 
    of possibly non-unique objects of type Key. Search, insertion, and 
    removal have average constant-time complexity.

It means that the only different between :code:`std::unordered_set` and :code:`std::unordered_multiset` is
that the second one allows to store multiple the same keys.

Example :code:`std::unordered_multiset` declaration is shown in code below:

.. code-block:: cpp
   
   std::unordered_multiset<int> n;

To initialize an :code:`std::unordered_multiset` we can simply assign values to it at the time of declaration.
This time the values may be repeated.

.. code-block:: cpp
   
   std::unordered_multiset<int> n {0, 1, 2, 1, 2};

Map
===

Now, we will move to the map containers, starting with **std::unordered_map**. 
According to C++ reference:

    :code:`std:unordered_map` is an associative container that contains key-value pairs with unique 
    keys. Search, insertion, and removal of elements have average constant-time complexity.

It means that the most important information about :code:`std::unordered_map` is that is stores 
**key-value pairs**, where **key is unique** and the average access time is **constant**.

Example :code:`std::unordered_map` declaration where key is type of int and value is type of 
:code:`std::string` is shown in code below:

.. code-block:: cpp
   
   std::unordered_map<int, std::string> m;

To initialize an :code:`std::unordered_map` we can simply assign values to it at the time of declaration.
Please remember that the key value have to be unique.

.. code-block:: cpp
   
   std::unordered_map<int, std::string> m {{0, "zero"}, 
                                           {1, "one"}, 
                                           {2, "two"}};

Similarly, as with set container, **std::unordered_multimap** and :code:`std::unordered_map` have 
a lot in common. Starting with C++ reference definition:

    :code:`std::unordered_multimap` is an unordered associative container that supports equivalent keys 
    (an unordered_multimap may contain multiple copies of each key value) and that associates values 
    of another type with the keys. (...) Search, insertion, and removal have average constant-time 
    complexity.

The only difference is that :code:`std::unordered_multimap` allow for keys to be repeated.

Example :code:`std::unordered_multimap` declaration where key is type of int and value is type of 
:code:`std::string` is shown in code below:

.. code-block:: cpp
   
   std::unordered_multimap<int, std::string> m;

To initialize an :code:`std::unordered_multimap`, as before we can assign values to it at the time 
of declaration. This time the keys don't need to be unique.

.. code-block:: cpp
   
   std::unordered_multimap<int, std::string> m {{0, "zero"}, 
                                                {1, "one"}, 
                                                {2, "two"}, 
                                                {0, "three"}};

And of course, it supports several operations like other standard library containers. 

Summary
*******

As the summary fot this module we would like to show you the comparison 
of the all standard library associative containers:

.. list-table:: 
   :header-rows: 1

   * - Container
     - Sorted
     - Value
     - Identical keys possible
     - Average access time
   * - std::set
     - yes
     - no
     - no
     - logarithmic
   * - std::unordered_set
     - no
     - no
     - no
     - constant
   * - std::map
     - yes
     - yes
     - no
     - logarithmic
   * - std::unordered_map
     - no
     - yes
     - no
     - constant
   * - std::multiset
     - yes
     - no
     - yes
     - logarithmic
   * - std::unordered_multiset
     - no
     - no
     - yes
     - constant
   * - std::multimap
     - yes
     - yes
     - yes
     - logarithmic
   * - std::unordered_multimap
     - no
     - yes
     - yes
     - constant
