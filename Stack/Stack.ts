import { NODE_FIELDS } from "@babel/types";

export class Stack {
    top: Node;
    constructor() {
        this.top = new Node()
    }
    push(val: any) {
        this.top = new Node(val, this.top)
    }
    pop() {
        let tempNode = this.top;
        this.top = this.top.next?? new Node();
        return tempNode.val;
    }
}
export class Node {
    val: any;
    next: Node | null;
    constructor(val?: any, next?: Node | null) {
        this.val = (val===undefined ? null: val)
        this.next = (next===undefined ? null : next)
    }
}
export class DoubleNode {
    val: any;
    next: DoubleNode | null;
    prev: DoubleNode | null;
    constructor(val?: any, next?: DoubleNode | null, prev?: DoubleNode | null) {
        this.val = (val===undefined ? null: val)
        this.next = (next===undefined ? null : next)
        this.prev = (prev===undefined ? null : prev)
    }
}