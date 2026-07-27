from src.llm.analyzer import analyze_review

review = """
Delivery was very late.
The stitching quality is poor.
Not worth the price.
"""

result = analyze_review(review)

print(result)