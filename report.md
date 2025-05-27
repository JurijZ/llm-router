# Hypothesis

Use Bloom's Taxonomy criterias to evaluate texts' cognitive complexity

# Results

There is a correlation between the text cognitive complexity and Bloom's Taxonomy criterias.  
This correlation can be used to make a routing decision.  
  
LLM can be used as a cognitive complexity evaluator.  
Pros: high quality, easy usage, easy access.  
Cons: low speed.  
  
Multi label classifier can be used as a cognitive complexity evaluator.  
Pros: high speed.  
Cons: low quality, expensive fine-tuning, hosting challenges.  
  
# Recommendations

If response speed is not a issue, use LLM.  
If response time is critical, consider fine-tuning.  
