# Phi2-GPTQ Streamlit App

A minimal Streamlit app that runs the quantized Phi-2 model (GPTQ) directly from Hugging Face and provides a simple web UI for generating responses to user prompts.

---

## 🚀 Live Demo

> **Deployed on Streamlit Cloud**: [https://phi2-gptq.streamlit.app](https://phi2-gptq.streamlit.app) *(replace with your actual URL)*

---

## 📦 Model Details

* **Model**: [Phi-2 GPTQ](https://huggingface.co/STiFLeR7/Phi2-GPTQ)
* **Quantization**: 4-bit GPTQ
* **Hosted On**: Hugging Face
* **Inference**: CPU (via Streamlit Cloud)

---

## 🧠 Features

* Load GPTQ-quantized model from Hugging Face
* CPU-only inference using `auto-gptq`
* Clean UI with Streamlit for prompt/response interaction

---

## 🏗️ Project Structure

```
phi2-gptq-streamlit/
├── app.py               # Streamlit UI logic
├── model_loader.py      # Model loading and inference logic
└── requirements.txt     # Python dependencies
```

---

## ▶️ Running Locally

```bash
# Clone the repo
git clone https://github.com/STiFLeR7/phi2-gptq-streamlit.git
cd phi2-gptq-streamlit

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click "New App"
4. Choose this repo and select `app.py`
5. Click **Deploy**

---

## ⚠️ Limitations

* Inference is slow due to CPU-only deployment
* Long prompts or token outputs may timeout
* For real-time performance, consider GPU-hosted APIs (we can help you set this up)

---

## 🙌 Acknowledgments

* [Phi-2 Model Authors](https://huggingface.co/microsoft/phi-2)
* [Auto-GPTQ](https://github.com/PanQiWei/AutoGPTQ)
* [Streamlit](https://streamlit.io)

---

## 👥 Contributors

* **Stifler** — Researcher & Developer | AI/ML/DL | Tech Lead at CudaBit

---

## 📜 License

MIT License
