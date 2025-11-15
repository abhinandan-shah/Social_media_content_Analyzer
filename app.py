import os
import uuid
import traceback
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import pandas as pd
import pdfplumber
from PIL import Image
import pytesseract

def analyze(df, outdir, n_topics=5):
    import os, pandas as _pd, matplotlib.pyplot as plt
    os.makedirs(outdir, exist_ok=True)
    cleaned_path = os.path.join(outdir, "cleaned_data.csv")
    df.to_csv(cleaned_path, index=False, encoding='utf-8')

    sent = df['content'].apply(lambda t: ('POSITIVE' if any(w in t.lower() for w in ['love','good','great','awesome','proud']) 
                                          else ('NEGATIVE' if any(w in t.lower() for w in ['ugh','bad','hate','exhaust','slow','problem']) 
                                                else 'NEUTRAL')) )
    ss = sent.value_counts().reset_index()
    ss.columns = ['sentiment','count']
    ss.to_csv(os.path.join(outdir,'sentiment_summary.csv'), index=False)

    try:
        ax = ss.plot.bar(x='sentiment', y='count', legend=False, figsize=(6,4))
        ax.set_title('Sentiment distribution')
        ax.set_xlabel('')
        ax.set_ylabel('Count')
        plt.tight_layout()
        plt.savefig(os.path.join(outdir,'sentiment_bar.png'), dpi=150)
        plt.close()
    except Exception:
        pass

    topics = []
    for i, row in df.iterrows():
        words = [w for w in str(row['content']).split() if len(w) > 3][:6]
        topics.append({'topic_id': i, 'top_words': ', '.join(words)})
    _pd.DataFrame(topics).to_csv(os.path.join(outdir,'topics.csv'), index=False)

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
RESULTS_FOLDER = os.path.join(os.getcwd(), "results")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

import os
from flask import Flask
HERE = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(HERE, "templates"), static_folder=os.path.join(HERE, "static"))

app.secret_key = os.urandom(24).hex()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULTS_FOLDER'] = RESULTS_FOLDER

ALLOWED = {'.pdf', '.png', '.jpg', '.jpeg'}

def extract_text_from_pdf(path):
    texts = []
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                txt = page.extract_text(x_tolerance=1, y_tolerance=1)
                if txt:
                    texts.append(txt)
    except Exception:
        traceback.print_exc()
    return "\n\n".join(texts)

def extract_text_from_image(path):
    try:
        img = Image.open(path)
        return pytesseract.image_to_string(img)
    except Exception:
        traceback.print_exc()
        return ""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    uploaded_files = request.files.getlist("files")
    if not uploaded_files or uploaded_files == [None]:
        flash("No files selected", "error")
        return redirect(url_for("index"))

    rows = []
    try:
        for up in uploaded_files:
            filename = up.filename or "unnamed"
            ext = os.path.splitext(filename)[1].lower()
            if ext not in ALLOWED:
                flash(f"Skipping unsupported file type: {filename}", "warning")
                continue
            save_name = str(uuid.uuid4()) + ext
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], save_name)
            up.save(save_path)

            if ext == '.pdf':
                extracted = extract_text_from_pdf(save_path)
            else:
                extracted = extract_text_from_image(save_path)

            if not extracted or not extracted.strip():
                extracted = "[NO TEXT EXTRACTED]"
            rows.append({'content': extracted, 'source_file': filename})
    except Exception as e:
        traceback.print_exc()
        flash("Error during extraction: " + str(e), "error")
        return redirect(url_for("index"))

    if not rows:
        flash("No valid text extracted from uploads.", "error")
        return redirect(url_for("index"))

    df = pd.DataFrame(rows)
    run_id = "run_" + uuid.uuid4().hex[:8]
    run_outdir = os.path.join(app.config['RESULTS_FOLDER'], run_id)
    os.makedirs(run_outdir, exist_ok=True)

    try:
        analyze(df, run_outdir, n_topics=5)
    except Exception as e:
        traceback.print_exc()
        flash("Analysis failed: " + str(e), "error")
        return redirect(url_for("index"))

    
    result_files = os.listdir(run_outdir)  
    cleaned_html = ""
    sentiment_html = ""
    topics_html = ""
    images = []

    try:
        cleaned_path = os.path.join(run_outdir, 'cleaned_data.csv')
        if os.path.exists(cleaned_path):
            cleaned_df = pd.read_csv(cleaned_path)
            cleaned_df['content'] = cleaned_df['content'].astype(str).str.replace('\n', '<br>')
            cleaned_html = cleaned_df.head(50).to_html(classes="table table-striped", index=False, escape=False)
    except Exception:
        traceback.print_exc()
        cleaned_html = "<p>Could not load cleaned_data.csv</p>"

    try:
        sent_path = os.path.join(run_outdir, 'sentiment_summary.csv')
        if os.path.exists(sent_path):
            sent_df = pd.read_csv(sent_path)
            sentiment_html = sent_df.to_html(classes="table table-sm", index=False, escape=False)
    except Exception:
        traceback.print_exc()
        sentiment_html = "<p>Could not load sentiment_summary.csv</p>"

    try:
        topics_path = os.path.join(run_outdir, 'topics.csv')
        if os.path.exists(topics_path):
            topics_df = pd.read_csv(topics_path)
            topics_html = topics_df.to_html(classes="table table-sm", index=False, escape=False)
    except Exception:
        traceback.print_exc()
        topics_html = "<p>Could not load topics.csv</p>"

    # Collect PNGs (only strings) and build image dicts
    for fn in result_files:
        if isinstance(fn, str) and fn.lower().endswith('.png'):
            images.append({'name': fn, 'url': f"/results/{run_id}/{fn}"})

    return render_template(
        "result.html",        
        run_outdir=run_outdir,
        files=result_files,
        cleaned_html=cleaned_html,
        sentiment_html=sentiment_html,
        topics_html=topics_html,
        images=images,
        run_id=run_id
    )


@app.route("/results/<run>/<filename>")
def serve_result(run, filename):
    base = os.path.join(app.config['RESULTS_FOLDER'], run)
    return send_from_directory(base, filename, as_attachment=False)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
