📊 Social Media Content Analyzer



A web-based AI tool for extracting, cleaning, and analyzing text from PDF files and image documents (JPG/PNG) using OCR, followed by sentiment analysis, topic extraction, and data visualization.



This project is built as part of a technical assessment, demonstrating your ability to handle real-world data processing tasks including NLP, OCR, backend APIs, and frontend UI development.



🚀 Features

✔ 1. File Upload (PDF \& Images)



Upload multiple PDF or image files.



Drag-and-drop interface with modern UI.



Server automatically stores uploaded files.



✔ 2. Text Extraction



PDF Parsing using pdfplumber



OCR for images using pytesseract



Supports scanned documents and photos



Extracted text is normalized for analysis



✔ 3. Sentiment Analysis



Classifies text into:



POSITIVE



NEGATIVE



NEUTRAL



Generates:



sentiment\_summary.csv



Bar chart: sentiment\_bar.png



✔ 4. Topic Extraction



Lightweight topic identification



Produces:



topics.csv



✔ 5. Cleaned Data Export



Stores processed text in cleaned\_data.csv



Shows formatted text ON the webpage (line-by-line)



✔ 6. Visual Results Page



Displays:



Cleaned text (beautifully formatted)



Sentiment summary table



Topics table



Generated images/charts



Download links for all result files



Modern CSS and layout



✔ 7. Fully Functional Flask Backend



/upload → uploads + analyzes



/results/... → serves result files



/ → landing upload page



🧠 Tech Stack

Backend



Python 3



Flask



pandas



pdfplumber



pytesseract



PIL (Pillow)



matplotlib



Frontend



HTML5



CSS3 (custom modern UI)



JavaScript (Drag \& Drop file upload)



📂 Project Structure

SocialMedia\_Content\_Analyzer/

│

├── app.py                         # Main Flask application

├── analyze.py (optional)          # Analyzer logic (if separated)

│

├── templates/

│   ├── index.html                 # Upload interface

│   └── result.html                # Display analysis results

│

├── static/

│   └── style.css                  # CSS styling

│

├── uploads/                       # Uploaded PDF \& image files

├── results/                       # Auto-generated analysis outputs

│

└── README.md                      # Project documentation



🛠 Installation \& Setup

1️⃣ Clone the repository

git clone https://github.com/abhinandan-shah/Social\_media\_content\_Analyzer.git

cd social-media-analyzer



2️⃣ Install required dependencies

pip install -r requirements.txt



3️⃣ Install Tesseract OCR



Required for reading text from image files.



Windows:



Download installer:

https://github.com/UB-Mannheim/tesseract/wiki



Add the installation path to system environment variables.



4️⃣ Run the application

python app.py





Visit:



http://127.0.0.1:5000



🔍 How It Works

Step 1 — Upload Files



User uploads PDF or images → stored in /uploads.



Step 2 — Text Extraction



PDF: extracted using pdfplumber



Images: extracted using pytesseract



Step 3 — Data Cleaning



Removes noise



Normalizes whitespace



Formats readable text for display



Step 4 — NLP Analysis



Sentiment classification



Topic extraction



Data export to CSV



Step 5 — Visualization



Sentiment bar chart



In-browser tables



Image previews



Step 6 — Result Page



User sees:



Tables



Charts



Download links



Cleaned text (line-by-line)



📁 Output Files Generated

File	Description

cleaned\_data.csv	Extracted, cleaned text

sentiment\_summary.csv	Sentiment counts

topics.csv	Auto-extracted keywords

sentiment\_bar.png	Visualization chart

wordcloud.png (optional)	Wordcloud visualization

🧪 Example Use Cases



✔ Extracting text from scanned resumes

✔ Analyzing feedback forms

✔ Understanding sentiment in handwritten notes

✔ Analyzing text-heavy reports

✔ Social media screenshot analysis

✔ Business document transcription📊 Social Media Content Analyzer



A web-based AI tool for extracting, cleaning, and analyzing text from PDF files and image documents (JPG/PNG) using OCR, followed by sentiment analysis, topic extraction, and data visualization.



This project is built as part of a technical assessment, demonstrating your ability to handle real-world data processing tasks including NLP, OCR, backend APIs, and frontend UI development.



🚀 Features

✔ 1. File Upload (PDF \& Images)



Upload multiple PDF or image files.



Drag-and-drop interface with modern UI.



Server automatically stores uploaded files.



✔ 2. Text Extraction



PDF Parsing using pdfplumber



OCR for images using pytesseract



Supports scanned documents and photos



Extracted text is normalized for analysis



✔ 3. Sentiment Analysis



Classifies text into:



POSITIVE



NEGATIVE



NEUTRAL



Generates:



sentiment\_summary.csv



Bar chart: sentiment\_bar.png



✔ 4. Topic Extraction



Lightweight topic identification



Produces:



topics.csv



✔ 5. Cleaned Data Export



Stores processed text in cleaned\_data.csv



Shows formatted text ON the webpage (line-by-line)



✔ 6. Visual Results Page



Displays:



Cleaned text (beautifully formatted)



Sentiment summary table



Topics table



Generated images/charts



Download links for all result files



Modern CSS and layout



✔ 7. Fully Functional Flask Backend



/upload → uploads + analyzes



/results/... → serves result files



/ → landing upload page



🧠 Tech Stack

Backend



Python 3



Flask



pandas



pdfplumber



pytesseract



PIL (Pillow)



matplotlib



Frontend



HTML5



CSS3 (custom modern UI)



JavaScript (Drag \& Drop file upload)



📂 Project Structure

SocialMedia\_Content\_Analyzer/

│

├── app.py                         # Main Flask application

├── analyze.py (optional)          # Analyzer logic (if separated)

│

├── templates/

│   ├── index.html                 # Upload interface

│   └── result.html                # Display analysis results

│

├── static/

│   └── style.css                  # CSS styling

│

├── uploads/                       # Uploaded PDF \& image files

├── results/                       # Auto-generated analysis outputs

│

└── README.md                      # Project documentation



🛠 Installation \& Setup

1️⃣ Clone the repository

git clone https://github.com/yourusername/SocialMediaContentAnalyzer.git

cd SocialMediaContentAnalyzer



2️⃣ Install required dependencies

pip install -r requirements.txt



3️⃣ Install Tesseract OCR



Required for reading text from image files.



Windows:



Download installer:

https://github.com/UB-Mannheim/tesseract/wiki



Add the installation path to system environment variables.



4️⃣ Run the application

python app.py





Visit:



http://127.0.0.1:5000



🔍 How It Works

Step 1 — Upload Files



User uploads PDF or images → stored in /uploads.



Step 2 — Text Extraction



PDF: extracted using pdfplumber



Images: extracted using pytesseract



Step 3 — Data Cleaning



Removes noise



Normalizes whitespace



Formats readable text for display



Step 4 — NLP Analysis



Sentiment classification



Topic extraction



Data export to CSV



Step 5 — Visualization



Sentiment bar chart



In-browser tables



Image previews



Step 6 — Result Page



User sees:



Tables



Charts



Download links



Cleaned text (line-by-line)



📁 Output Files Generated

File	Description

cleaned\_data.csv	Extracted, cleaned text

sentiment\_summary.csv	Sentiment counts

topics.csv	Auto-extracted keywords

sentiment\_bar.png	Visualization chart

wordcloud.png (optional)	Wordcloud visualization

🧪 Example Use Cases



✔ Extracting text from scanned resumes

✔ Analyzing feedback forms

✔ Understanding sentiment in handwritten notes

✔ Analyzing text-heavy reports

✔ Social media screenshot analysis

✔ Business document transcription

