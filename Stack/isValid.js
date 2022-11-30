"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.isValid = void 0;
const Stack_1 = require("./Stack");
function isValid(s) {
    let openStr = '';
    let stack = new Stack_1.Stack();
    let opposite = new Map([
        ['(', ')'],
        [')', '('],
        ['[', ']'],
        [']', '['],
        ['{', '}'],
        ['}', '{'],
    ]);
    for (let i = 0; i < s.length; i++) {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
            openStr = openStr.concat(s[i]);
        }
        else {
            stack.push(s[i]);
        }
    }
    let j = openStr.length - 1;
    while (j >= 0) {
        if (openStr[j] != opposite.get(stack.top.val)) {
            return false;
        }
        else {
            stack.pop();
            j--;
        }
    }
    if (stack.top.val)
        return false;
    return true;
}
exports.isValid = isValid;
;
