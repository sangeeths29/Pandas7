# Problem 1 - Immediate Food Delivery I ( https://leetcode.com/problems/immediate-food-delivery-i/ )
import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # Approach 1 - Using mean() method
    immediate_delivery = delivery['order_date'] == delivery['customer_pref_delivery_date']
    immediate_percentage = round(immediate_delivery.mean() * 100, 2)
    return pd.DataFrame({'immediate_percentage':[immediate_percentage]})

    # Approach 2 - Dividing count by total
    df = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]
    return pd.DataFrame([round(len(df) / len(delivery) * 100, 2)], columns = ['immediate_percentage'])