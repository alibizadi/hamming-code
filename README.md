# Hamming Code
Implementing hamming code algorithm using PySide2 and QML

## Content
- [What's Hamming Code](#What's%20Hamming%20Code)
- [Algorithm](#Algorithm)
- [Output](#Output)

## What's Hamming Code
Hamming code is an error correction system that can detect and correct errors when data is stored or transmitted. It requires adding additional parity bits with the data. It is commonly used in error correction code (ECC) RAM.
[Read more...](https://www.techtarget.com/whatis/definition/Hamming-code#:~:text=Hamming%20code%20is%20an%20error,correction%20code%20(ECC)%20RAM.)

## Algorithm
First we need to know number of prity bits (k). We use the n <= 2^k - k - 1 formula to calculate k value.
```python
def calcRedundantBits(self, n):
    for k in range(n):
        if(n <= 2**k - k - 1):
            self.m_k = k
            return
```
Above function calculate minimum value of k that applies to above formula.

When we calculate k value, we must specify the position of parity bits. Parity bits are placed in positions that is are power of 2 ($2^0$).
