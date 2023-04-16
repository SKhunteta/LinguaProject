# Base image
FROM python:3.11-slim-bullseye

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip3.11 install -r requirements.txt

# Copy Lingua.py and LinguaDiscordBot.py
COPY LinguaConsoleBot/Lingua.py LinguaDiscordBot/LinguaDiscordBot.py ./

# Expose port 8000 for Lingua.py and 8080 for LinguaDiscordBot.py
EXPOSE 8080

# Start the LinguaDiscordBot.py script
CMD ["python3.11", "LinguaDiscordBot.py"]
