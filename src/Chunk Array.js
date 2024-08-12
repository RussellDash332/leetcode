/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const res = [];
    let subarr = []
    for (let i = 0; i < arr.length; i++) {
        subarr.push(arr[i]);
        if (subarr.length === size) {
            res.push(subarr);
            subarr = [];
        }
    }
    if (subarr.length) {
        res.push(subarr);
    }
    return res;
};
