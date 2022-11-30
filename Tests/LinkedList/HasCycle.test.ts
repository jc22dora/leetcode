import { arrayToCycle, arrayToLinkedList, ListNode } from "../../LinkedList";
import { hasCycle } from "../../LinkedList/HasCycle";

describe('hasCycle', () => {
    let arr: any[];
    let head: ListNode | null;
    let output: boolean;
    let expected: boolean;
    let pos: number;
    test('3, 2, 0, -4', () => {
        arr = [3,2,0,-4];
        pos = 1;
        head = arrayToCycle(arr.reverse(), arr.length-pos-1);
        output = hasCycle(head)
        expected = true;
        expect(output).toBe(expected);
    });
    test(' 1 ', () => {
        arr = [1];
        head = arrayToLinkedList(arr);
        output = hasCycle(head)
        expected = false;
        expect(output).toBe(expected);
    });
})