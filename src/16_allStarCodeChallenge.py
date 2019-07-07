'''
Rewrite code challenges you've solved before or projects you've implemented
before in a different language in Python. Start getting in as much practice
with the language as possible!
'''

# JS VERSION =================
'''
/* All Star Code Challenge #18

Create a function called that accepts 2 string arguments and returns an integer of the count of
occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

*/

function strCount(str, letter){  
  let strArr = Array.from(str);
  let count = 0;
  for(let i = 0; i < strArr.length; i++) {
  if(strArr[i] === letter) {
    count++;
    }
  }
  return count;  
}
// strCount('Hello', 'o') // => 1
// strCount('Hello', 'l') // => 2
// strCount('', 'z')      // => 0
'''


def strCount(string, letter):
    print(string.count(letter))


strCount('Hello', 'o')
strCount('Hello', 'l')
strCount('', 'z')
