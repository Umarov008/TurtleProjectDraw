import os
import pandas as pd
import PyPDF2

# Fayl yolları
excel_file = "C:\\Users\\user.pondera\\666.xlsx"
pdf_folder = "C:\\Users\\user.pondera\\666"

# Excel faylını yükləyirik
df = pd.read_excel(excel_file, dtype=str)

# Sütunları müəyyən edirik
kodlar = df.iloc[:, 0].astype(str).tolist()  # 1-ci sütun: Kod
adlar = df.iloc[:, 1].astype(str).tolist()  # 2-ci sütun: Soyad Ad Ata adı
yeni_adlar = df.iloc[:, 2].astype(str).tolist()  # 3-cü sütun: "Açar söz - Kod"

# Qovluqdakı bütün PDF fayllarını alırıq
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

# Hər bir PDF faylı üçün yoxlama
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)

    # PDF faylını açırıq və içindəki mətni oxuyuruq
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        pdf_text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])

    # Excel siyahısı ilə müqayisə edirik
    for idx, ad in enumerate(adlar):
        if ad in pdf_text:
            yeni_ad = yeni_adlar[idx] + ".pdf"  # Yeni ad .pdf formatında olmalıdır
            yeni_path = os.path.join(pdf_folder, yeni_ad)

            # Faylı yenidən adlandırırıq
            os.rename(pdf_path, yeni_path)
            print(f"{pdf_file} -> {yeni_ad}")
            break  # Tapılan ilk uyğunluqdan sonra növbəti PDF-ə keçiririk