# innomatics-internship
internship assesments and tasks
# Advanced Python Task 1

This repository contains solutions to three algorithmic problems assigned as part of the internship program at Innomatics Research Labs. All problems are solved using Python 3.x and demonstrate proficiency in array manipulation, logic building, and space optimization.

---

##  Problem 1: Running Sum of 1D Array

**Description:**  
Given an array `nums`, return an array `runningSum` where each element is the sum of all previous elements including itself.

**Approach:**  
Used prefix sum logic with either a new list or in-place update.

**Example:**  
Input: `[1,2,3,4]`  
Output: `[1,3,6,10]`

---

##  Problem 2: Shuffle the Array

**Description:**  
Given an array in the form `[x1,x2,...,xn,y1,y2,...,yn]`, return `[x1,y1,x2,y2,...,xn,yn]`.

**Approach:**  
Used in-place list manipulation with `insert()` and `pop()` to avoid extra space.

**Example:**  
Input: `[2,5,1,3,4,7], n = 3`  
Output: `[2,3,5,4,1,7]`

---

##  Problem 3: Kids With the Greatest Number of Candies

**Description:**  
Given an array `candies` and an integer `extraCandies`, return a boolean array indicating whether each kid can have the greatest number of candies after receiving the extra ones.

**Approach:**  
Compared each kid's total with the current maximum using list comprehension.

**Example:**  
Input: `candies = [2,3,5,1,3], extraCandies = 3`  
Output: `[True, True, True, False, True]`

---

## 📂 Folder Structure

