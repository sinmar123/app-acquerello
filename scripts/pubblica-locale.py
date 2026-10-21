#!/usr/bin/env python3
"""Pubblica il sito su Cloudflare Pages dal PC, senza passare dal controllo su GitHub (npm run deploy).

Parte solo da main, senza modifiche non committate e allineato a origin/main: così in produzione
va sempre un commit approvato e unito, mai un ramo di lavoro o file toccati in locale. La strada
ordinaria resta il job «pubblica» di .github/workflows/sito.yml, che parte a ogni unione su main."""
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

WRANGLER = "wrangler@4.141.0"


def git(*argomenti):
    return subprocess.run(["git", *argomenti], capture_output=True, text=True, check=True).stdout.strip()


def ferma(motivo):
    raise SystemExit(f"pubblica-locale: {motivo}. Pubblicazione annullata.")


ramo = git("branch", "--show-current")
if ramo != "main":
    ferma(f"sei sul ramo «{ramo}», si pubblica solo da main")
if git("status", "--porcelain", "--untracked-files=no"):
    ferma("ci sono modifiche non committate")
git("fetch", "origin", "main")
if git("rev-parse", "HEAD") != git("rev-parse", "origin/main"):
    ferma("main locale non coincide con origin/main: fai prima git pull --ff-only")

subprocess.run([sys.executable, "scripts/genera-sito.py"], check=True)
npx = shutil.which("npx") or ferma("npx non trovato nel PATH")
subprocess.run([npx, "--yes", WRANGLER, "pages", "deploy", "site", "--project-name", "app-acquerello", "--branch", "main"], check=True)
