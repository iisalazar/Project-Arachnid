# Project Arachnid

This serves as the official repository for QSHS's official website

# Usage
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
