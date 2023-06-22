ludwig train --dataset "Simpsons character classifier at home\simpsons_dataset\dataset.csv" --config "Simpsons character classifier at home\config.yaml" --output_directory "Simpsons character classifier at home\results"



ludwig predict --model_path "Simpsons character classifier at home\results\experiment_run_8\model" --dataset "Simpsons character classifier at home\simpsons_dataset\dataset.csv" --output_directory "Simpsons character classifier at home\predict"

> ludwig visualize --visualization learning_curves --training_statistics "Twitter US Airline Sentiment\results\experiment_run_2\training_statistics.json"


> ludwig predict --model_path "Simpsons character classifier at home\results\experiment_run_2\model" --dataset "Simpsons character classifier at home\simpsons_dataset\dataset.csv" --output_directory "Simpsons character classifier at home\predict" 



ludwig train --dataset "Simpsons character classifier at home\simpsons_dataset\simpsons_dataset.csv" --config "Simpsons character classifier at home\config.yaml"
