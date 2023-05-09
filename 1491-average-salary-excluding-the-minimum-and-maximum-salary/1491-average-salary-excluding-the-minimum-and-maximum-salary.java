class Solution {
    public double average(int[] salary) {
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        int total = 0;
        for(int i = 0; i < salary.length; i++) {
            max = Math.max(max, salary[i]);
            min = Math.min(min, salary[i]);
        }
        // System.out.println("min =" +  min);
        // System.out.println("max =" + max);
        for(int i = 0; i < salary.length; i++) {
            if(salary[i] != min && salary[i] != max) {
                total += salary[i];
            }             
        }
        // System.out.println("total =" + total);
        
        return total/(double)(salary.length-2);
        
    }
}