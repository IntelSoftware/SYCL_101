Hash Tables
############

This chapter talks about hash tables. You will learn the following:

#. What is a hash table and why should I use it?
#. What is hashing and hash function?
#. What are the C++ standard library implementations of hash tables?


Introduction
************

A **hash table** is a data structure that stores elements in key-value pairs.
**Key** is a unique value used to compute a table index, when **value** is data
associated with the key.

The benefit of using a hash table is that it has quick access time. Typically, 
the time complexity is a constant (O(1) access time).

Hashing function
================

As stated previously, in a hash table, a new index is processed using the key 
and the corresponding value to this key is stored in the index. This process 
is called hashing and the function performing this operation is called **hashing function**.

Here's an example.

Please consider a hashing function as operation mod 10 and a set of key-value pairs 
to insert into hash table :code:`{{15, 25}, {23, 63}, {12, 22}, {48, 78}, {30, 0}}`.

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

This means that the positions in the hash table will be the following:

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

As you can see, there's a good chance that more than one key value will compute the same index. 
To solve this problem, in a standard library, values are stored in buckets — so multiple values
can be under the same index.


C++ standard library hash tables
********************************

In the C++ standard library there are four different hash tables available. They are the equivalents of 
standard containers but with a hashing function:

* std::unordered_set (equivalent of std::set)
* std::unordered_multiset (equivalent of std::multiset)
* std::unordered_map (equivalent of std::map)
* std::unordered_multimap (equivalent of std::multimap)

Let's look at all of them one by one.

Set
===

Let's start with **std::unordered_set**. According to C++ reference:

    :code:`std::unordered_set` is an associative container that contains 
    a set of unique objects of type Key. Search, insertion, and 
    removal have average constant-time complexity.

The most important aspect about std::unordered_set is that it contains 
**unique objects**, which are of type **key** and average access time is **constant**.

An example of a :code:`std::unordered_set` declaration is shown in the code below:

.. code-block:: cpp
   
   std::unordered_set<int> n;

To initialize :code:`std::unordered_set`, we can simply assign values to it at the time of declaration.
Please remember that the given values have to be unique.

.. code-block:: cpp
   
   std::unordered_set<int> n {0, 1, 2, 3, 4};

As in other standard containers, we can conduct operations like the following:

* size(),
* insert(...),
* erase(...),
* count(...),
* find(...),
* iteration over elements.

Similar to :code:`std::unordered_set` is **std::unordered_multiset**. 
Let's start with definition:

    :code:`std::unordered_multiset` is an associative container that contains a set 
    of possibly non-unique objects of type Key. Search, insertion, and 
    removal have average constant-time complexity.

This means that the only difference between :code:`std::unordered_set` and :code:`std::unordered_multiset` is
that the second one allows multiple keys to be stored.

An example of the :code:`std::unordered_multiset` declaration is shown in code below:

.. code-block:: cpp
   
   std::unordered_multiset<int> n;

To initialize :code:`std::unordered_multiset`, we can simply assign values to it at the time of declaration.
This time the values may be repeated.

.. code-block:: cpp
   
   std::unordered_multiset<int> n {0, 1, 2, 1, 2};

Map
===

Now, we will move to the map containers, starting with **std::unordered_map**. 
According to C++ reference:

    :code:`std:unordered_map` is an associative container that contains key-value pairs with unique 
    keys. Search, insertion, and removal of elements have average constant-time complexity.

This means that the most important information about :code:`std::unordered_map` is that it stores 
**key-value pairs**, where **key is unique** and the average access time is **constant**.

The code below shows an example of a :code:`std::unordered_map` declaration where key is of type :code:`int` and value is of type 
:code:`std::string`:

.. code-block:: cpp
   
   std::unordered_map<int, std::string> m;

To initialize :code:`std::unordered_map`, we can simply assign values to it at the time of declaration.
Please remember that the key values have to be unique.

.. code-block:: cpp
   
   std::unordered_map<int, std::string> m {{0, "zero"}, 
                                           {1, "one"}, 
                                           {2, "two"}};

Similarly, as with a set container, **std::unordered_multimap** and :code:`std::unordered_map` have 
a lot in common. Let's look at the C++ reference definition:

    :code:`std::unordered_multimap` is an unordered associative container that supports equivalent keys 
    (an unordered_multimap may contain multiple copies of each key value) and that associates values 
    of another type with the keys. (...) Search, insertion, and removal have average constant-time 
    complexity.

The only difference is that :code:`std::unordered_multimap` allows for keys to be repeated.

The code below shows an example of a :code:`std::unordered_multimap` declaration where key is of type :code:`int` and value is of type 
:code:`std::string`:

.. code-block:: cpp
   
   std::unordered_multimap<int, std::string> m;

To initialize :code:`std::unordered_multimap`, as before, we can assign values to it at the time 
of declaration. This time the keys don't need to be unique.

.. code-block:: cpp
   
   std::unordered_multimap<int, std::string> m {{0, "zero"}, 
                                                {1, "one"}, 
                                                {2, "two"}, 
                                                {0, "three"}};

And of course, it supports several operations like other standard library containers. 

Summary
*******

To summarize this module, we would like to compare
all of the standard library associative containers.

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
