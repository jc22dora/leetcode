import { arrayToCycle, arrayToLinkedList, ListNode } from "../LinkedList";

describe('test', () => {
    let arr: any[];
    let head: ListNode | null;
    let pos: number;
    test('arrayToCycle', () => {
        arr = [3,2,0,-4];
        pos = 1;
        head = arrayToCycle(arr.reverse(), arr.length-pos-1);
    });
})
// describe('test', () => {
//     test('test', () => {
//     });
// })