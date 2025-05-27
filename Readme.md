# Repo structure
## notebooks folder
1_dataset_generation.ipynb - to generate questions of various complexity  
2_research.ipynb - blooms taxonomy with prompt engineering and training dataset generation  
3_classifier.ipynb - custom BERT based multi label classifier tuning
  
## api
Basic FastAPI Web API with prompt based classifier.
To run:
```
cd api
uvicorn main:app --reload
```

# Artifacts
## LLM Generated dataset
notebooks\high_complexity.csv
notebooks\low_complexity.csv
notebooks\moderate_complexity.csv

## Custom model:
fine-tuned model trainig dataset - notebooks\train.csv
fine-tuned model files - https://huggingface.co/jzilcov/prompt_complexity_classifier/tree/main

# Report
report.md