#!/usr/bin/env bash
# One-time setup for the free voiceover pipeline (Kokoro-82M, Apache-2.0). CPU only, no GPU needed.
# Needs: uv (https://docs.astral.sh/uv/) and ffmpeg.
#   Linux:  sudo apt install ffmpeg      macOS:  brew install ffmpeg uv
set -euo pipefail
VENV="${VENV:-$HOME/.venvs/kokoro}"
uv venv --python 3.12 "$VENV"
# shellcheck disable=SC1091
source "$VENV/bin/activate"
uv pip install --index-strategy unsafe-best-match --extra-index-url https://download.pytorch.org/whl/cpu \
  torch "kokoro>=0.9.4" ptts soundfile numpy num2words faster-whisper jiwer librosa
echo "Done. Activate with: source $VENV/bin/activate"
