'''
Rewrite code challenges you've solved before or projects you've implemented
before in a different language in Python. Start getting in as much practice
with the language as possible!
'''

# JAVASCRIPT VERSION =======================
'''
// Given an array, find the int that appears an odd number of times.

// There will always be only one integer that appears an odd number of times.

const findOdd = arr => {
  let answer;
  arrObj = arr.reduce((acc, curr) => {
    typeof acc[curr] === 'undefined' ? (acc[curr] = 1) : (acc[curr] += 1);
    return acc;
  }, {});
  Object.keys(arrObj).forEach(key => {
    if (!(arrObj[key] % 2 === 0)) {
      answer = key;
    }
  });
  return answer;
}

// const findOdd = (xs) => xs.reduce((a, b) => a ^ b); // crazy bitwise solution using xor

console.log(findOdd([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5);
console.log(findOdd([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
console.log(findOdd([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
console.log(findOdd([10]), 10);
console.log(findOdd([1,1,1,1,1,1,10,1,1,1,1]), 10);
console.log(findOdd([5,4,3,2,1,5,4,3,2,10,10]), 1);
'''

# PYTHON VERSION =================

'''
Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
'''


def findOdd(arr):
    hashTable = {}
    for num in arr:
        if (num in hashTable):
            hashTable[num] += 1
        else:
            hashTable[num] = 1

    for key, num in hashTable.items():
        if (int(num) % 2 == 1):
            print(key)
            return key


findOdd([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
findOdd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
findOdd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
findOdd([10])
findOdd([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1])
findOdd([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10])
