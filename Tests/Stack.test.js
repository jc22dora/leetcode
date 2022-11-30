"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const isValid_1 = require("../Stack/isValid");
const Stack_1 = require("../Stack/Stack");
describe('testing Stack Problems', () => {
    let s;
    let expected;
    test('Stack', () => {
        let stack = new Stack_1.Stack();
        stack.push('(');
        stack.push(')');
        stack.pop();
        expect(stack.top.val === '(');
    });
    test('isValid - "()"', () => {
        s = "()";
        expected = true;
        expect((0, isValid_1.isValid)(s)).toBe(expected);
    });
    test('isValid - "()[]{}"', () => {
        s = "()[]{}";
        expected = true;
        expect((0, isValid_1.isValid)(s)).toBe(expected);
    });
    test('isValid - "(]"', () => {
        s = "(]";
        expected = false;
        expect((0, isValid_1.isValid)(s)).toBe(expected);
    });
    test('isValid - ', () => {
        s = "([)]";
        expected = false;
        expect((0, isValid_1.isValid)(s)).toBe(expected);
    });
});
