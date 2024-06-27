# About the Repository

This repository contains a Python application designed for real-time data processing and analysis. The application leverages Python's capabilities to handle data streams efficiently, making it suitable for real-time monitoring, analytics, or other dynamic data-driven tasks.

The Python applications in the repository include:

- Language Translation: Translates text from one language to another.
- Email Processing: Sends emails to recipients.
- Password Checker: Evaluates the uniqueness of passwords.
- PDF Operations: Merges, rotates, or adds watermarks to PDF files.
- Image Processing: Performs tasks such as blurring, smoothing, rotating, cropping, creating thumbnails, converting to grayscale, and resizing images.

## Features
- Real-time data processing
- Python-based architecture for flexibility and scalability
- Suitable for applications requiring live data analysis

## Getting Started
To get started with the Real-Time Python Application, follow these steps:

1. Clone the repository:
```
git clone https://github.com/Vishesh29/real-time-python-app.git
cd real-time-python-app
```

2. Install dependencies:
```
pip install -r requirements.txt
```

## Documentation for PyPDF2 library for PDF operations:
[PyPDF2](https://pypdf2.readthedocs.io/en/3.x/) : PyPDF2 is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. PyPDF2 can retrieve text and metadata from PDFs as well.

## Documentation for PIL library for Image Processing:
[PIL](https://pillow.readthedocs.io/en/stable/): The Python Imaging Library adds image processing capabilities to your Python interpreter. This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.


## Documentation for smtplib and email for Email Processing:
[smtplib](https://docs.python.org/3/library/smtplib.html) : The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon. For details of SMTP and ESMTP operation, consult RFC 821 (Simple Mail Transfer Protocol) and RFC 1869 (SMTP Service Extensions).

[email](https://docs.python.org/3/library/email.html) : The email package is a library for managing email messages. It is specifically not designed to do any sending of email messages to SMTP (RFC 2821), NNTP, or other servers; those are functions of modules such as smtplib and nntplib. 

## Documentation for hashlib library for Password checker:
[hashlib](https://docs.python.org/3/library/hashlib.html) : This module implements a common interface to many different secure hash and message digest algorithms. Included are the FIPS secure hash algorithms SHA1, SHA224, SHA256, SHA384, SHA512, the SHA-3 series, as well as RSA’s MD5 algorithm.

[SHA1 Hash Generator](https://passwordsgenerator.net/sha1-hash-generator/) : This online tool allows you to generate the SHA1 hash from any string. SHA1 is more secure than MD5. You can generate the sha1 checksum of your files to verify the identity of them later, or generate the SHA1 hashes of your users' passwords to prevent them from being leaked.

[Pwned Password](https://haveibeenpwned.com/Passwords) : To help the user check if the password is pawned before or not. This exposure makes them unsuitable for ongoing use as they're at much greater risk of being used to take over other accounts.

## Documentation for translate library for language translation:
[translate](https://translate-python.readthedocs.io/en/latest/) : Translate is a simple but powerful translation tool written in python with with support for multiple translation providers.


## Documentation for File and Text Translator
This Streamlit app allows users to translate text and text files between multiple languages. Users can choose between translating a block of text or uploading a text file for translation. The app supports several common languages and includes options for auto-detecting the source language.

### Features
- Text Translation: Enter text directly into the app and translate it to the desired language.
- File Translation: Upload a .txt file and translate its contents.
- Language Support: Supports translation between multiple languages, including but not limited to English, Japanese, Spanish, French, German, Chinese, Russian, Korean, Portuguese, Italian, Arabic, Hindi, Bengali, Urdu, and Punjabi.
- Auto-Detection: Option to auto-detect the source language.
- Download Translated File: After translating a file, download the translated content as a new text file.


### How to use:
```
streamlit run app.py
```

- Navigate to the App in Your Browser: Open the URL provided by Streamlit (typically http://localhost:8501).

### Usage
- Select Translation Type:

  - Choose "Translate Text" to translate a block of text.
  - Choose "Translate File" to upload and translate a text file.

- Select Source and Target Languages:

  - Use the dropdown menus to select the source and target languages. The source language can be set to "Auto-detect".

- Enter Text or Upload File:

  - For text translation, enter the text in the provided text area and click "Translate".
  - For file translation, upload a .txt file and click "Translate".

- View Translated Text:

  - For text translation, the translated text will be displayed below the input area.
  - For file translation, the translated text will be displayed, and a download button will be provided to download the translated content.

### Example
- Text Translation
  - Select "Translate Text".
  - Choose "English" as the source language and "Japanese" as the target language.
  - Enter the text "Hello, how are you?" and click "Translate".
  - The translated text "こんにちは、お元気ですか？" will be displayed.

- File Translation
  - Select "Translate File".
  - Choose "Auto-detect" as the source language and "Spanish" as the target language.
  - Upload a text file containing the text "Good morning, have a nice day!".
  - Click "Translate".
  - The translated text "Buenos días, ¡que tengas un buen día!" will be displayed, and a button will allow you to download the translated file.
