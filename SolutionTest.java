import java.util.Arrays;

public class SolutionTest {
  Solution test;
    public SolutionTest() {
      
      testOne();
      testTwo();
    }
      public void testOne() {
        int[] nums1 = {1, 2, 3, 0, 0 ,0};
        int m = 3;
        int[] nums2 = {2,5,6};
        int n = 3;
        test = new Solution();
        int[] given = test.merge(nums1, m, nums2, n);
        int[] answer = {1,2,2,3,5,6};
        if(checkTest(nums1, answer)) {
          System.out.println("Test One: Passed");
        }else{
          System.out.println("Test One: Failed");
        }
    }
    public void testTwo() {
      int[] nums1 = {1,2,6,3,6,8,0,4,3,5,7,0,0,0,0};
      int m = nums1.length;
      int[] nums2 = {2,5,6,22};
      int n = nums2.length;
      nums1 = concat(nums1,m, nums2);
      int[] answer = nums1;
      Arrays.sort(answer);
      test.merge(nums1, m, nums2, n);
      if(checkTest(nums1, answer)) {
        System.out.println("Test Two: Passed");
      }else{
        System.out.println("Test Two: Failed");
      }
  }


    public boolean checkTest( int[] given, int[] correct){
      for(int i=0; i<given.length;i++){
        if(given[i]!=correct[i]){
          return false;
        }
      }
      return true;
    }

    public int[] concat(int[] arr1,int m, int[] arr2){
      for(int i=m;i<arr1.length;i++){
        arr1[i]=arr2[i-m];
      }
      return arr1;
    }
}