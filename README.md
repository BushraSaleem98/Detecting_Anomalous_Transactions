# Detecting Anomalous Transactions  

**A Python project using Isolation Forest to detect and visualize anomalous financial transactions for fraud detection.**  

## 📌 Project Overview  
- Analyze banking transaction data (amount, duration, balance).  
- Use **Isolation Forest (IForest)** from the `pyod` library for anomaly detection.  
- Flag suspicious transactions and summarize them.  
- Visualize differences in transaction patterns between normal and anomalous data.  

## 🛠️ Tech Stack  
- **Python**  
- **Libraries**: Pandas, NumPy, Matplotlib, PyOD  

## 📂 Files in this Repository  
- `detecting_anomalous.py` → Main solution file with anomaly detection workflow.  
- `README.md` → Project documentation.  
- `anomalies_histogram.png` → Visualization comparing normal vs anomalous transactions.  

## 📑 Dataset  
The dataset used in this project can be downloaded here:  
👉 [Download transactions.csv](https://your-dataset-link.com)  

> Replace this link with your Google Drive, Kaggle, or GitHub-hosted dataset link.  

## 🚀 How to Run  
1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/anomalous-transactions.git
   cd anomalous-transactions
   ```
2. Download the dataset (`transactions.csv`) and place it in the project folder.  
3. Install dependencies:  
   ```bash
   pip install pandas numpy matplotlib pyod
   ```
4. Run the solution file:  
   ```bash
   python detecting_anomalous.py
   ```  

## 📊 Example Output  
- A summary of anomalous transactions including:  
  - Transaction ID  
  - Transaction Amount  
  - Transaction Duration  
  - Account Balance  
- A histogram (`anomalies_histogram.png`) showing the distribution of normal vs anomalous transaction amounts.  

## 🔗 Source Code  
👉 [detecting_anomalous.py](./detecting_anomalous.py)  

---

✨ This project demonstrates anomaly detection in real-world financial datasets and can serve as a foundation for **fraud detection systems** in banking and e-commerce.  
