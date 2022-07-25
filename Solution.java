class Solution {
    public int[] merge(int[] nums1, int m, int[] nums2, int n) {
        int[] tempnums1 = new int[m + n];
        int tempm = m;
        int tempn = n;
        int x = -1;
        while (tempm + tempn > 0) {
            if (tempm == 0) {
                tempnums1[tempm + tempn+x] = nums2[tempn+x];
                tempn--;
            } else if (tempn == 0) {
                tempnums1[tempm + tempn+x] = nums1[tempm+x];
                tempm--;
            } else {
                //
                if (nums1[tempm+x] > nums2[tempn+x]) {
                    tempnums1[tempm + tempn+x] = nums1[tempm+x];
                    tempm--;
                } else if (nums1[tempm+x] < nums2[tempn+x]) {
                    tempnums1[tempm + tempn+x] = nums2[tempn+x];
                    tempn--;
                } else if (nums1[tempm+x] == nums2[tempn+x]) {
                    tempnums1[tempm + tempn+x] = nums1[tempm+x];
                    tempm--;
                    tempnums1[tempm + tempn+x] = nums2[tempn+x];
                    tempn--;
                }
                //
            }

        }
        for (int i = 0; i < tempnums1.length; i++) {
            nums1[i] = tempnums1[i];
        }
        return nums1;
    }
    public static void main(String[] args) {
        SolutionTest test = new SolutionTest();
    }
}