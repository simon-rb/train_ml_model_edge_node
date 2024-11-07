# AI Model Training on Alibaba Cloud's Zurich Edge Node

## Project Overview

This repository demonstrates a simple example of training an AI model using TensorFlow on Alibaba Cloud's Zurich edge node. The goal is to showcase the basic process of leveraging edge computing resources for AI workloads. While this is a straightforward example, it sets the stage for exploring more advanced use cases in the future.

## Project Contents

- `train_model.py`: Script for training a basic neural network model and saving the weights.
- `inference.py`: Script for loading the trained weights and performing a simple inference operation.
- This README file: Documentation and instructions for using the repository.

---

## Motivation

Edge computing is a powerful paradigm that enables faster data processing by bringing computation closer to data sources. While this example is simple, it highlights how even basic AI workflows can benefit from reduced latency and efficient resource utilization at the edge. Alibaba Cloud's Zurich edge node offers a robust platform to demonstrate these capabilities.

## Prerequisites

- Python 3.x installed on both your local machine and the edge node.
- SSH access to the Alibaba Cloud edge node.
- Installed packages: `numpy`, `matplotlib`, and `tensorflow`.

---

## Setup Instructions

### 1. Connecting to the Edge Node

Connect to your Alibaba Cloud edge node using SSH:

```bash
ssh root@your_instance_ip
```

Replace `your_instance_ip` with the actual IP address of your edge node (e.g., `163.121.137.9`).

### 2. Preparing the Environment on the Edge Node

#### a. Install Necessary Packages for Virtual Environment

```bash
sudo apt-get update
sudo apt-get install python3-venv
```

#### b. Create and Activate a Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

#### c. Install TensorFlow and Other Dependencies

Use the official PyPI index to avoid potential connectivity issues:

```bash
pip install tensorflow --index-url https://pypi.org/simple
pip install numpy matplotlib --index-url https://pypi.org/simple
```

---

### 3. Uploading the Training Script

Transfer `train_model.py` from your local machine to the edge node:

```bash
scp Documents/code/playground/train_model.py root@163.121.137.9:~/training_files/
```

---

### 4. Running the Training Script

#### a. Connect to the Edge Node (if not already connected)

```bash
ssh root@163.121.137.9
```

#### b. Navigate to the Directory and Activate the Virtual Environment

```bash
cd ~/training_files/
source ~/myenv/bin/activate
```

#### c. Run the Training Script

```bash
python3 train_model.py
```

This will train a basic model and save the weights to `model.weights.h5`.

---

### 5. Downloading the Trained Weights

Transfer the trained weights back to your local machine:

```bash
scp root@163.121.137.9:~/training_files/model.weights.h5 Documents/code/playground/
```

---

## Using the Inference Script Locally

1. Place `inference.py` and `model.weights.h5` in the same directory on your local machine.
2. Run the inference script:

```bash
python3 inference.py
```

This script will load the trained weights and perform a simple inference, generating a plot of model predictions versus the true function.

---

## Note on Simplicity and Future Improvements

This example is intentionally kept simple to provide a clear, focused demonstration of model training on an edge node. There are many other, more efficient, approaches to edge-based AI workflows that will be explored in future examples. Stay tuned!

---

## Benefits of Edge Computing for AI Training

- **Reduced Latency**: Training and processing are performed closer to the data source.
- **Efficiency**: Even simple workflows benefit from the robust compute capabilities of edge nodes.
- **Data Privacy**: Localized processing minimizes data movement and improves privacy.

---
