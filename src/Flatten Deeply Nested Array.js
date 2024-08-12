/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    const res = [];
    function helper(arr, depth) {
        for (const val of arr) {
            if (typeof val === 'object' && depth > 0) {
                helper(val, depth-1);
            } else {
                res.push(val);
            }
        }
        return res;
    }
    return helper(arr, n);
};