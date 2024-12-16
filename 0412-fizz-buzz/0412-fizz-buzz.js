/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let ans = [];
    let fizz = ""
    for (let i = 1; i <= n; i++) {
        fizz = "";
        if (i%3 === 0) {
            fizz = "Fizz";
        }
        if (i%5 === 0) {
            fizz += "Buzz";
        }
        if (i%3 != 0 && i%5 != 0) {
            fizz = i.toString();
        }
        ans.push(fizz);
    }
    return ans;
};