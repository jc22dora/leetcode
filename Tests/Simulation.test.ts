describe('MultiplyString', () => {
    test('single - single', () => {
        expect(multiply("2", "6") == "12");
    });
    test('double - single', () => {
        expect(multiply("10", "6") == "60");
    });

})