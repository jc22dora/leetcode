"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Stack = void 0;
class Stack {
    constructor() {
        this.top = new Node();
    }
    push(val) {
        this.top = new Node(val, this.top);
    }
    pop() {
        this.top = this.top.next ?? new Node();
    }
}
exports.Stack = Stack;
class Node {
    constructor(val, next) {
        this.val = (val === undefined ? null : val);
        this.next = (next === undefined ? null : next);
    }
}
