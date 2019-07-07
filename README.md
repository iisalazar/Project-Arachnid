# Project Arachnid

This serves as the official repository for QSHS's official website

# Usage
## Using docker
0. Install docker (if you haven't yet)
1. Build the image
   ```shell 
	docker build -t arachnid:0.1 .
   ```
2. After building, run the image
   ```shell
	docker run -d -p 8000:8000 arachnid:0.1
   ```
3. Open your browser at 127.0.0.1:8000

## Without docker

1. clone repo
2. install pip or pipenv
3. ```cd``` to directory
4. if you use pip, run 
   ```shell 
	pip install -r requirements.txt
   ```
4.5 if you use pipenv, run
   ```shell 
	pipenv shell
	pipenv install
   ```

5. ```cd``` to "Project-Arachnid"
6. Run python manage.py runserver