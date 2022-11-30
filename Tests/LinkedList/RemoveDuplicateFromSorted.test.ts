import { ListNode } from '../../LinkedList';
import {deleteDuplicates, isEqual} from '../../LinkedList/RemoveDuplicateFromSorted'
describe('RemoveDuplicateFromSorted', () => {
    let head: ListNode | null;
    let expected: ListNode;
    let output: ListNode | null;
    test('test1', () => {
        head = new ListNode(1, new ListNode(1));
        expected = new ListNode(1);
        output = deleteDuplicates(head);
        expect(isEqual(head, output)).toBe(true)
    });
})