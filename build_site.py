import os
import glob
import subprocess

# Notebook'ları HTML'e çevir
notebooks = glob.glob('*.ipynb')
for nb in notebooks:
    print(f"HTML'e çevriliyor: {nb}")
    subprocess.run(['jupyter', 'nbconvert', '--to', 'html', '--theme', 'dark', nb])

# index.html oluştur
html_content = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S&P 500 Kantitatif Araştırma Portföyü</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #121212;
            color: #ffffff;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }
        header {
            background-color: #1e1e1e;
            padding: 3rem 2rem;
            text-align: center;
            border-bottom: 3px solid #00B894;
        }
        h1 {
            margin: 0;
            font-size: 2.5rem;
            color: #00B894;
        }
        p.subtitle {
            font-size: 1.2rem;
            color: #b3b3b3;
            max-width: 800px;
            margin: 1rem auto 0;
        }
        .container {
            max-width: 1000px;
            margin: 3rem auto;
            padding: 0 2rem;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        .card {
            background-color: #1e1e1e;
            border-radius: 10px;
            padding: 2rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            text-decoration: none;
            color: inherit;
            display: block;
            border: 1px solid #333;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 184, 148, 0.2);
            border-color: #00B894;
        }
        .card h2 {
            margin-top: 0;
            color: #fff;
            font-size: 1.5rem;
            border-bottom: 2px solid #333;
            padding-bottom: 0.5rem;
        }
        .card p {
            color: #aaa;
            font-size: 1rem;
        }
        .tag {
            display: inline-block;
            background-color: #2d3436;
            color: #00B894;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            margin-top: 1rem;
            font-weight: bold;
        }
        footer {
            text-align: center;
            padding: 2rem;
            margin-top: 4rem;
            color: #777;
            font-size: 0.9rem;
            background-color: #1e1e1e;
        }
    </style>
</head>
<body>

<header>
    <h1>S&P 500 Kantitatif Araştırma Portföyü</h1>
    <p class="subtitle">İstatistiksel hipotez testleri ve veri bilimi kullanılarak piyasa anomalilerinin kanıtlanması.</p>
</header>

<div class="container">
    <div class="grid">
        
        <a href="H1_Tail_Risk_vs_Return.html" class="card">
            <h2>H1: Kuyruk Riski Ödüllendirilir mi?</h2>
            <p>Aşırı fiyat hareketi (Yüksek Kurtosis) sergileyen hisseler, uzun vadede yatırımcıya daha yüksek getiri sunar mı?</p>
            <div class="tag">Pearson Korelasyonu</div>
        </a>

        <a href="H2_H3_Seasonality.html" class="card">
            <h2>H2/H3: Mevsimsellik & Ocak Etkisi</h2>
            <p>Piyasada aylar arasında istatistiksel bir fark var mı? Ocak rallisi gerçek bir anomali mi, yoksa efsane mi?</p>
            <div class="tag">Tek Yönlü ANOVA / T-Testi</div>
        </a>

        <a href="H4_Weekend_Effect.html" class="card">
            <h2>H4: Hafta Sonu Etkisi (Cuma vs Pzt)</h2>
            <p>Piyasalar Cuma günleri gerçekten Pazartesi günlerine göre daha mı kârlı? Günlük log getirilerin analizi.</p>
            <div class="tag">Welch T-Testi / KDE Dağılım</div>
        </a>

    </div>
</div>

<footer>
    &copy; Furkan Çelik | Kantitatif Araştırma Portföyü
</footer>

</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html_content)

print("index.html ve tüm alt HTML sayfaları başarıyla oluşturuldu!")
