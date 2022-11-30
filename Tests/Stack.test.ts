import { isValid, isValidFast} from "../Stack/isValid";
import { Stack } from "../Stack/Stack";

describe('testing Stack Problems', () => {
    let s: string
    let expected: boolean;

    test('Stack', () => {
        let stack = new Stack();
        stack.push('(');
        stack.push(')')
        stack.pop();
        expect(stack.top.val === '(');
    });
    test('isValid - "()"', () => {
        s = "()";
        expected = true;
        expect(isValid(s)).toBe(expected);
    });
    test('isValid ', () => {
        s = "()[]{}";
        expected = true;
        expect(isValid(s)).toBe(expected);
    });
    test('isValid - "(]"', () => {
        s = "(]";
        expected = false;
        expect(isValid(s)).toBe(expected);
    });
    test('isValid - ', () => {
        s = "([)]";    
        expected = false;
        expect(isValid(s)).toBe(expected);
    });
    test('isValidFast - ', () => {
        s = "()";
        expected = true;
        expect(isValidFast(s)).toBe(expected);
    });
    test('isValidFast ', () => {
        s = "()[]{}";
        expected = true;
        expect(isValidFast(s)).toBe(expected);
    });
    test('isValidFast - "(]"', () => {
        s = "(]";
        expected = false;
        expect(isValidFast(s)).toBe(expected);
    });
    test('isValidFast - ', () => {
        s = "([)]";    
        expected = false;
        expect(isValidFast(s)).toBe(expected);
    });
    test('isValidFast - ', () => {
        s = "{[]}";    
        expected = true;
        expect(isValidFast(s)).toBe(expected);
    });
});