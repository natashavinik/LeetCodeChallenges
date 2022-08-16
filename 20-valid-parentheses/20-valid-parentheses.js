/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {

    let s_len = s.length;
    if (s.length % 2 != 0){
        return false;
    }
    let str = s
    let open_p = ["(", "[", "{"]
    let open_array = [];
    for (p of s) {
        if (open_p.includes(p)){
            open_array.push(p);
        }else if (p == ")" && open_array[open_array.length -1] == "("){
            open_array.pop();
        }else if (p == "]" && open_array[open_array.length -1] == "["){
            open_array.pop();
        }else if (p == "}" && open_array[open_array.length -1] == "{"){
            open_array.pop(); 
    }else {
        return false
    }
    };
    if (open_array.length > 0) {
        return false
    }else {
        return true
    }
};