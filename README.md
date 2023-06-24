This repo contains projects for training and prediction via ludwig for studying purpose 

this project aims for only Ludwig CLI ( yaml file )

> Commands : ludwig train --dataset ratings_sample.csv --config config.yml

>  ludwig predict --dataset test_data.csv  --model_path "results\experiment_run_12\model" --output_directory 'Predict'


> ludwig visualize --visualization learning_curves --training_statistics ratings_sample.meta.json


>git push --force origin main