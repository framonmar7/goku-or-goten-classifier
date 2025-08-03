# 🧠 Goten vs Goku Classifier

This is a technical challenge in binary image classification, designed to evaluate whether a given face image corresponds to **Son Goten** or **Son Goku (child)**. The project explores how deep learning models handle visual ambiguity between nearly identical characters from the *Dragon Ball* universe.

Live demo available at goku-or-goten.framonmar7.dev

## 🔬 Models

This project uses **three CNN-based models** trained via transfer learning:

- A model specialized in detecting **Goten**, which may confuse him with Goku.
- A model specialized in detecting **Goku**, which may confuse him with Goten.
- An **arbiter model** that intervenes when the other two disagree, acting as a tie-breaker to decide whether the face belongs to Goten or Goku.

The dataset includes cropped facial images of both characters in their childhood form. This resemblance introduces a real challenge, pushing image classification techniques to their limits in terms of feature extraction and decision boundaries.

You can explore and download the models on Hugging Face:
👉 https://huggingface.co/framonmar7/goku-or-goten-classifier

## ⚙️ Setup Instructions

1. **Install the dependencies in a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate    # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. **Create your environment file**:

Copy the `.env.example` to `.env` and provide the values:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

3. **Prepare the backend**:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

4. **Run the development server**:

```bash
python manage.py runserver
```

Once the development server is running, you can access the application in your browser at the URL shown in the terminal.

---

## 📜 License

This project is released under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it — with attribution.

---

## 👤 Author

Developed by [Francisco Jesús Montero Martínez](https://github.com/framonmar7)  
For suggestions, improvements, or collaboration, feel free to reach out.
