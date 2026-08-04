$ErrorActionPreference = "Stop"

Write-Host "Inizio Build del Progetto SIR Markov Chain..." -ForegroundColor Cyan

Write-Host "`n1. Installazione Dipendenze" -ForegroundColor Yellow
pip install -r requirements.txt -q

Write-Host "`n2. Esecuzione Test Unitari (Pytest)" -ForegroundColor Yellow
python -m pytest tests/ -v

Write-Host "`n3. Esecuzione Simulazione per generazione Plot" -ForegroundColor Yellow
python src/simulation.py --no-plot

Write-Host "`n4. Compilazione LaTeX: relazione.tex" -ForegroundColor Yellow
Set-Location -Path report
# Primo passaggio
pdflatex -interaction=nonstopmode relazione.tex | Out-Null
# Secondo passaggio (per riferimenti)
pdflatex -interaction=nonstopmode relazione.tex | Out-Null

Write-Host "`n5. Compilazione LaTeX: presentazione.tex (Beamer)" -ForegroundColor Yellow
# Primo passaggio
pdflatex -interaction=nonstopmode presentazione.tex | Out-Null
# Secondo passaggio
pdflatex -interaction=nonstopmode presentazione.tex | Out-Null

Set-Location -Path ..

Write-Host "`nBuild completata con successo! I PDF si trovano in report/" -ForegroundColor Green
