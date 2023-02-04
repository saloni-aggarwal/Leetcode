class Pair implements Comparable<Pair>{
    int idx;
    int value;
    
    public Pair(int idx, int value) {
        this.idx = idx;
        this.value = value;
    }
    
    public int getIdx() {
        return this.idx;
    }
    
    public int compareTo(Pair other) {
        return Integer.valueOf(this.value).compareTo(other.value);
    }
    
    public String toString() {
        return "idx = " + this.idx + " value = " + this.value;
    }
}

class Solution {
    public int[][] sortTheStudents(int[][] score, int k) {
        
        Pair[] arr = new Pair[score.length];
        Pair pair;
        for(int i = 0; i < score.length; i++) {
            pair = new Pair(i, score[i][k]);
            arr[i] = pair;
        }
        
        Arrays.sort(arr);
        int[][] ans = new int[score.length][score[0].length];
        int j = 0;
        
        for(int i = arr.length-1; i >= 0; i--) {
            ans[j++] = score[arr[i].getIdx()];            
        }
        
        return ans;
    }
}