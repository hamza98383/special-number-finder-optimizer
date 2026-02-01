# 🔢 Special Number Finder: Prime & Palindrome Optimizer

A high-performance Python-based computational tool designed to identify "Special Numbers"—integers that are simultaneously **prime** and **palindromic**. This project demonstrates advanced proficiency in **Algorithm Optimization**, **Mathematical Logic**, and **Computational Efficiency**.

---

## 🚀 Performance Breakthrough

The core focus of this project was transitioning from a brute-force approach to a highly optimized generation-based strategy.

* **Before Optimization:** Processing ranges up to 1 trillion took approximately **50 minutes**.
* **After Optimization:** The same range is processed in just **7 seconds**.
* **Total Efficiency Gain:** Over **428,000% reduction** in execution time.

---

## 📌 Project Overview

Instead of checking every single integer in a range (Brute Force), this system utilizes a "Generation over Search" methodology. It generates potential palindromic candidates first and then filters them through an optimized primality test.

### 🔍 Key Technical Features
* **Optimized Primality Testing:** Implemented a square-root limit trial division and skipped even numbers to minimize CPU cycles.
* **Direct Palindrome Generation:** Used string manipulation and mirroring techniques to generate candidate numbers directly, bypassing billions of non-palindromic integers.
* **Performance Tracking:** Integrated the Python `time` module to provide precise execution benchmarks.
* **Intelligent Data Output:** Automatically adjusts display logic to show a preview (first and last three numbers) when result sets are large.

---

## 🛠️ Logic & Methodology

1. **Candidate Generation:** The algorithm builds palindromes using string slicing and mirroring to cover both even and odd-length numbers.
2. **Primality Filtering:** Each candidate is verified using an optimized complexity function.
3. **Benchmarking:** Start and end timestamps are recorded to measure real-time efficiency.

---

## 👥 Authors & Contribution
This project was a collaborative effort by our group:
* **Venkata Ramachandra Madhav Peddada** (100%)
* **Hamza Ali Khan** (100%)
* **Ahmed Farah** (100%)
* **Mohammed Jahidul Ahmed** (90%)
* **Vanessa Blyznyuk Petrunyak** (85%)

---

## 🔗 Connect with Me
🚀 **GitHub:** [https://github.com/hamza-ali-khan](https://github.com/hamza-ali-khan)  
💼 **LinkedIn:** [https://www.linkedin.com/in/hamza-ali-khan-69116820b/](https://www.linkedin.com/in/hamza-ali-khan-69116820b/)

---
*Note: Developed to demonstrate how proper algorithmic strategy can solve "impossible" brute-force problems.*
