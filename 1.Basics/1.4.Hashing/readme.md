# 🔐 Hashing in Python

Hashing is a process of converting data (like a string or file) into a fixed-size integer or hexadecimal value using a **hash function**.
It’s commonly used for data lookups, password storage, integrity checks, and cryptography.




---

## 🧠 What is Hashing?

Hashing maps data of arbitrary size to a fixed-size value called a **hash value** or **digest**.
A good hash function should:
- Produce the same output for the same input every time
- Distribute values uniformly
- Be fast to compute
- Be irreversible (for secure hashes)

---

## ⚙️ Built-in `hash()` Function

Not available in all the versions

Python has a built-in `hash()` function for hashing immutable objects like strings, tuples, and numbers.

```python
# Example
print(hash("Python"))   # Output: varies between runs
print(hash(12345))
print(hash((1, 2, 3)))
