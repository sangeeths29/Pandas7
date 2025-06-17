# Problem 2 - Count Salary Categories ( https://leetcode.com/problems/count-salary-categories/ )
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_df = accounts[accounts['income'] < 20000]
    avg_df = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)]
    high_df = accounts[accounts['income'] > 50000]
    return pd.DataFrame([['Low Salary', len(low_df)],
                        ['Average Salary', len(avg_df)],
                        ['High Salary', len(high_df)]], columns = ['category', 'accounts_count'])