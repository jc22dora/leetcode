import {DoubleNode } from "../Stack/Stack";

export class MyCircularQueue {
    front: DoubleNode;
    rear: DoubleNode;
    size: number;
    length: number;
    constructor(k: number) {
        this.size = k;
        this.length = 0;
        this.front = new DoubleNode();
        this.rear = this.front;
    }

    enQueue(value: number): boolean {
        if(this.length < this.size){
            let tempNode = this.front;
            let newNode = new DoubleNode(value, this.rear, tempNode);
            this.front = newNode;
            this.length++;
            if(!this.front.prev?.val){
                this.front.prev = this.front;
            } else {
                this.front.prev = tempNode;
            }
            if(!this.rear.val){
                this.rear = this.front;
            } else {
                this.rear.prev = newNode;
                this.rear.next = this.front;
            }
            return true;
        } return false;
    }

    deQueue(): boolean {
        if(this.length == 0){
            return false;
        }
        this.rear = this.rear.next?? new DoubleNode();
        this.length--;
        return true;
    }

    Front(): number {
        if(this.length == 0) return -1;
        return this.front.val;
    }

    Rear(): number {
        if(this.length == 0) return -1;
        return this.rear.val;
    }

    isEmpty(): boolean {
        if(this.length == 0) {
            return true;
        } return false;
    }

    isFull(): boolean {
        if(this.length < this.size){
            return false;
        } return true;
    }
    Link(): number[]{
        return [this.front.next?.val, this.rear.next?.val];
    }
}