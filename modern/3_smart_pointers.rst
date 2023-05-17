Smart Pointers
#############################

This chapter talks about smart pointers. You will learn:

#. What are smart pointers?
#.	When to use different smart pointer type?
#.	Why should you use smart pointers?


What are the smart pointers and when to use them?
****************************************************

#.	It's a type whose values can be used like pointers, but which provides the additional feature of automatic memory management. We have 3 types of smart pointers: std::unique_ptr, std::shared_ptr and std::weak_ptr.
#.	In general smart pointers are used in code which involves tracking the ownership of a piece of memory, allocating or de-allocating it.
#.	Regular pointers can be still used in code with oblivious memory ownership. This would typically be in functions which get a pointer from someplace else and do not allocate nor de-allocate, and do not store a copy of the pointer which outlasts their execution.

std::unique_ptr 
***************

smart pointer with unique object ownership semantics

#.	syntax
#.	usage with explanation
#.	std::make_unique

std::shared_ptr 
***************

smart pointer with shared object ownership semantics

#.	syntax
#.	usage with explanation
#.	std::make_shared

std::weak_ptr 
***************

weak reference to an object managed by std::shared_ptr

#.	syntax
#.	usage with explanation in relation to std::shared_ptr

Summary
=======
