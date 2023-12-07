# Trying Out MLC

## Installation and Model Setup

```shell
python3 -m pip install --pre -U -f https://mlc.ai/wheels mlc-chat-nightly mlc-ai-nightly

port install git-lfs

git lfs install && mkdir -p dist/prebuilt
git clone https://huggingface.co/mlc-ai/mlc-chat-Llama-2-7b-chat-hf-q4f16_1 \
						  dist/prebuilt/mlc-chat-Llama-2-7b-chat-hf-q4f16_1

git clone https://github.com/mlc-ai/binary-mlc-llm-libs.git dist/prebuilt/lib
```

## Updating MLC and Model
```shell
python3 -m pip install --pre -U -f https://mlc.ai/wheels mlc-chat-nightly mlc-ai-nightly && \
pushd dist/prebuilt/lib && \
git pull && \
popd && \
pushd dist/prebuilt/mlc-chat-Llama-2-7b-chat-hf-q4f16_1 && \
git pull && \
popd
```

## Running Tests

```python
python3 -m unittest
```
