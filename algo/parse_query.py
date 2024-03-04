from typing import List

"""
(Michael K - f2f) Given an array of strings and a query. Each string in the array has several parts separated by delimiters.
 You need to filter the strings by query  and return parts of these strings that are missing from the query.

array = “hello | world | tag:value1, server:val2, param:val3”

query = [“tag:value1”, ”param:val3”]

expected answer = [“server:val2”]

To sum up, find a subset of strings according to the query and return elements that are present in them and are missing in the query.
"""

class Solution:

    def find_missing_tags(self, query: List, data: str)->List:
        query_set = set(query)
        data_elements = data.split("|")
        data_sets = [set([tag.strip() for tag in element.split(",")]) for element in data_elements]
        # print(query_set, data_sets)

        sets_diff = []
        for data_set in data_sets:
            if query_set & data_set:
                # print(f"{data_set} match {query_set}")
                sets_diff = data_set - query_set
                # print(f"sets diff: {sets_diff}")
            
        return list(sets_diff)

if __name__ == "__main__":
    solution = Solution()
    print(solution.find_missing_tags(["tag:value1", "param:val3"], "hello | world | tag:value1, server:val2, param:val3"))
    print(solution.find_missing_tags(["hello"], "hello, datadog | world | tag:value1, server:val2, param:val3"))