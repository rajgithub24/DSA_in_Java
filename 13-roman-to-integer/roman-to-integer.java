class Solution {
    static Map<String, Integer> value = new HashMap<>();
    static {
        value.put("I", 1);
        value.put("V", 5);
        value.put("X", 10);
        value.put("L", 50);
        value.put("C", 100);
        value.put("D", 500);
        value.put("M", 1000);
        value.put("IV", 4);
        value.put("IX", 9);
        value.put("XL", 40);
        value.put("XC", 90);
        value.put("CD", 400);
        value.put("CM", 900);
    }
    public int romanToInt(String s) {
        int sum = 0, i = 0;
        while(i< s.length()){
            if(i < s.length()-1){
                String twocount = s.substring(i, i+2);
                if(value.containsKey(twocount)){
                    sum+= value.get(twocount);
                    i = i+2;
                    continue;
                }
            }
            String onecount = s.substring(i, i+1);
            sum += value.get(onecount);
            i = i+1;
        }
        return sum;
        
    }
}