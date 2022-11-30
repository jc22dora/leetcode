import { Stack } from "./Stack";

export function isValid(s: string): boolean {
    let stack: Stack = new Stack();
    let opposite: Map<string, string> = new Map([
        ['(', ')'],
        [')', '('],
        ['[', ']'],
        [']', '['],
        ['{', '}'],
        ['}', '{'],
      ]);
    for(let i=0; i<s.length;i++) {
        if(s[i] == '(' || s[i] == '[' || s[i] == '{') {
            stack.push(s[i]);
        } else if(!stack.top.val || opposite.get(s[i]) != stack.pop()) {
            return false;
        }
    }
    if(stack.top.val) return false;
    return true;
};
export function isValidFast(s: string): boolean {
    let stack: string[] = [];
    let opposite: Map<string, string> = new Map([
        ['(', ')'],
        [')', '('],
        ['[', ']'],
        [']', '['],
        ['{', '}'],
        ['}', '{'],
      ]);
    for(let i=0; i<s.length;i++) {
        if(s[i] == '(' || s[i] == '[' || s[i] == '{') {
            stack.push(s[i]);
        } else if(!stack || opposite.get(s[i]) != stack[stack.length-i+1]) {
            return false;
        }
    }
    return true;
};
