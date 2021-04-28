From python:3.8
COPY . .
# install needed libs
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
# intall python packages
RUN pip install -r requirements.txt
# Run python script
CMD ["python", "./ping_my_image.py"]
