DrawingRecognition
  A handwritten digit recognition app built with Tkinter and TensorFlow/Keras. 
  Draw a number (0–9) on the canvas, and the trained CNN model predicts what digit it is, along with a confidence percentage.

Features
- Interactive Tkinter Board — B for Brush, C for Clear, E for Eraser
- Real-time digit recognition using a trained CNN model
- Displays predicted digit with a confidence level
- Uses the MNIST dataset for training
- Modular code: separate scripts for training and UI

How It Works
- The CNN model is trained on the MNIST dataset, which contains 70,000 images of handwritten digits (0–9).
- The trained model is saved as digital_model.keras.
- The Tkinter interface allows the user to draw digits on a canvas.
- When the mouse button is released:
  - The canvas area is captured using ImageGrab
  - The image is converted to grayscale, inverted, and resized to 28×28
  - The processed image is passed to the pretrained model
  - The model outputs the predicted digit and confidence level

Installation
1. Clone the Repository
  git clone https://github.com/Parth-Joshi0/DrawingRecognition.git
  cd DrawingRecognition
2. Install Dependencies
  Make sure you have Python 3.9 or higher installed, then run:
  pip install -r requirements.txt

Dataset Setup (Manual Download Required)
- This project uses the MNIST Handwritten Digit Dataset, which must be downloaded manually before training.
- Download the Files
- Download the dataset from one of the following sources:
- Yann LeCun’s MNIST page
- Kaggle: MNIST Original Dataset
- You will receive four files:
  - train-images-idx3-ubyte
  - train-labels-idx1-ubyte
  - t10k-images-idx3-ubyte
  - t10k-labels-idx1-ubyte
- Create a folder named mnist/ in your project directory and move all four .ubyte files into it.

File Paths in Code
- In train_model.py, make sure the dataset paths match:
  - training_images = load_images("mnist/train-images-idx3-ubyte")
  - training_labels = load_labels("mnist/train-labels-idx1-ubyte")
  - testing_images = load_images("mnist/t10k-images-idx3-ubyte")
  - testing_labels = load_labels("mnist/t10k-labels-idx1-ubyte")
- Keep the folder name as mnist/ to avoid path changes.

Training the Model
- Once the dataset is in place, run:
    python3 train_model.py
- The script will:
  - Load the .ubyte data files
  - Train a CNN on the MNIST dataset
  - Print training accuracy and loss
  - Save the trained model as digital_model.keras
- You can manually change the epochs to a higher value for a more accurate model

Running the Application
- After training the model, launch the Tkinter interface:
    python3 drawing_recognition.py

Usage:
- Draw a digit (0–9) using your mouse
- Press C to clear or E to erase
- The predicted digit and confidence level will appear above the canvas

Model Overview
- Conv2D: 32 filters (3×3), ReLU activation
- MaxPooling2D: 2×2
- Conv2D: 64 filters (3×3), ReLU activation
- Flatten → Dense(128, ReLU)
- Dense(10, Softmax)
- Trained for 10–15 epochs on MNIST, typically achieving around 98–99% accuracy on the test set.

Example Output
- Example when drawing a “2”:
- Prediction: 2 (99.5% confidence)
<img width="508" height="538" alt="image" src="https://github.com/user-attachments/assets/17fa5e07-109f-4110-bbfa-1b80920c03bb" />

Author: Parth Joshi
Computer Science, Western University
GitHub: Parth-Joshi0
