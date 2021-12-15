class Solution {
    public int maxProfit(int[] prices) {
        int l = prices.length;
        int max_profit = 0;
        int min_price = prices[0];
        for (int i=0;i<prices.length;i++){
            if((prices[i]-min_price) > max_profit){
                max_profit = prices[i]-min_price;
            }
            if(prices[i] < min_price){
                min_price = prices[i];
            }
        }        
        return max_profit;
    }
}