# -recreating-the-poetic-style-of-Irish-lyrics
explore cultural preservation through technology by recreating the poetic style of Irish lyrics


the Microsoft DEPI Internship in Machine Learning!
Generating Poetry from Irish Lyrics! This project combined the power of machine learning with the beauty of traditional Irish music, allowing us to generate authentic, Irish-inspired poetry with AI.
 Project Highlights:
1. Purpose and Motivation
Our aim was to explore cultural preservation through technology by recreating the poetic style of Irish lyrics. This project brought together art and AI, bridging creativity and cultural appreciation with cutting-edge technology.
2. Data Collection through Web Scraping
We used web scraping techniques to collect authentic Irish folk lyrics. This approach allowed us to gather a broader range of lyrical.
3. Data Preprocessing
Once we gathered the data, we processed it to enhance model performance:
Text Cleaning: Converted all text to lowercase, removed special characters, and standardized formats for consistency.
Tokenization and Sequencing: Split the text into tokens and created fixed-length sequences to provide context to the model.
4. Model Architecture
Our model was based on an LSTM Recurrent Neural Network due to its ability to handle sequential data effectively:
Embedding Layer: Encoded words as dense vectors, capturing underlying semantic meanings.
LSTM Layers: Captured the temporal dependencies essential for poetry generation.
Dense Layer with Softmax: Predicted the probability of each word in the sequence, allowing the model to generate coherent and contextually relevant lyrics.
5. Model Configuration and Training
To optimize performance, we carefully tuned our configurations:
Optimizer: Adam, known for its efficiency in handling adaptive learning rates.
Batch Size: 64, balancing computational efficiency and model robustness.
Dropout: 0.2, which helped prevent overfitting by randomly deactivating neurons during training.
6. Deployment on Flask
We brought our project to life by deploying the model on a Flask webpage, enabling users to generate their own Irish-inspired lyrics in real time. Sample outputs like “the green fields of Ireland are calling me home” showcased the model’s ability to capture Irish themes and lyricism.
