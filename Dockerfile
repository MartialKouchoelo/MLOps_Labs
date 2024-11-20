FROM continuumio/miniconda3

LABEL maintainer="Spero Tossogbe <spero.tossogbe@edu.dsti.institute>" \
      description="Docker Data Science Workflow #2: Data Science Project\
      Libraries inside image. Data/code mounted via shared folder.\
      Easy to set up a new developmenet environment."


# Set the working directory to /app and copy current dir
WORKDIR /app
COPY . /app

# Run hello_world.py when the container launches
RUN conda install pytest && \
    conda install pytest-cov

CMD ["sh", "-c", "cd ./unit_testing_best_practice/test && coverage run -m pytest && coverage report -m"]
