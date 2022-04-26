train:
	docker-compose run web jupyter nbconvert --execute --to notebook --inplace  notebooks/xgboost-with-scikit-learn-pipeline-gridsearchcv.ipynb

up:
	docker-compose up --build

down:
	docker-compose down

build:
	docker-compose build